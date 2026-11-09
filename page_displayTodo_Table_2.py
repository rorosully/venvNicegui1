import sqlite3
import nicegui
from nicegui import ui

#COnfig
#import configDB
from configDB import currDB

#SCript to showTodo 
# Aug 2026
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

    #dateCreated = ui.input(label="Date created :").classes("w-full")
    #textbox = ui.textarea(label="Notes :").classes("w-full")
    #add Button

    #ui.button('Show Apiary Todo data', on_click=addnewdata)

    #add get all data button
    ui.button('Get all Todo data for this Apiary', on_click=getAlldata)
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




#list all data
#list_alldata = ui.column()

#reDisplay all data from table based on filter Date and Apiary name
def getAlldata():
    global apiary
    global list_alldata
    list_alldata = ui.column()

    cursor.execute("SELECT * FROM todo WHERE APIARY = ?  COLLATE NOCASE AND DATE >= ?",
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
            {"name": "APIARY", "label": "Apiary", "field": "APIARY"},
            {"name": "DATE", "label": "Date", "field": "DATE"},
            {"name": "TEXTBOX", "label": "Text", "field": "TEXTBOX"}

        ],
        #columns = columns,
        #columns = columns,
        rows = rows,
        row_key="APIARY",
        pagination={"page": 1, "rowsPerPage": 9},
        #pagination=True,
        selection='single',
        #rows = get_customers(),
        
      
        
        )
    #display record count
    ui.label(f'Total records found: {len(rows)}')
#Table columns





def get_customers():
    # Aug 26 add Filter Date entered
    cursor.execute("SELECT * FROM todo WHERE APIARY = ?  COLLATE NOCASE AND DATE >= ?",
                    (apiary.value, dateFilter.value))

    #columns = [ 'APIARY', 'DATE', 'TEXTBOX']                 
    #rows = cursor.fetchall()
    rows = [dict(row) for row in cursor.fetchall()] #gives error on l154
    print(rows)
   
    # Gives error 'valueError: dict update sequence element #1 has length 10; 2 is required'
    #return [dict(row) for row in rows] (To fix added conn.rowfactory line + 1 after it)

    #Gives error too -1 when pass columns as dict it gives unhashable type Dict
    #rows = [
    #    dict(zip(columns,row)) for row in rows
    #]
   
       
    #print(result) #ok, print to command line

#ui.run()
