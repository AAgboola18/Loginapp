import streamlit as st


st.title("Login")
Username = st.text_input("Username")
password = st.textP_input("Password", type="password")


st.button("Login")
