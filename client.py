def update():
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
    # use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    # to select what spreadsheet and sheet you want ot select(by url: cahnge it, this is an example one):
    sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1J4zBSzftrlolololololololol0o").sheet1
    # Extract and print all of the values
    sheet.update_cell(8, 2, "prova2")
