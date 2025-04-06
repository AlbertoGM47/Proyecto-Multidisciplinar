import streamlit as st

st.title("Puesto de montaje en un entorno lean")

st.write("Esta es la app para el puesto de montaje de los ruedines. Aquí aparecerán los pedidos recibidos, junto con una guía paso a paso de qué piezas debes elegir y cómo deben ser ensambladas")

button1=st.button("Pedido nuevo")
if button1:
  st.write("Has pulsado en el boton :)")

like1 = st.checkbox("Soporte S1 seleccionado")
like2 = st.checkbox("Rueda WN2 seleccionado")
like3 = st.checkbox("Casquillo M12 seleccionado")
like4 = st.checkbox("Rodamiento seleccionado")
like5 = st.checkbox("Tornillo M8x60 seleccionado")
like6 = st.checkbox("Tuerca M8 seleccionado")

button2=st.button("Ensamblaje")
if button2:
  st.write(like1,like2,like3,like4,like5,like6)
