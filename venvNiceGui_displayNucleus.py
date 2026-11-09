import sqlite3
import nicegui
from nicegui import ui

#SCript to display Nucleus data / add function to UPDATE data
# June 2026
conn = sqlite3.connect('mydb52023.db')
cursor = conn.cursor()

#Display the input nucleus fields
#Fields
nucleusNumber = ui.input(label = 'Nucleus number :')
hiveNumber = ui.input(label = 'Hive number :')
apiary = ui.input(label="Apiary location :")
dateCreated = ui.input(label="Date created :")
f5or6frames = ui.input(label="Number of frames :").classes("w-full")
cells = ui.input(label="Number of queen cells:").classes("w-full")
newApiary = ui.input(label="New apiary  :").classes("w-full")
inspectionDate1 = ui.input(label="Inspection date 1st:").classes("w-full")
inspectionNote1 = ui.input(label="Inspection note 1st:").classes("w-full")
inspectionDate2 = ui.input(label="Inspection date 2 :").classes("w-full")
inspectionNote2 = ui.input(label="Inspection note 2 :").classes("w-full")

def displayData():
    global nucleusNumber
    global hiveNumber
    global apiary
    global dateCreated
    global f5or6frames
    global cells
    global newApiary
    global inspectionDate1
    global inspectionNote1
    global inspectionDate2
    global inspectionNote2
       

    
    try:
        #cursor.execute('''INSERT INTO hive 
        #               (HIVE_NO, APIARY, DATE_CREATED, SUPERS, SWARMED, NUM_NUCS_MADE, QUEEN_SOURCE) VALUES (?, ?, ?, ?, ?, ?, ?)''', 
        #               (hiveNumber.value, apiary.value, dateCreated.value, supers.value, swarmed.value, numNucsMade.value, queenSource.value))
        cursor.execute('''SELECT * FROM nucleus where HIVE_NO = ? AND NUC_NO = ?''', (hiveNumber.value, nucleusNumber.value))
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
                hiveNumber.value = row[1]
                apiary.value = row[2]
                dateCreated.value = row[3]
                f5or6frames.value = row[4]
                cells.value = row[5]
                newApiary.value = row[6]
                inspectionDate1.value = row[7]
                inspectionNote1.value = row[8]
                inspectionDate2.value = row[9]
                inspectionNote2.value = row[10]
                ui.notify(f"success  display Nucleus data {hiveNumber.value}")
                #ui.label(f"Hive number: {row[0]}, Apiary: {row[1]}, Date created: {row[2]}, Supers: {row[3]}, Swarmed: {row[4]}, Number nucs made: {row[5]}, Queen source: {row[6]}")
        else:
            ui.notify(f"No data found for Nucleus number {nucleusNumber.value}")
    except Exception as e:
        ui.notify(f"Error displaying HiNucleusve data: {str(e)}")
        conn.rollback()

#UPDATE function
def updateData():
    global nucleusNumber
    global hiveNumber
    global apiary
    global dateCreated
    global f5or6frames
    global cells
    global newApiary
    global inspectionDate1
    global inspectionNote1
    global inspectionDate2
    global inspectionNote2

    #print(f"apiaryName.value: {apiaryName.value}")
    #apiaryLocation = ui.input(label="Apiary location :").classes("w-full")
    #apiaryDistance = ui.input(label="Apiary distance :").classes("w-full")
    #apiaryDate = ui.input(label="Apiary date :").classes("w-full")
    #apiaryCost = ui.input(label="Apiary cost :").classes("w-full")
    #apiaryGPS = ui.input(label="Apiary GPS :").classes("w-full")
    try:
        cursor.execute('''UPDATE nucleus SET APIARY = ?, DATE = ?, FIVEOR6FMS = ?, CELLS = ? , NEW_APIARY = ?, INSPECT1_DATE = ?, INSPECT1_NOTE = ?, INSPECT2_DATE = ?, INSPECT2_NOTE = ? WHERE HIVE_NO = ? AND NUC_NO = ?''',
                      (apiary.value, dateCreated.value, f5or6frames.value, cells.value, newApiary.value, inspectionDate1.value, inspectionNote1.value, inspectionDate2.value, inspectionNote2.value, hiveNumber.value, nucleusNumber.value))
        conn.commit()
        ui.notify(f"success update Nucleus data {nucleusNumber.value}")
        print(f"{nucleusNumber}, {nucleusNumber.value}")
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
        ui.notify(f"Error updating Nucleus data: {str(e)}")
        conn.rollback()

# EdIT FUNCTION
def editdata():
    pass

#DELETE FUNCTION
def deletebtn():
    pass
#add Button

with ui.row():
    ui.button('Display Nucleus data', on_click=displayData)

#UPDATE
    ui.button('Update Nucleus data', on_click=updateData)





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