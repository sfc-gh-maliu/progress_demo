import streamlit as st
import time


for i in range(10):
    st.write("")

# progress_text = "Hang tight😬"
# my_bar = st.progress(0, text=progress_text)

col1, col2 = st.columns([1,1])
with col1:
    progress_text = "Hang tight😬"
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.1)
        if percent_complete == 50:
            progress_text = "Almost there🥹"
        if percent_complete == 98:
            progress_text = "Done🥰"
        my_bar.progress(percent_complete + 1, text=progress_text)
with col2:
    st.write("this is second col")
