import pygsheets
import pandas as pd

gc = pygsheets.authorize(service_file='D:\Allen\GoogleSheetTestkey\ Personal key')
sheet_url = ('https://docs.google.com/spreadsheets/ your own address')
google_sheet = gc.open_by_url(sheet_url)
wks_title=google_sheet.title
wks_list = google_sheet.worksheets()
print(wks_title, wks_list)


class google_sheet_helper:
    def __init__(self, sheet_name = "BtaxID"):
        # setting sheet        
        self.working_sheet = google_sheet.worksheet_by_title(sheet_name)

    def write(self, position = "A1", content = "test"):    
        self.working_sheet.update_value(position, content)

    def read(self, position = "A1"):
        content = self.working_sheet.cell(position)
        print(content)
        print(content.value)

    def append(self, values = []):
        self.working_sheet.append_table(values=values) 

    def insert(self, insert_rows = 1, values = []): # insert_rows = 1, start from 2
        self.working_sheet.insert_rows(insert_rows, number=1, values=values)

