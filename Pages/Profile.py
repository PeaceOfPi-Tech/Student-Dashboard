import streamlit as st

from menu import menu
from Services.Auth.Google import googleAuth

def profile():
    menu()
    #st.wirte the students name that is saved in the session state
    if "_name" not in st.session_state:
        student_name = ""
    else:
        student_name = st.session_state["_name"]
    st.title(f"Welcome to your profile {student_name}")
   
    get_sheets_service, get_drive_service = googleAuth()
    sheets_service = get_sheets_service()
    spreadSheet_Id = "1DNRf8wULVtEXTE8ij3X4F8U_-Nea9cRKzBW16ndV4sM"
    range_name = "Overview!F19:H26"

    result = sheets_service.spreadsheets().values().get(
            spreadsheetId=spreadSheet_Id, 
            range=range_name).execute()
    values = result.get('values', [])

    display_student_profile(values)

def display_student_profile(data):
    # Personal Information
    with st.container():
        st.subheader('Personal Information')
        for item in data: 
            st.write(f"**{item[0]}:** {item[2]}")

if __name__ == "__main__":
    profile()
