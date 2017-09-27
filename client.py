def update(x, y, data):
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
    # use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    # to select what spreadsheet and sheet you want ot select(by url):
    sheet = client.open_by_url("#############!!!##############!!!!put here your spreadsheet url").sheet1
    # Extract and print all of the values
    sheet.update_cell(x, y, data)
