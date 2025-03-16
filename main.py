import streamlit as st
import pandas as pd

# st.set_page_config(layout="wide")

col1, col2 = st.columns(2) #define 2 columns

with col1:
    st.image(r"G:\PYTHON PROJECTS\Portfolio Website\images\photo.jpg")

with col2:
    st.title("Farhan Fahmid")
    content = """
    Hey, I'm Farhan Fahmid! I am an aspiring Python Programmer, MBA student, and CSE graduate. I'm continuosly learning and improving my programming skills by building projects.
    """
    st.info(content)

st.info("Check out some of the Python projects I have worked on. And feel free to contact me anytime!")

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5]) #ratio of column widths

df = pd.read_csv(r"G:\PYTHON PROJECTS\Portfolio Website\data2.csv", encoding='ISO-8859-1') #sep tells that the data are separated by ;

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f"[Source Code]({row['code']})")
        st.write(f"[Check it Out]({row['demo']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f"[Source Code]({row['code']})")
        st.write(f"[Check it Out]({row['demo']})")
