import sqlite3
import nicegui
from nicegui import ui

#SCript to display Hive data / add function to UPDATE data
# a) display Hive
# b) Update hive detail
# June 2026
# 
conn = sqlite3.connect('mydb52023.db')
cursor = conn.cursor()

#SElect a table
#cursor.execute("SELECT * FROM apiary where APIARY_NAME = 'saleen'")
#results = cursor.fetchall()

#Display the input apiary fields
#Fields

hiveNumber = ui.input(label = 'Hive number :').classes("colour=green")
apiary = ui.input(label="Apiary location :").classes("w-full")
dateCreated = ui.input(label="Date created :").classes("w-full")
supers = ui.input(label="Supers :").classes("w-full")
swarmed = ui.input(label="Swarmed:").classes("w-full")
numNucsMade = ui.input(label="Number nucs made :").classes("w-full")
queenSource = ui.input(label="Queen source:").classes("w-full")

def displayData():
    global hiveNumber
    global apiary
    global dateCreated
    global supers
    global swarmed
    global numNucsMade
    global queenSource

    #print(f"apiaryName.value: {apiaryName.value}")
    #apiaryLocation = ui.input(label="Apiary location :").classes("w-full")
    #apiaryDistance = ui.input(label="Apiary distance :").classes("w-full")
    #apiaryDate = ui.input(label="Apiary date :").classes("w-full")
    #apiaryCost = ui.input(label="Apiary cost :").classes("w-full")
    #apiaryGPS = ui.input(label="Apiary GPS :").classes("w-full")
    try:
        #cursor.execute('''INSERT INTO hive 
        #               (HIVE_NO, APIARY, DATE_CREATED, SUPERS, SWARMED, NUM_NUCS_MADE, QUEEN_SOURCE) VALUES (?, ?, ?, ?, ?, ?, ?)''', 
        #               (hiveNumber.value, apiary.value, dateCreated.value, supers.value, swarmed.value, numNucsMade.value, queenSource.value))
        cursor.execute('''SELECT * FROM hive where HIVE_NO = ?''', (hiveNumber.value,))
        conn.commit()
#show success ADD
        
        print(f"{hiveNumber, hiveNumber.value}")
         #ui.notify(f"successNumberd Apiary data {apiaryName.value}")
#CLear input fields #input fields not cleared byusing following code
        #apiaryName = hive.APIARY 
        #apiaryLocation = ""
        #apiaryDistance = ""
        #apiaryDate = ""
        #apiaryCost = ""
        #apiaryGPS = ""
        #list_alldata
        #  clear() #X 'import from turtle'
        #get_Alldata()
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                apiary.value = row[1]
                dateCreated.value = row[2]
                supers.value = row[3]
                swarmed.value = row[4]
                numNucsMade.value = row[5]
                queenSource.value = row[6]
                ui.notify(f"success  display Hive data {hiveNumber.value}")
                #ui.label(f"Hive number: {row[0]}, Apiary: {row[1]}, Date created: {row[2]}, Supers: {row[3]}, Swarmed: {row[4]}, Number nucs made: {row[5]}, Queen source: {row[6]}")
        else:
            ui.notify(f"No data found for Hive number {hiveNumber.value}")
    except Exception as e:
        ui.notify(f"Error displaying Hive data: {str(e)}")
        conn.rollback()

#UPDATE function
def updateData():
    global hiveNumber
    global apiary
    global dateCreated
    global supers
    global swarmed
    global numNucsMade
    global queenSource

    #print(f"apiaryName.value: {apiaryName.value}")
    #apiaryLocation = ui.input(label="Apiary location :").classes("w-full")
    #apiaryDistance = ui.input(label="Apiary distance :").classes("w-full")
    #apiaryDate = ui.input(label="Apiary date :").classes("w-full")
    #apiaryCost = ui.input(label="Apiary cost :").classes("w-full")
    #apiaryGPS = ui.input(label="Apiary GPS :").classes("w-full")
    try:
        cursor.execute('''UPDATE hive SET APIARY = ?, DATE_CREATED = ?, SUPERS = ?, SWARMED = ?, NUM_NUCS_MADE = ?, QUEEN_SOURCE = ? WHERE HIVE_NO = ?''',
                      ( apiary.value, dateCreated.value, supers.value, swarmed.value, numNucsMade.value, queenSource.value, hiveNumber.value))
        conn.commit()
#show success ADD
        ui.notify(f"success update Hive data {hiveNumber.value}")
        print(f"{hiveNumber, hiveNumber.value}")
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
        #get_Alldata()# copied from addhive for EDIT/DELETE



    except Exception as e:
        ui.notify(f"Error updating Hive data: {str(e)}")
        conn.rollback()

# EdIT FUNCTION
def editdata():
    pass

#DELETE FUNCTION
def deletebtn():
    pass
#add Button

ui.button('Display Hive data', on_click=displayData)

#UPDATE
ui.button('Update Hive data', on_click=updateData)





#list all data
list_alldata = ui.column()

#reDisplay all data from table
def getAlldata():
    cursor.execute("SELECT * FROM hive")
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
                        ui.label([x['HIVE_NO']])
                        ui.label([x['APIARY']])
                        ui.label([x['DATE_CREATED']])
                        ui.label([x['SUPERS']])
                        ui.label([x['SWARMED']])
                        ui.label([x['NUM_NUCS_MADE']])
                        ui.label([x['QUEEN_SOURCE']])
                    with ui.row():
                        #AND CREATE EDIT AND DELETE BUTTONS
                        ui.button("Edit").on("click", lambda e, carddata=carddata: editdata(carddata))    
                        #DELETE BUTTONS
                        ui.button("Delete").on("click", lambda e, carddata=carddata: deletebtn(carddata)).classes("bg-red")

#       CALL function when app first open or running
# Does this display all existing data ?  
getAlldata()


#add get all data button
ui.button('Get All Hive data', on_click=getAlldata)


#ui.run(native=True) #need to install pywebview to r
#un asnative
ui.run()