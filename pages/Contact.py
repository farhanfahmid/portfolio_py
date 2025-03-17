import streamlit as st

st.header("Contact Me")

with st.form(key="form"):
    user_email = st.text_input("Your email address please!")
    message = st.text_area("Enter your message")
    button1 = st.form_submit_button("Submit")

    if button1: #when submit button is clicked
        print("I was clicked")