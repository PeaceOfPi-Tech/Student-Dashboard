import streamlit as st 

from menu import menu

def dashboard():
    menu()
    st.title("Dashboard")
    

if __name__ == "__main__":
    dashboard()
