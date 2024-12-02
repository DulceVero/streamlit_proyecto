import streamlit as st

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
