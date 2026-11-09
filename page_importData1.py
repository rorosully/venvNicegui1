import sqlite3
import nicegui
from nicegui import ui
import csv


#COnfig
#import configDB
from configDB import currDB

#SCript to export DB 
# try to import csv file to  a table 
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
    ui.button('Upload csv file', on_click=lambda: ui.download.file('configDB.py'))
    
    #Button to export a SQLIte table as csv
    ui.button('Upload csv file to TREATMENT table', on_click=export_table_as_csv)

def export_table_as_csv():


        try:
           # open the csv file
           # encoding is utf-8
            with open('todo_treatment.csv','r',encoding='utf-8') as csv_file: 
                csv_reader = csv.reader(csv_file)            
           #skip the header
                next(csv_reader)   

           #loop thru the csv file 
                for row in csv_reader:
                #insert the data into the table
                    cursor.execute('''INSERT INTO treatment (MEDICINE_NAME,APIARY,DATE_ADMINISTRATION,QTY_GIVEN,HIVE_TREATED,WITHDRAWAL_PERIOD,TREATMENT_NOTE) VALUES (?,?,?,?,?,?,?)''', (row[0], row[1], row[2], row[3], row[4], row[5], row[6])) 
                    #this not working ,runs but no insert
                    #cursor.execute("INSERT INTO treatment (MEDICINE_NAME,APIARY,DATE_ADMINISTRATION,QTY_GIVEN,HIVE_TREATED,WITHDRAWAL_PERIOD,TREATMENT_NOTE) VALUES (?,?,?,?,?,?,?)", row)
           #commit the changes         
                    conn.commit()
           #close the connection    
                   # conn.close() 
                    print(f"Inserted row: {row}")    
                    ui.notify(f"success import Treatments csv file")

        except Exception as e:
            ui.notify(f"Error importing  Treatment data: {str(e)}")
            conn.rollback()
    





#ui.run()
