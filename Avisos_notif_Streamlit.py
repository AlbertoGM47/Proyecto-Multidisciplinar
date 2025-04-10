import streamlit as st

import streamlit as st

st.toast("¡Proceso completado con éxito!", icon="🎉")



# Simulamos una condición para mostrar el mensaje
mostrar_aviso = True  # Podrías usar alguna lógica para esto

st.title("Notificación previa al botón")

if mostrar_aviso:
    st.info("Ya puedes presionar el botón para continuar. 👇")

if st.button("Ejecutar acción"):
    st.success("¡Botón presionado y acción ejecutada!")
