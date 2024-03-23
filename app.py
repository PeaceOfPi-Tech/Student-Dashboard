import streamlit as st 
from menu import menu

def app():
    st.title("App")
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
    menu() # Render the dynamic menu! 
    
    
if __name__ == "__main__":
    app()
