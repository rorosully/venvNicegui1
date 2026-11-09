import sqlite3
import nicegui
from nicegui import ui

#SCript to add new Todo 
# June 2026
conn = sqlite3.connect('mydb52023.db')
cursor = conn.cursor()

#SElect a table
#cursor.execute("SELECT * FROM apiary where APIARY_NAME = 'saleen'")
#results = cursor.fetchall()

#Display the input apiary fields
#Fields

def content():
    global apiary
    global dateCreated
    global textbox
    apiary = ui.input(label="Apiary name :").classes("w-full")
    #dateCreated = ui.input(label="Date created :").classes("w-full")
    dateCreated = ui.date_input(label="Date created :").classes("w-full")
    dateCreated.picker.props('mask="DD-MM-YYYY"')
    textbox = ui.textarea(label="Notes :").classes("w-full")

    #try this
    

    #ui.input_chips('My favorite chips', value=['Pringles', 'Doritos', "Lay's"])



    #add Button

    ui.button('Add Todo data', on_click=addnewdata)

    #add get all data button
    ui.button('Get all Todo data for this Apiary', on_click=getAlldata)
            #list all data
            
    #list_alldata = ui.column()

def addnewdata():
    
    global apiary
    global dateCreated
    global textbox
    
    try:
        cursor.execute('''INSERT INTO todo ( APIARY, DATE, TEXTBOX ) VALUES (?, ?, ?)''', 
                       (apiary.value, dateCreated.value, textbox.value))
        conn.commit()
#show success ADD
        ui.notify(f"success add todo data {apiary.value}")
        
         #ui.notify(f"successNumberd Apiary data {apiaryName.value}")
#CLear input fields #input fields not cleared byusing following code
        #apiaryName = "" 
        apiaryLocation = ""
        apiaryDistance = ""
        apiaryDate = ""
        apiaryCost = ""
        apiaryGPS = ""
        #list_alldata
        #  clear() #X 'import from turtle'
        #get_Alldata()



    except Exception as e:
        ui.notify(f"Error adding Todo data: {str(e)}")
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

#reDisplay all data from table
def getAlldata():

    global list_alldata
    list_alldata = ui.column()
        
    cursor.execute("SELECT * FROM todo WHERE APIARY = ?", (apiary.value,))
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
                        
                    with ui.row():
                        #AND CREATE EDIT AND DELETE BUTTONS
                        ui.button("Edit").on("click", lambda e, carddata=carddata: editdata(carddata))    
                        #DELETE BUTTONS
                        ui.button("Delete").on("click", lambda e, carddata=carddata: deletebtn(carddata)).classes("bg-red")

#       CALL function when app first open or running
# Does this display all existing data ?  
#getAlldata()


#add get all data button
#ui.button('Get All Todo data', on_click=getAlldata)


#ui.run()
