# email_capture.py

import streamlit as st

def capture_email():
    email = st.text_input("📧 Enter your email to get updates:")
    if email:
        st.success(f"Thanks! Updates will be sent to {email}")


