import streamlit as st
from menu import menu
def Admin():
    menu()
    st.title("Admin")
    st.write("Welcome to the admin page!")
    st.write("This page is only accessible to users with the role 'admin'.")

if __name__ == "__main__":
    Admin()
