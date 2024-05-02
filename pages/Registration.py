import streamlit as st

st.title("Registration page")

Firstname = st.text_input("First Name")
Surname = st.text_input("Surname")
Username = len(Firstname[0])+Surname
Password = st.text_input("Password", type="password")
confirm_pass = st.text_input("Confirm Password", type="password")

if st.button("Register"):
    if Password == confirm_pass:
        st.success("Registration successful!")
    else:
        st.error("Password do not match")

