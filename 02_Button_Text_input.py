import streamlit as st

st.title('Streamlit Widgets')
st.write('**Developed by Naman Adep**')

if st.button('Click Me'):
    st.write('Thanks for clicking!')

name = st.text_input('Enter your name:')
if name:
    st.write('Hello, ', name, '!')
