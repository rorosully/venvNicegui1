import sqlite3
import nicegui
from nicegui import ui

#COnfig
#import configDB
from configDB import currDB

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

    #dateCreated = ui.input(label="Date created :").classes("w-full")
    #textbox = ui.textarea(label="Notes :").classes("w-full")
    #add Button

    #ui.button('Show Apiary Todo data', on_click=addnewdata)

    #add get all data button
    ui.button('Get all Hive data for this Apiary', on_click=getAlldata)
            #list all data
            
    #list_alldata = ui.column()


# EdIT FUNCTION
def editdata():
    pass

#DELETE FUNCTION
def deletebtn():
    pass

"""selected_name = None

def load_names_from_db(db_path='mydb52023.db', table_name='apiary', column_name='APIARY_NAME'):
    #Load names from SQLite database with error handling
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(f'SELECT {column_name} FROM {table_name}')
        names = [row[0] for row in cursor.fetchall()]
        conn.close()
        return names
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []

def on_selection(name):
    #Handle selection from dropdown button
    global selected_name
    selected_name = name
    button.set_text(f'✓ {name}')
    status.set_text(f'Current selection: {selected_name}')
    menu.close()
    print(f"Selected name: {selected_name}")


# Load names from database
names = load_names_from_db()

# Create the UI
with ui.column().classes('w-full max-w-md m-auto p-6'):
    ui.label('Name Selection').classes('text-2xl font-bold mb-4')
    
    if names:
        # Create dropdown button with styling
        with ui.button(icon='person').props('no-caps color=primary') as button:
            button.set_text('Select a Name')
            with ui.menu() as menu:
                for name in names:
                    ui.menu_item(name, lambda n=name: on_selection(n))
        
        status = ui.label('No selection yet').classes('text-sm text-gray-600 mt-4 p-2')
    else:
        ui.label('No names found in database').classes('text-red-500')    

"""


#list all data
#list_alldata = ui.column()

#reDisplay all data from table based on filter Date and Apiary name
# Upd: allow blank 'APiary' entry to select all apiaries
def getAlldata():
    global apiary
    global list_alldata
    list_alldata = ui.column()
    
    #if not apiary.value:
    cursor.execute("SELECT * FROM hive WHERE APIARY = ?  COLLATE NOCASE AND DATE_CREATED >= ?",
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
            {"name": "HIVE_NO", "label": "Hive Number", "field": "HIVE_NO"},
            {"name": "APIARY", "label": "Apiary", "field": "APIARY"},
            {"name": "DATE_CREATED", "label": "Date", "field": "DATE_CREATED"},
            {"name": "SUPERS", "label": "Supers", "field": "SUPERS"},
            {"name": "SWARMED", "label": "Swarmed", "field": "SWARMED"},
            {"name": "NUM_NUCS_MADE", "label": "Nucs Made", "field": "NUM_NUCS_MADE"},
            {"name": "QUEEN_SOURCE", "label": "Queen Source", "field": "QUEEN_SOURCE"},
        ],
        
        rows=rows,
        row_key="HIVE_NO",
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

#ui.run()
