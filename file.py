import streamlit as st

st.title("Activación del Comité de Vivienda")

st.title("Datos de Voceros Activos")
with st.form("my_form"):
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        nombre = st.text_input("Nombre")
        apellido = st.text_input("Apellido")

    with col2:
        cedula = st.text_input("Cédula")
        correo = st.text_input("Correo")

    with col3:
        telefono = st.text_input("Número de Telefóno")
        edad = st.text_input("Edad")

    with col4:
        sexo = st.selectbox("Sexo", ["MASCULUINO", "FEMENINO"])
        tipo_voceria = st.radio("Tipo de Vocería", ["Principal", "Suplente"])

    
    # Botón para enviar el formulario
    submitted = st.form_submit_button("Guardar")


st.title("Formulario con 8 Campos en Streamlit")

with st.form("mi_formulario"):
    col1, col2 = st.columns(2)

    with col1:
        nombre = st.text_input("Nombre")
        apellido = st.text_input("Apellido")
        edad = st.number_input("Edad")
        pais = st.selectbox("País", ["España", "México", "Argentina", "Estados Unidos"])

    with col2:
        email = st.text_input("Email")
        telefono = st.text_input("Teléfono")
        fecha_nacimiento = st.date_input("Fecha de Nacimiento")
        intereses = st.multiselect("Intereses", ["Programación", "Data Science", "Machine Learning", "Inteligencia Artificial"])
