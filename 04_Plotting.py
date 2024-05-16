import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a random time series data
ts = pd.Series(np.random.randn(100), index=pd.date_range('today', periods=100))

# Plotting
st.title('Plotting Data')
st.write('Time Series Plot:')
st.write('**Developed by Naman Adep**')
st.line_chart(ts)