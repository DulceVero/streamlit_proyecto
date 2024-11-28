import streamlit as st

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
