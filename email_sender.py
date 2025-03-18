import requests
import streamlit as st

# Your Formspree endpoint
FORMSPREE_URL = "https://formspree.io/f/mnnpnozd"


def send_email(name, sender_email, message):
    """Sends a form submission to Formspree."""
    data = {
        "name": name,
        "email": sender_email,
        "message": message
    }

    response = requests.post(FORMSPREE_URL, data=data)

    if response.status_code == 200:
        return True
    else:
        return False



