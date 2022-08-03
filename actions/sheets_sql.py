import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import sqlite3
import pandas as pd

def get_from_sheet():
    
    sheet_to_display = "DB- AY 2021-2022"
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(
    'creds.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open(sheet_to_display).sheet1
    return sheet.get_all_values()
  
  
class SQLite:
    DB_NAME = "db.sqlite"
  
    def __init__(self):
        self.conn = self.create_connection()
        self._get_or_create_table()
  
    @classmethod
    def create_connection(cls):
        conn = None
        try:
            conn = sqlite3.connect(cls.DB_NAME)
            return conn
        except Error as e:
            print(e)
        return conn
 
    def _get_or_create_table(self):
        """Creates the table if it does not exists"""
          
        create_table_sql = """CREATE TABLE IF NOT EXISTS details (
            timestamp varchar(20) PRIMARY KEY,
            name varchar(30) NOT NULL,
            year varchar(3) NOT NULL
        )"""
        try:
            
            # initializing the query cursor
            c = self.conn.cursor()
              
            # executes the create table query
            c.execute(create_table_sql)
        except Error as e:
            
            # prints the exception if any errors 
            # occurs during runtime
            print(e)
  
    def add_data_to_table(self, rows: list):
        """Inserts the data from sheets to the table"""
          
        # initializing sql cursor
        c = self.conn.cursor()
          
        # excluding the first row because it 
        # contains the headers
        insert_table_sql = """INSERT INTO details (timestamp, name, year) 
        VALUES (?, ?, ?);"""
        for row in rows[1:]:
            
            # inserts the data into the table
            # NOTE: the data needs to be in the order 
            # which the values are provided into the 
            # sql statement
            c.execute(insert_table_sql, tuple(row))
              
        # committing all the changes to the database
        self.conn.commit()
          
        # closing the connection to the database
        c.close()
  
  
if __name__ == '__main__':
    
    # fetches data from the sheets
    data = get_from_sheet()
  
    sqlite_util = SQLite()
    sqlite_util.add_data_to_table(data)