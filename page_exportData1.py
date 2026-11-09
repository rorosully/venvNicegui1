import sqlite3
import nicegui
from nicegui import ui
import csv

#COnfig
#import configDB
from configDB import currDB

#SCript to export DB 
# try to export a table as CSV , write rows as csv file
# NOv 2026
#database = configDB.currDB
database = currDB
#conn = sqlite3.connect('mydb52023.db')
conn = sqlite3.connect(database)
cursor = conn.cursor()


# DOwnload the DB
# How do i export a table as csv?

def content():
  #  ui.button('Download Database', on_click=lambda: ui.download.file('configDB.py'))
    ui.button('Download script', on_click=lambda: ui.download.file('configDB.py'))
    
    #Button to export a SQLIte table as csv
    ui.button('Export table as CSV', on_click=export_table_as_csv)

def export_table_as_csv():


        try:
           # cursor.execute('SELECT * FROM treatment WHERE APIARY = "mx"')
            cursor.execute('SELECT * FROM treatment ')
                        
                    
            rows = cursor.fetchall()
            if len(rows) == 0:
                    ui.notify(f"No treatment found for apiary ")
            else:
                 print(rows)
              
                 with open ('todo_treatment.csv', 'w') as f:
                        writer = csv.writer(f)
                        # Write the column names
                        writer.writerow([description[0] for description in cursor.description])
                        # Write the data rows
            
                        
                        writer.writerows(rows)
                        ui.notify(f"success export Treatments ")
        except Exception as e:
            ui.notify(f"Error reading database Treatment data: {str(e)}")
            conn.rollback()
    





#ui.run()
