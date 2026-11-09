import sqlite3
import nicegui
from nicegui import ui

#SCript to display Todo data / add function to UPDATE data
# Use a dropdown to select the apiary for todo display
# Options
# a) 'DIsplay Todo Data for APiary - latest entry
# b) 'UPdate Todo Data for latest entry
# c) 'Display all todo data for apiary

conn = sqlite3.connect('mydb52023.db')
cursor = conn.cursor()

#try to get a colour value in "select" to make it stand out
select = ui.select(label='Select Apiary from Dropdown', options=[], value=None).classes("w-80").props("color=green")
blankline = ui.label("") # is this the way to space out the form ?
apiary = ui.input(label="Apiary location :")
date = ui.input(label="Date created :")
textbox = ui.input(label="Todo :").classes("w-full")

def displayData():
    
    global apiary
    global date
    global textbox
        
    try:
        cursor.execute('''SELECT * FROM todo where APIARY = ?''', (select.value,))
        conn.commit()
#show success ADD
        
        print(f"{apiary.value}")
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                apiary.value = row[0]
                date.value = row[1]
                textbox.value = row[2]
                ui.notify(f"success  display todo data {apiary.value}")
                
        else:
            ui.notify(f"No data found for apiary number {apiary.value}")
    except Exception as e:
        ui.notify(f"Error displaying apiary data: {str(e)}")
        conn.rollback()

def displayDropdownData():
    #NOt used: 'Select' type worked for Dropdown values
    global apiary
    global date
    global textbox
    global select
    #select = ui.select(label='Select Select Apiary', options=[], value=None).classes("w-60")
    #with ui.dropdown_button('Select Ddown Apiary', icon='menu') as dropdown:    
    try: 
             cursor.execute('''SELECT * FROM apiary ''')
             conn.commit()
#show success 
        
             print(f"{apiary.value}")
             rows = cursor.fetchall()
             if rows:
              for row in rows:
                print(f"Apiary {row[0]}")
                select.options.append(row[0])
                select.update()
                #dropdown.add
                #dropdown.add(row[0])
                
                
             else:
                ui.notify(f"No data found for apiary number {apiary.value}")
    except Exception as e:
                ui.notify(f"Error displaying apiary data: {str(e)}")
    conn.rollback()

#UPDATE function
def updateData():
    
    global apiary
    global date
    global textbox
        
    try:
        cursor.execute('''UPDATE todo SET DATE = ?, TEXTBOX = ? WHERE APIARY = ?''',
                      (date.value, textbox.value, apiary.value))
        conn.commit()
#show success 
        ui.notify(f"success update todo data {apiary.value}")
        #print(f"{hiveNumber, hiveNumber.value}")
         #ui.notify(f"successNumberd Apiary data {apiaryName.value}")

    except Exception as e:
        ui.notify(f"Error updating apiary data: {str(e)}")
        conn.rollback()

# EdIT FUNCTION
def editdata():
    pass

#DELETE FUNCTION
def deletebtn():
    pass
#add Button

ui.button('Display Todo data for selected Apiary', on_click=displayData)

#ui.button('Display dropdown data', on_click=displayDropdownData)
#UPDATE
ui.button('Update Todo data', on_click=updateData)


#
#populate Dropdown with apiary names
displayDropdownData()

#list all data
list_alldata = ui.column()

#reDisplay all data from table
def getAlldata():
    cursor.execute('''SELECT * FROM todo where APIARY = ?''', (select.value,))
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
  #CREATE CARD
            with ui.card():
                with ui.column():
                    with ui.row().classes("justify-between w-full") as carddata:
                        ui.label([x['APIARY']])
                        ui.label([x['DATE']])
                        ui.label([x['TEXTBOX']])
                        
                    #with ui.row():
                     #   #AND CREATE EDIT AND DELETE BUTTONS
                     #   ui.button("Edit").on("click", lambda e, carddata=carddata: editdata(carddata))    
                     #   #DELETE BUTTONS
                     #   ui.button("Delete").on("click", lambda e, carddata=carddata: deletebtn(carddata)).classes("bg-red")

#       CALL function when app first open or running
# Does this display all existing data ?  
#getAlldata()


#add get all data button
ui.button('Get All Todo data for selected apiary', on_click=getAlldata)


#ui.run(native=True) #need to install pywebview to r
#un asnative
ui.run()