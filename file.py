import streamlit as st
import pandas as pd

st.write("Esto es una linea de Prueba")
st.text_input('dato')


st.write(1234)
st.write(
    pd.DataFrame(
        {
            "first column": [1, 2, 3, 4],
            "second column": [10, 20, 30, 40],
        }
    )
)
