import streamlit as st
import send_email

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message")
    button = st.form_submit_button("Submit")

    content_to_send = "subject:Portfolio webpage contact\n\n" + f"User email: {user_email} \n\nMessage: {message}"

    if button:
        send_email.send_email(content_to_send)
        st.info("Your email was sent successfully!")
