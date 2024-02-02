import streamlit as st
from pages.1_test import test
from pages.2_asignaturas import mostrar_asignaturas

st.set_page_config(
    page_title="EmotutorIA",
    page_icon= "🤖"

)

st.title("¡Bienvenido a la Aplicación de Apoyo a Estudiantes!")
st.write("Esta aplicación te ayudará a mejorar tus habilidades de aprendizaje.")
st.write("Por favor, selecciona una opción en el menú lateral.")