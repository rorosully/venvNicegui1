import sqlite3
import nicegui
from nicegui import ui

#COnfig
#import configDB
from configDB import currDB

#SCript to showTodo (using coPilot code)
# Oct 2026
#database = configDB.currDB
database = currDB
#conn = sqlite3.connect('mydb52023.db')
conn = sqlite3.connect(database)
cursor = conn.cursor()


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
    #ui.button('Get all Todo data for this Apiary', on_click=getAlldata)
            #list all data
    #OCt '26 call coPilot function
    ui.button('Get all Todo data for this Apiary', on_click=columns, rows = load_from_sqlite(database, 'todo'))
            
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

    global list_alldata
    list_alldata = ui.column()
        
    table = ui.table(
        
        #columns = columns,
        columns = columns,

        #try copilot following 2 lines
         # Fetch all rows
        # rows = [dict(row) for row in cursor.fetchall()]

        rows = get_customers(),
        #rows2 = cursor.fetchall(),
        #rows = rows2, not allowed
        ###get_customers(),
        #columns = [ 'APIARY', 'DATE', 'TEXTBOX']                 
        
       #try hard code a rows dict w. values. reslut= an empty table. (field was text, chg to TExtbox,ok)
       #  Why? because the rows are not being passed as a list of dicts.
        #rows = rows2,
        row_key = "apiary",
        pagination=4
        ,
        )
    
   
#Table columns
#columns = [
columns = [
    {"name": "APIARY", "label": "Apiary", "field": "apiary"},
    {"name": "DATE", "label": "Date", "field": "date"},
    {"name": "TEXTBOX", "label": "Text", "field": "Textbox"}

]

rows2 = [
    {"apiary": "Saleen", "date": "2023-08-01", "textbox": "Todo 1"},
    {"apiary": "Kdooling", "date": "2023-08-02", "textbox": "Todo 2"},
    {"apiary": "Saleen", "date": "2023-08-03", "textbox": "Todo 3"},
    {"apiary": "Kdooling", "date": "2023-08-04", "text": "Todo 4"}
]


def get_customers():
    # Aug 26 add Filter Date entered
    cursor.execute("SELECT * FROM todo WHERE APIARY = ?  COLLATE NOCASE AND DATE >= ?",
                    (apiary.value, dateFilter.value))

    #columns = [ 'APIARY', 'DATE', 'TEXTBOX']                 
    #rows = cursor.fetchall()
    rows = [dict(row) for row in cursor.fetchall()] #gives error on l154
    print(rows)
   
    # Gives error 'valueError: dict update sequence element #1 has length 10; 2 is required'
    #return [dict(row) for row in rows]

    #Gives error too -1 when pass columns as dict it gives unhashable type Dict
    #rows = [
    #    dict(zip(columns,row)) for row in rows
    #]
   
       
    #print(result) #ok, print to command line

#ui.run()

#OCt '26 coPilot code
def load_from_sqlite(db_path: str, table_name: str) -> tuple[list[dict], list[dict]]:
    """
    Load data from SQLite table and return columns and rows for NiceGui table.
    
    Args:
        db_path: Path to the SQLite database file
        table_name: Name of the table to read
        
    Returns:
        Tuple of (columns, rows) formatted for NiceGui
    """
    #insert my DB conn OCt2 4 line
    database = currDB
    conn = sqlite3.connect('mydb52023.db')
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

   # conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row  # Return rows as dictionaries
    cursor = conn.cursor()
    
    # Get column information
    cursor.execute(f"PRAGMA table_info({table_name})")
    column_info = cursor.fetchall()
    
    # Format columns for NiceGui
    columns = [
        {
            'name': col[1],
            'label': col[1].replace('_', ' ').title(),
            'field': col[1]
        }
        for col in column_info
    ]
    
    # Fetch all rows
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = [dict(row) for row in cursor.fetchall()]
    
    conn.close()
    
    return columns, rows
