import streamlit as st

formulario = st.form('practica')

st.write("Esto es una linea de Prueba")

@st.fragment()
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
