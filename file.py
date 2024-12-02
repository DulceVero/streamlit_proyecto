import streamlit as st

formulario = st.form('practica')

st.write("Esto es una linea de Prueba")


def datos():
  cols = st.colums(2)
  cols[0].text_input('dato')
  cols[1].text_input('dato2')


option = st.selectbox(
  "Tipo de vehículo que usa",
  ("Moto", "Carro", "Camión", "Helicóptero"),
)

tipo = st.selectbox(
  "Tipo de animal",
  ("Hervivoro", "Carnivoro"),
)

st.title("Formulario Básico en Streamlit")

with st.form("my_form"):
    col1, col2 = st.columns(2)

    with col1:
        nombre = st.text_input("Nombre")
        email = st.text_input("Correo")

    with col2:
        edad = st.number_input("Edad")
        pais = st.selectbox("País", ["España", "México", "Argentina", "Estados Unidos"])

    # Botón para enviar el formulario
    submitted = st.form_submit_button("Guardar")
