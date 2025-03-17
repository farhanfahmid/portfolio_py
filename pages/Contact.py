import streamlit as st

from email_sender import send_mail

st.header("Contact Me")

with st.form(key="form"):
    user_email = st.text_input("Your email address please!")
    message_body = st.text_area("Enter your message")
    message = f"""\
Subject: New email from {user_email}
    
From: {user_email}
{message_body}
"""
    button1 = st.form_submit_button("Submit")

    if button1: #when submit button is clicked
        send_mail(message)
        st.info("Your email was sent successfully! Thanks for reaching out! I'll get back to you shortly.")