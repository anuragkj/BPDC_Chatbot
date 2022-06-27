# import json
# import gspread
# from oauth2client.service_account import ServiceAccountCredentials
# import sqlite3
# import pandas as pd

# con = sqlite3.connect('Dbase.db')
# sheet_to_display = "DB- AY 2021-2022"
# scope = ['https://spreadsheets.google.com/feeds',
#          'https://www.googleapis.com/auth/drive']
# creds = ServiceAccountCredentials.from_json_keyfile_name(
#     'creds.json', scope)
# client = gspread.authorize(creds)
# wb = client.open(sheet_to_display)
# #display_record = wb.get_all_records()
# # print(type(display_record))

# for sheet in wb:
#     wb[sheet].to_sql(sheet,con,index=False)
# con.commit()
# con.close()


https://towardsdatascience.com/writing-google-sheets-data-to-mysql-using-python-9cabe2ed88cd