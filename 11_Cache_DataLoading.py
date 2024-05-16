import streamlit as st
import pandas as pd
import time

@st.cache
def load_data():
    time.sleep(2)  # Simulating a time-consuming operation
    return pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
    })

st.title('Caching Example')
st.write('**Developed by Naman Adep**')

if st.button('Load Data'):
    data = load_data()
    st.write(data)
