import streamlit as st
import time


for i in range(10):
    st.write("")

progress_text = "Changing over time"
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1, text=progress_text)