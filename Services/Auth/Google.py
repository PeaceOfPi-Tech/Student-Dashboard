from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

def googleAuth():
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
    creds = Credentials.from_service_account_file('Student_Dashboard_Credentials.json', scopes=SCOPES)
    def getSheetServive():
        return build('sheets', 'v4', credentials=creds)
    
    def getDriveService(): 
        return build('drive', 'v3', credentials=creds)
