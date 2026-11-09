import sqlite3
from matplotlib.table import table
import nicegui
from nicegui import ui

#COnfig
#import configDB
from configDB import currDB

#SCript to showTodo 
# try to display Table value and not a Card for every row
# Aug 2026
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
        #ui.item('Kdooling', on_click=lambda: ui.notify('You clicked Saleen'))
                       
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

    global list_alldata
    list_alldata = ui.column()
        
    #cursor.execute("SELECT * FROM todo WHERE APIARY = ?  COLLATE NOCASE", (apiary.value,))
    
    #Aug 26 add Filter Date entered
    cursor.execute("SELECT * FROM todo WHERE APIARY = ?  COLLATE NOCASE AND DATE >= ?",
                    (apiary.value, dateFilter.value))
                     
    res = cursor.fetchall()
   # for row in results:
   #     ui.label(f"Apiary name: {row[1]}, Location: {row[2]}, Distance: {row[3]}, Date: {row[4]}, Cost: {row[5]}, GPS: {row[6]}")
    result = []
    for row in res:
        #AND CONVERT TO DICT JSON ARRAY#
        data = {}
        for i,col in enumerate(cursor.description):
            data[col[0]] = row[i]
        result.append(data)

       
    print(result) #ok, print to command line 
#CREATE CARD FOR SCREEN
    for x in result:
        with list_alldata:
  #CREATE TABLE
  #
  #look at example Add tables_and_slots in github 
  #looks like many ways 
           
            #Table columns
            columns = [
                  {'name': 'apiary', 'label': 'Apiary', 'field': 'name'},
                  {'name': 'date', 'label': 'Date', 'field': 'age'},
                  {'name': 'notes', 'label': 'Notes', 'field': 'notes'},]
            table = ui.table(columns=columns, rows=result, row_key='name')#result displays Cols only no row data
            
            #ui.table(columns=columns, rows=result[0:2], row_key='name')  # Display first 5 rows
            #ui.table(columns=columns, rows=result, row_key='name')  # Display all row
            #table.add_row(result)
            #table.add_row({'id': time.time(), 'name': new_name.value, 'age': new_age.value}),
            #with ui.table(columns=columns, rows=rows, row_key='name') as table:  
            #with ui.table(columns=columns, rows=result, row_key='name') as table: 
                #table.add_slot('body-cell', r""" 
                #    <q-td :props="props" @click="$parent.$emit('cell_click', props)">
           # {{ props.value }}
        #</q-td>
   # """)        
  #CREATE CARD
           # with ui.card():
            #    with ui.column():
             #       with ui.row().classes("justify-between w-full") as carddata:
                        
            #            ui.label([x['APIARY']])
            #            ui.label([x['DATE']])
            #            ui.label([x['TEXTBOX']])
                        
            #        with ui.row():
            #            #AND CREATE EDIT AND DELETE BUTTONS
             #           ui.button("Edit").on("click", lambda e, carddata=carddata: editdata(carddata))    
                        #DELETE BUTTONS
             #           ui.button("Delete").on("click", lambda e, carddata=carddata: deletebtn(carddata)).classes("bg-red")

#       CALL function when app first open or running
# Does this display all existing data ?  
#getAlldata()


#add get all data button
#ui.button('Get All Todo data', on_click=getAlldata)


#ui.run()
