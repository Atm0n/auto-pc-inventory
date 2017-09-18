import gspread
from oauth2client.service_account import ServiceAccountCredentials
# use creds to create a client to interact with the Google Drive API
link = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', link)  # need it
client = gspread.authorize(creds)
# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("prova").sheet1
# Extract and print all of the values
sheet.update_cell(8, 1, "prova2")
