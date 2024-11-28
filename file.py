import streamlit as st

st.write("Esto es una linea de Prueba")
st.text_input('dato')

option = st.selectbox(
  "Tipo de vehículo que usa",
  ("Moto", "Carro", "Camión", "Helicóptero"),
)

option2 = st.selectbox(
  "Tipo de vehículo que usa",
  ("Moto", "Carro", "Camión", "Helicóptero"),
)

option3 = st.selectbox(
  "Tipo de vehículo que usa",
  ("Moto", "Carro", "Camión", "Helicóptero"),
)

