import streamlit as st

st.write("Esto es una linea de Prueba")
st.text_input('dato')

option = st.selectbox(
  "Tipo de vehículo que usa",
  ("Moto", "Carro", "Camión", "Helicóptero"),
)
st.write("Su elección fue:", option)

option = st.selectbox(
  "Tipo de vehículo que usa",
  ("Moto", "Carro", "Camión", "Helicóptero"),
)
st.write("Su elección fue:", option)

option = st.selectbox(
  "Tipo de vehículo que usa",
  ("Moto", "Carro", "Camión", "Helicóptero"),
)
st.write("Su elección fue:", option)
