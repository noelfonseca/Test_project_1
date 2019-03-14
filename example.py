import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('SpreadsheetExample-b020928dcb91.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open('test').sheet1

# 

cell_list = wks.range('A1:C7')

for cell in cell_list:
    cell.value = 'O_o'

# Update in batch
wks.update_cells(cell_list)
