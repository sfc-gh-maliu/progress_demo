import streamlit as st 
import numpy as np



for i in range(10):
    st.write("")
st.code('''st.button(label = "Button")''')
st.button(label = "Button")

st.code('''st.button(label = "Make your button as the container width", use_container_width = True)''')
with st.container():
    st.button(label = "Make your button as the container width", use_container_width = True)

