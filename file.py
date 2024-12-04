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
        cedula = st.number_input("Cédula")
        correo = st.text_input("Correo")
        descripción = st.text_area("Descripción")

    with col2:
        edad= st.text_input("Edad")
        telefono = st.text_input("Teléfono")
        sexo = st.selectbox("Sexo", ["MASCULUINO", "FEMENINO"])
        tipo_voceria = st.radio("Tipo de Vocería", ["Principal", "Suplente"])

    # Botón para enviar el formulario
    submitted = st.form_submit_button("Guardar")


# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)
