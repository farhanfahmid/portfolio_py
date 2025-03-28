import streamlit as st
import functions
import pandas as pd
from PIL import Image, ImageDraw

# st.set_page_config(layout="wide")

col1, col2 = st.columns(2) #define 2 columns

# with col1:
#     circular_img = functions.make_circle(r"G:\PYTHON PROJECTS\Portfolio Website\images\photo.jpg")
#     st.image(circular_img)

# with col1:
#     st.image(r"G:\PYTHON PROJECTS\Portfolio Website\images\farhan.png", use_container_width=True)

with col1:
    image_base64 = functions.get_base64_image("G:/PYTHON PROJECTS/Portfolio Website/images/farhan.png")

    st.markdown(f"""
        <img src="data:image/png;base64,{image_base64}" width="250" style="border-radius: 80%; margin-left: 50px">
    """, unsafe_allow_html=True)


with col2:
    st.title("Farhan Fahmid")
    content = """
    Hey, I'm Farhan Fahmid! I am an aspiring Python Programmer, MBA student, and CSE graduate. 
    I'm continuously learning and improving my programming skills by building projects. 
    In fact, this very website was created using the Python library streamlit!
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

# st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/farhan-fahmid-966935205/)", unsafe_allow_html=True)



# st.sidebar.markdown(
#     '<a href="https://www.linkedin.com/in/farhan-fahmid-966935205/" target="_blank" style="text-decoration: none;">'
#     '🔗 Connect on LinkedIn</a>',
#     unsafe_allow_html=True
# )
# st.sidebar.markdown(
#     '<a href="https://www.facebook.com/farhan.fahmid.3" target="_blank" style="text-decoration: none;">'
#     '🔗 Find me on Facebook</a>',
#     unsafe_allow_html=True
# )

