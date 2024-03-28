import streamlit as st 
from menu import menu
from Models.Names import Names
from Services.Auth.Google import googleAuth

def app():
    st.set_page_config(layout="wide")
    get_sheets_service, get_drive_service = googleAuth()
    sheets_service = get_sheets_service()
    st.title("App")
    student_names = Names()
    # Initialize st.session_state.role to None
    if "role" not in st.session_state:
        st.session_state.role = None

    # Retrieve the role from Session State to initialize the widget
    st.session_state._role = st.session_state.role

    def set_role():
        # Callback function to save the role selection to Session State
        st.session_state.role = st.session_state._role

    # Selectbox to choose role
    st.selectbox(
        "Select your role:",
        ["User", "Admin"],
        key="_role",
        on_change=set_role,
    )
    spreadsheetID = "1DNRf8wULVtEXTE8ij3X4F8U_-Nea9cRKzBW16ndV4sM"
    student_name = st.selectbox(
        "Name:",
        student_names.names,
        key = '_name',
    )

    #Update student name in base spreadsheet
    if student_name:
        sheets_service.spreadsheets().values().update( 
            spreadsheetId=spreadsheetID, 
            range="Overview!B1", 
            valueInputOption="USER_ENTERED", 
            body={"values": [[student_name]]}
        ).execute()
    menu() # Render the dynamic menu! 
    
    
if __name__ == "__main__":
    app()
