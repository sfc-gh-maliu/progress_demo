import streamlit as st
import time


for i in range(10):
    st.write("")

progress_text = "Hang tight"
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.1)
    if percent_complete == 50:
        progress_text = "Almost there"
    if percent_complete == 99:
        progress_text = "Done!"
    my_bar.progress(percent_complete + 1, text=progress_text)