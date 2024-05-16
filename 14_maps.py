import streamlit as st
import pandas as pd

data = pd.DataFrame({
    'lat': [28.6139, 19.0760, 12.9716, 17.3850], 
    'lon': [77.2090, 72.8777, 77.5946, 78.4867],
    'name': ['Delhi', 'Mumbai', 'Bengaluru', 'Hyderabad']
})

st.title('Maps Integration')
st.write('**Developed by Naman Adep**')
st.map(data)
