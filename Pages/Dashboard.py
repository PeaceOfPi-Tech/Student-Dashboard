import streamlit as st 
import pandas as pf
import plotly.express as px

from Services.Auth.Google import googleAuth
from menu import menu

def dashboard():
    get_sheets_service, get_drive_service = googleAuth()
    sheets_service = get_sheets_service()
    spreadSheet_Id = "1DNRf8wULVtEXTE8ij3X4F8U_-Nea9cRKzBW16ndV4sM"
    range_name = "Overview!A3:D36"

    result = sheets_service.spreadsheets().values().get(
        spreadsheetId=spreadSheet_Id, 
        range=range_name).execute()
    values = result.get('values', [])

    filtered_data = [row for row in values if len(row) == 4]
    print(filtered_data)
    df = pf.DataFrame(filtered_data,columns = ['Test Name' , 'Score' , 'Order','Date'])
    df['Score'] = pf.to_numeric(df['Score'],errors='coerce')
    df['Order'] = pf.to_numeric(df['Order'],errors='coerce')
    df.dropna(inplace=True)

    menu()
    st.title("Dashboard")
    col1 , col2, _= st.columns(3) 
    with col1:
        st.write(df.to_html(index=False), unsafe_allow_html=True)
    with col2:
        fig = px.line(df, x='Date', y='Score')

        # Customize hover information
        fig.update_traces(mode='lines+markers', hovertemplate='Score: %{y} <br>%{text}', text=df['Test Name'])

        fig.update_layout(hovermode="closest",  # Show data for closest point on hover
                          xaxis_title='Date',
                          yaxis_title='Score',
                          yaxis=dict(range=[400, 800]),  # Set y-axis range
                          showlegend=False)  # Hide legend if not necessary
        st.plotly_chart(fig,user_container_width=True,config = {'displayModeBar': False})

if __name__ == "__main__":
    dashboard()
