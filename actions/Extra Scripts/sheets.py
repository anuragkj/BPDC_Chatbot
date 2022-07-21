import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

sheet_to_display = "DB- AY 2021-2022"
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(
    'creds.json', scope)
client = gspread.authorize(creds)
club_details_sheet = client.open(sheet_to_display).worksheet("Clubs")
club_details_display_record = club_details_sheet.get_all_records()
# print(type(display_record))

with open("Resources/club_details.json", "w") as of:
    json.dump(club_details_display_record, of)

event_details_sheet = client.open(sheet_to_display).worksheet("Events")
event_details_display_record = event_details_sheet.get_all_records()
# print(type(display_record))

with open("Resources/event_details.json", "w") as ef:
    json.dump(event_details_display_record, ef)      