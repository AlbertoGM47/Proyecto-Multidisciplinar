import streamlit as st

st.title("Puesto de montaje en un entorno lean")

st.write("Esta es la app para el puesto de montaje de los ruedines. Aquí aparecerán los pedidos recibidos, junto con una guía paso a paso de qué piezas debes elegir y cómo deben ser ensambladas")

import streamlit as st

st.toast("¡Proceso completado con éxito!", icon="🎉")

button1=st.button("Pedido nuevo")
if button1:
  st.write("Has pulsado en el boton.🤝")

like1 = st.checkbox("Soporte S1 seleccionado")
like2 = st.checkbox("Rueda WN2 seleccionado")
like3 = st.checkbox("Casquillo M12 seleccionado")
like4 = st.checkbox("Rodamiento seleccionado")
like5 = st.checkbox("Tornillo M8x60 seleccionado")
like6 = st.checkbox("Tuerca M8 seleccionado")

if like1 and like2 and like3 and like4 and like5 and like6:
    button2 = st.button("Ensamblaje")
    if button2:
        st.write("Has pulsado en el botón ensamblaje, aquí aparecerían los pasos a seguir para montarlo.")

st.image('IMG-20250325-WA0017.jpeg')

st.header("Ensamblaje")

Respuesta=st.radio("(Una Pregunta)",("Opcion 1","Opcion 2","Opcion 3"))
button3= st.button("Aceptar")
if button3:
  st.write(Respuesta)
  if Respuesta == "Opcion 1":
    st.write("Has elegido la Opcion 1")


Multirespuesta = st.multiselect("Escoge varias opciones",["Multirespuesta1","Multirespuesta2","Multirespuesta3","Multirespuesta4"])
button4= st.button("Mostrar multirespuesta")
if button4:
                   st.write(Multirespuesta)


Control_deslizante=st.slider("Escoge un valor del 1 al 100",1,100)

Control_deslizante=st.slider("Escoge un valor del 1 al 100",1,100,10)

texto_usuario = st.text_input("Escribe aqui lo que quieras")
if st.button("Aceptar texto"):
  st.write(texto_usuario)


numero_usuario = st.number_input("Escribe aqui un numero")
if st.button("Aceptar numero"):
  st.write(numero_usuario)

