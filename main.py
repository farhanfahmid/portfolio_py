import streamlit as st

# st.set_page_config(layout="wide")

col1, col2 = st.columns(2) #define 2 columns

with col1:
    st.image(r"G:\PYTHON PROJECTS\Portfolio Website\images\photo.jpg")

with col2:
    st.title("Farhan Fahmid")
    content = """
    Hey, I'm Farhan Fahmid! I am a Python Programmer, MBA student, and CSE graduate. Check out my Python projects below1
    """
    st.info(content)