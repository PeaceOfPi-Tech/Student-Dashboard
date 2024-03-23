import streamlit as st

from menu import menu

def profile():
    menu()
    st.title("Profile")
    st.write("Welcome to the profile page!")

if __name__ == "__main__":
    profile()
