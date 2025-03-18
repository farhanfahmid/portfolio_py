# import streamlit as st
#
# from email_sender import send_mail
#
# st.header("Contact Me")
#
# with st.form(key="form"):
#     user_email = st.text_input("Your email address please!")
#     message_body = st.text_area("Enter your message")
#     message = f"""\
#     Subject: New email
#
#     From: {user_email}
#
#     {message_body}
# """
#     button1 = st.form_submit_button("Submit")
#
#     if button1: #when submit button is clicked
#         send_mail(message)
#         st.info("Your email was sent successfully! Thanks for reaching out! I'll get back to you shortly.")

import requests
import streamlit as st

# Your Formspree endpoint
FORMSPREE_URL = "https://formspree.io/f/mnnpnozd"


def send_email(name, sender_email, message):
    """Sends a form submission to Formspree."""
    headers = {"Accept": "application/json"}
    data = {
        "name": name,
        "email": sender_email,
        "message": message
    }

    response = requests.post(FORMSPREE_URL, headers=headers, data=data)

    # Print debug info
    # st.write(f"Response Code: {response.status_code}")
    # st.write(f"Response Text: {response.text}")

    return response.status_code == 200



# Streamlit UI
st.title("Mail Me")

name = st.text_input("Your Name")
email = st.text_input("Your Email")
message = st.text_area("Your Message")

if st.button("Send"):
    if name and email and message:  # Ensure all fields are filled
        success = send_email(name, email, message)
        if success:
            st.success("Message sent successfully! 🎉")
        else:
            st.error("Failed to send message. Please try again later.")
    else:
        st.warning("Please fill out all fields before sending.")


st.sidebar.markdown(
    '<a href="https://www.linkedin.com/in/farhan-fahmid-966935205/" target="_blank" style="text-decoration: none;">'
    '🔗 Connect on LinkedIn</a>',
    unsafe_allow_html=True
)
st.sidebar.markdown(
    '<a href="https://www.facebook.com/farhan.fahmid.3" target="_blank" style="text-decoration: none;">'
    '🔗 Find me on Facebook</a>',
    unsafe_allow_html=True
)

