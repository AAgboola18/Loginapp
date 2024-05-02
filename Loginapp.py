import streamlit as st


st.title("Login")
Username = st.text_input("Username")
password = st.text_input("Password", type="password")


if st.button("Login"):
    if Username == "admin" and password == "admin1":
        st.success("Logging successful ")
    else:
        st.error("Invalid username or password.")



