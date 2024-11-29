import streamlit as st

formulario = st.form('practica')

st.write("Esto es una linea de Prueba")
st.text_input('dato')

option = st.selectbox(
  "Tipo de vehículo que usa",
  ("Moto", "Carro", "Camión", "Helicóptero"),
)

tipo = st.selectbox(
  "Tipo de animal",
  ("Hervivoro", "Carnivoro"),
)

st.title("My Awesome App")

@st.fragment()
def toggle_and_text():
    cols = st.columns(2)
    cols[0].toggle("Toggle")
    cols[1].text_area("Enter text")
