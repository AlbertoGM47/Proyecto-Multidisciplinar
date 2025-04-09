import sqlite3
import os
import funciones_bd as fn
import paho.mqtt.client as mqtt
from datetime import datetime
import streamlit as st

st.title("Puesto de montaje en un entorno lean")

st.write("Esta es la app para el puesto de montaje de los ruedines. Aquí aparecerán los pedidos recibidos, junto con una guía paso a paso de qué piezas debes elegir y cómo deben ser ensambladas")

## Base de datos
DB_PATH = "BD_Puesto_Lean_copia.db"  # Ruta de la base de datos

## MQTT Configuration
MQTT_BROKER = "192.168.105.32"
MQTT_PORT = 1884
MQTT_TOPIC = "ESP8266"
MQTT_USERNAME = "usuario_mqtt"
MQTT_PASSWORD = "daniel1234"

## Funciones de conexion y suscripcion al broker MQTT

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado al broker MQTT")

        #Me suscribo al topico de interes
        client.subscribe(MQTT_TOPIC)
        print(f"Suscrito al topic {MQTT_TOPIC}")
        
    else:
        print(f"Fallo en la conexión, codigo de error: {rc}")

def on_message(client, userdata, msg):
    print(f"Mensaje recibido: {msg.payload.decode()} en el tópico {msg.topic}")

    if msg.payload.decode().startswith("pedido_"):
        try:
            # Extraer datos del mensaje
            _, cliente, referencia, unidades = msg.payload.decode().split("_")
            unidades = int(unidades)  # Convertir unidades a entero
            timestamp = int(datetime.now().timestamp())  # Obtener timestamp actual
            st.toast("¡Pedido nuevo! Haz click en el boton 'Pedido Nuevo' para ver el pedido", icon="🎉" ) # Notificacion de pedido
            #AÑADIR SONIDO
            button1=st.button("Pedido nuevo") # Añadir botón para mostrar el pedido en Streamlit
            if button1:
                st.write(_, cliente, referencia, unidades) #Mostrar el pedido en Streamlit

            # Conectar a la base de datos
            connection = sqlite3.connect(DB_PATH)
            cursor = connection.cursor()

            # Verificar los componentes necesarios para la referencia
            cursor.execute("SELECT Ref_hijo FROM BOM WHERE Ref_padre = ?", (referencia,))
            componentes = cursor.fetchall()

            if not componentes:
                print(f"No se encontraron componentes para la referencia {referencia}")
                connection.close()
                return

            # Verificar el stock de cada componente y aplicar FIFO
            stock_suficiente = True
            componentes_a_pedir = []
            coste_total = 0  # Inicializar el coste total

            for componente in componentes:
                componente = componente[0]
                cursor.execute(
                    "SELECT ID, Stock, CosteUnitario, FechaIngreso FROM Componente_Bien WHERE Nombre = ? ORDER BY FechaIngreso ASC",
                    (componente,)
                )
                filas = cursor.fetchall()

                stock_necesario = unidades
                for fila in filas:
                    id_componente, stock_actual, coste_unitario, fecha_ingreso = fila

                    if stock_actual >= stock_necesario:
                        # Consumir completamente del stock actual
                        nuevo_stock = stock_actual - stock_necesario
                        cursor.execute("UPDATE Componente_Bien SET Stock = ? WHERE ID = ?", (nuevo_stock, id_componente))
                        coste_total += coste_unitario * stock_necesario
                        stock_necesario = 0
                        break
                    else:
                        # Consumir parcialmente y continuar con la siguiente fila
                        stock_necesario -= stock_actual
                        coste_total += coste_unitario * stock_actual
                        cursor.execute("UPDATE Componente_Bien SET Stock = 0 WHERE ID = ?", (id_componente,))

                if stock_necesario > 0:
                    stock_suficiente = False
                    cantidad_a_pedir = stock_necesario
                    componentes_a_pedir.append((componente, cantidad_a_pedir))

            if stock_suficiente:
                # Insertar el pedido en la tabla
                cursor.execute("SELECT MAX(ID) FROM pedidos")
                max_id = cursor.fetchone()[0]
                next_id = max_id + 1 if max_id is not None else 1

                cursor.execute("SELECT MAX(orden_fabricacion) FROM pedidos")
                max_orden = cursor.fetchone()[0]
                next_orden = max_orden + 1 if max_orden is not None else 1

                cursor.execute('''INSERT INTO pedidos (ID, cliente, fecha, referencia, unidades, orden_fabricacion, estado)
                                  VALUES (?, ?, ?, ?, ?, ?, ?)''',
                               (next_id, cliente, timestamp, referencia, unidades, next_orden, "PENDIENTE"))

                connection.commit()
                print(f"Pedido procesado correctamente: Cliente={cliente}, Referencia={referencia}, Unidades={unidades}, Coste Total={coste_total:.2f}")

                # Verificar el stock total de cada componente después del pedido
                for componente in componentes:
                    componente = componente[0]
                    cursor.execute("SELECT SUM(Stock) FROM Componente_Bien WHERE Nombre = ?", (componente,))
                    stock_total = cursor.fetchone()[0]

                    # Obtener el stock mínimo del componente
                    cursor.execute("SELECT Stock_minimo FROM Stock_Minimo WHERE Nombre = ?", (componente,))
                    resultado = cursor.fetchone()
                    if resultado:
                        stock_minimo = resultado[0]
                        if stock_total < stock_minimo:
                            mensaje_pedir = f"PEDIR {stock_minimo - stock_total} de {componente}"
                            client.publish(MQTT_TOPIC, mensaje_pedir)
                            print(f"Stock total por debajo del mínimo para {componente}. {mensaje_pedir}")
                    else:
                        print(f"El componente {componente} no tiene un valor definido en la tabla Stock_Minimo")
            else:
                # Informar sobre los componentes que deben pedirse
                for componente, cantidad_a_pedir in componentes_a_pedir:
                    mensaje_pedir = f"PEDIR {cantidad_a_pedir} de {componente}"
                    client.publish(MQTT_TOPIC, mensaje_pedir)
                    print(f"Stock insuficiente para {componente}. {mensaje_pedir}")

            connection.close()
        except Exception as e:
            print(f"Error al procesar el mensaje: {e}")

    elif msg.payload.decode().startswith("caja_"):
        try:
            # Extraer datos del mensaje
            _, proveedor, coste_unitario, componente, unidades = msg.payload.decode().split("_")
            coste_unitario = float(coste_unitario)  # Convertir coste unitario a float
            unidades = int(unidades)  # Convertir unidades a entero
            fecha_ingreso = int(datetime.now().timestamp())  # Fecha de ingreso actual

            # Conectar a la base de datos
            connection = sqlite3.connect(DB_PATH)
            cursor = connection.cursor()

            # Obtener el stock mínimo del componente desde la tabla Stock_Minimo
            cursor.execute("SELECT Stock_minimo FROM Stock_Minimo WHERE Nombre = ?", (componente,))
            resultado = cursor.fetchone()
            if resultado:
                stock_minimo = resultado[0]
            else:
                raise ValueError(f"El componente {componente} no tiene un valor definido en la tabla Stock_Minimo")

            # Insertar una nueva fila para el componente
            cursor.execute("INSERT INTO Componente_Bien (Nombre, Descripcion, CosteUnitario, Proveedor, Stock, Stock_minimo, FechaIngreso) VALUES (?, ?, ?, ?, ?, ?, ?)",
                        (componente, None, coste_unitario, proveedor, unidades, stock_minimo, fecha_ingreso))
            print(f"Nuevo registro creado: Componente={componente}, Proveedor={proveedor}, CosteUnitario={coste_unitario}, Unidades añadidas={unidades}, Stock mínimo={stock_minimo}")

            connection.commit()
            connection.close()
        except Exception as e:
            print(f"Error al procesar el mensaje de caja: {e}")

    elif msg.payload.decode().startswith("estado_pedido_"):
        try:
            # Extraer datos del mensaje
            _, _, orden_fabricacion, estado = msg.payload.decode().split("_")
            orden_fabricacion = int(orden_fabricacion)  # Convertir orden de fabricación a entero
            timestamp_actual = int(datetime.now().timestamp())  # Obtener timestamp actual

            # Conectar a la base de datos
            connection = sqlite3.connect(DB_PATH)
            cursor = connection.cursor()

            if estado == "enProceso":
                # Actualizar el estado a "EN PROCESO" y registrar el tiempo de inicio
                cursor.execute('''UPDATE pedidos 
                                  SET estado = ?, tiempo_inicio = ? 
                                  WHERE orden_fabricacion = ?''',
                               ("EN PROCESO", timestamp_actual, orden_fabricacion))
                print(f"Pedido con orden de fabricación {orden_fabricacion} actualizado a EN PROCESO.")

            elif estado == "terminado":
                # Actualizar el estado a "TERMINADO", registrar el tiempo de fin y calcular la duración
                cursor.execute('''SELECT tiempo_inicio FROM pedidos WHERE orden_fabricacion = ?''', (orden_fabricacion,))
                tiempo_inicio = cursor.fetchone()
                if tiempo_inicio and tiempo_inicio[0] is not None:
                    tiempo_inicio = tiempo_inicio[0]
                    duracion = timestamp_actual - tiempo_inicio
                    cursor.execute('''UPDATE pedidos 
                                      SET estado = ?, tiempo_fin = ?, duracion = ? 
                                      WHERE orden_fabricacion = ?''',
                                   ("TERMINADO", timestamp_actual, duracion, orden_fabricacion))
                    print(f"Pedido con orden de fabricación {orden_fabricacion} actualizado a TERMINADO. Duración: {duracion} segundos.")
                else:
                    print(f"No se encontró un tiempo de inicio para el pedido con orden de fabricación {orden_fabricacion}. No se puede calcular la duración.")

            connection.commit()
            connection.close()
        except Exception as e:
            print(f"Error al procesar el mensaje de pedido: {e}")

def main():
    # Configurar cliente MQTT
    client = mqtt.Client()
    client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
    client.on_connect = on_connect
    client.on_message = on_message

    # Conectar al broker MQTT
    client.connect(MQTT_BROKER, MQTT_PORT,)

    # Iniciar el loop para mantener la conexión
    client.loop_start()

    fn.create_database()
    # fn.rellenar_tabla()

    # Aquí puedes agregar otras funciones o lógica de tu programa
    input("Presiona Enter para salir...\n")  # Mantener el programa corriendo

    # Detener el loop y desconectar
    client.loop_stop()
    client.disconnect()

if __name__ == "__main__":
    main()


