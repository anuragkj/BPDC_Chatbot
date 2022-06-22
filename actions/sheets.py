import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

sheet_to_display = "DB- AY 2021-2022"
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(
    'creds.json', scope)
client = gspread.authorize(creds)
sheet = client.open(sheet_to_display).sheet1
display_record = sheet.get_all_records()

with open("output_file.json", "w") as of:
    json.dump(display_record, of)