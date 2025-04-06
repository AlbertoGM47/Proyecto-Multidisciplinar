import streamlit as st

st.title("Puesto de montaje en un entorno lean")

st.write("Esta es la app para el puesto de montaje de los ruedines. Aquí aparecerán los pedidos recibidos, junto con una guía paso a paso de qué piezas debes elegir y cómo deben ser ensambladas")

button1=st.button("Pedido nuevo")
if button1:
  st.write("Has pulsado en el boton :)")

like = st.checkbox("Soporte SP1 seleccionado")

