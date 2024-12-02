import streamlit as st

st.title("Activación del Comité de Vivienda")

st.title("Datos de Voceros Activos")
with st.form("my_form"):
    col1, col2 = st.columns(2)

    with col1:
        nombre = st.text_input("Nombre")
        apellido = st.text_input("Apellido")
        cedula = st.text_input("Cédula")
        correo = st.email_input("Correo")

    with col2:
        edad = st.number_input("Edad")
        pais = st.selectbox("País", ["España", "México", "Argentina", "Estados Unidos"])

    # Botón para enviar el formulario
    submitted = st.form_submit_button("Guardar")
