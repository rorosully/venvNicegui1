import sqlite3
import nicegui
from nicegui import ui

#COnfig
#import configDB
from configDB import currDB

import csv

#SCript to show all hive in a table 
# Oct 2026
#Update Oct '26 Show all data f6unction 'getAllData'  ,use ui.table
#database = configDB.currDB
database = currDB
#conn = sqlite3.connect('mydb52023.db')
conn = sqlite3.connect(database)
cursor = conn.cursor()

#add line from copilot oct '26
conn.row_factory = sqlite3.Row  # Return rows as dictionaries
cursor = conn.cursor()

# Why would you want to return rows as Dicts?
#conn.row_factory = sqlite3.Row  # Set row factory to return rows as dictionaries


#Display the input apiary fields
#Fields

def content():
    global apiary
    global dateFilter
    #global dateCreated
    #global textbox
    #apiary = ui.dropdown(label="Select Apiary", ['A', 'B', 'C'])
    #select = ui.select(['A', 'B', 'C'])
    with ui.dropdown_button("Apiary name", auto_close=False):
        ui.item('Saleen', on_click=lambda: ui.notify('You clicked Saleen'))
        ui.item('Kdooling', on_click=lambda: ui.notify('You clicked Saleen'))
                       
    apiary = ui.input(label="Apiary name :").classes("w-full")

    #Filter date
    dateFilter = ui.date_input(label="Date Filter (From) :").classes("w-full")
    dateFilter.picker.props('mask="DD-MM-YYYY"')


    #add get all data button
    ui.button('Get all Treatment data for this Apiary', on_click=getAlldata)
            #list all data
            
    #list_alldata = ui.column()

def addnewdata():
    
    global apiary
    global dateCreated
    global textbox
    
    try:
        cursor.execute('SELECT * FROM todo WHERE APIARY = ?', (apiary.value,))
        
                
        res = cursor.fetchall()
        if len(res) == 0:
                ui.notify(f"No todo found for apiary {apiary.value}")
        else:
             print(res)
             #apiary.value = res[0][1]
             dateCreated.value = res[0][1]
             textbox.value = res[0][2]
           
    #show success  data {hiveNumber.value}")
            #print(f"{hiveNumber, hiveNumber.value}")
             ui.notify(f"success TODO data {apiary.value}")
    
    except Exception as e:
        ui.notify(f"Error showing Todo data: {str(e)}")
        conn.rollback()

# EdIT FUNCTION
def editdata():
    pass

#DELETE FUNCTION
def deletebtn():
    pass

#add Button
#ui.button('Add Todo data', on_click=addnewdata)

#reDisplay all data from table based on filter Date and Apiary name
# Upd: allow blank 'APiary' entry to select all apiaries(not implemented)
def getAlldata():
    global apiary
    global dateFilter
    global list_alldata
    list_alldata = ui.column()
    
    #if not apiary.value:
    cursor.execute("SELECT * FROM treatment WHERE APIARY = ?  COLLATE NOCASE AND DATE_ADMINISTRATION >= ?",
                        (apiary.value, dateFilter.value))
    
    #try copilot following 2 lines
             # Fetch all rows
    rows = [dict(row) for row in cursor.fetchall()] #result empty talbe display
    
    print(rows) #ok, print to command line
    #add return statement
    #return rows #result no table , maybe return has to be last stmt

    table = ui.table(
        #add hard code colums
        #NOTE: 'field' must match the column name in the database table else empty table
        columns = [
            {"name": "MEDICINE_NAME", "label": "Medicine Name", "field": "MEDICINE_NAME"},
            {"name": "APIARY", "label": "Apiary", "field": "APIARY"},
            {"name": "DATE_ADMINISTRATION", "label": "Date", "field": "DATE_ADMINISTRATION"},
            {"name": "QTY_GIVEN", "label": "Quantity Given", "field": "QTY_GIVEN"},
            {"name": "HIVE_TREATED", "label": "Hive Treated", "field": "HIVE_TREATED"},
            {"name": "WITHDRAWAL_PERIOD", "label": "Withdrawal Period", "field": "WITHDRAWAL_PERIOD"},
            {"name": "TREATMENT_NOTE", "label": "Treatment Notes", "field": "TREATMENT_NOTE"},
        ],
        
        rows=rows,
        row_key="MEDICINE_NAME",
        pagination={"page": 1, "rowsPerPage": 9},
        selection="single",
        column_defaults={
            "align": "left",
            "headerClasses": "uppercase text-primary",
        },
    )
    #display record count
    ui.label(f'Total records found: {len(rows)}')
#Table columns





def get_customers():
    #  add Filter Date entered
    cursor.execute("SELECT * FROM hive WHERE APIARY = ?  COLLATE NOCASE AND DATE >= ?",
                    (apiary.value, dateFilter.value))
    
    rows = [dict(row) for row in cursor.fetchall()] #gives error on l154
    print(rows)
   
    # Gives error 'valueError: dict update sequence element #1 has length 10; 2 is required'
    #return [dict(row) for row in rows] (To fix added conn.rowfactory line + 1 after it)

    #Gives error too -1 when pass columns as dict it gives unhashable type Dict
    #rows = [
    #    dict(zip(columns,row)) for row in rows
    #]
   
       
    #print(result) #ok, print to command line

"""def export_csv(get_Alldata):
    rows = get_Alldata.rows
    columns = get_Alldata.columns
    with open('data.csv', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=[column['name'] for column in columns])
        writer.writeheader()
        writer.writerows(rows)
    ui.download('data.csv')
"""

#ui.button('Export to CSV', on_click=export_csv)   
    

#ui.run()
