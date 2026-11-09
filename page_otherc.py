# page_otherc.py
import sqlite3
#import nicegui
from nicegui import ui

#SCript to add new Nucleus 
# June 2026
conn = sqlite3.connect('mydb52023.db')
cursor = conn.cursor()

#SElect a table
#cursor.execute("SELECT * FROM apiary where APIARY_NAME = 'saleen'")
#results = cursor.fetchall()

def addnewdata():
    global hiveNumber
    global nucleusNumber
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
        cursor.execute('''INSERT INTO nucleus (NUC_NO, HIVE_NO, APIARY, DATE, FIVEOR6FMS, CELLS, NEW_APIARY, INSPECT1_DATE, INSPECT1_NOTE, INSPECT2_DATE, INSPECT2_NOTE) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                       (nucleusNumber.value, hiveNumber.value, apiary.value, dateCreated.value, f5or6frames.value, cells.value, newApiary.value, inspectionDate1.value, inspectionNote1.value, inspectionDate2.value, inspectionNote2.value))
        conn.commit()
#show success ADD
        ui.notify(f"success add Nucleus data for Hive{hiveNumber.value}")
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
    



    except Exception as e:
        ui.notify(f"Error adding Nucleus data: {str(e)}")
        conn.rollback()

def content():
        ui.label('Another page content page_ptherc')
        ui.link('Go to main page', '/')
        ui.separator()
        #Display the input nucleus fields
#Fields
        nucleusNumber = ui.input(label = 'Nucleus number :')
        hiveNumber = ui.input(label = 'Hive number :')
        apiary = ui.input(label="Apiary location :").classes("w-full")
        dateCreated = ui.input(label="Date created :").classes("w-full")
        f5or6frames = ui.input(label="Number of frames :").classes("w-full")
        cells = ui.input(label="Number of queen cells:").classes("w-full")
        newApiary = ui.input(label="New apiary  :").classes("w-full")
        inspectionDate1 = ui.input(label="Inspection date 1st:").classes("w-full")
        inspectionNote1 = ui.input(label="Inspection note 1st:").classes("w-full")
        inspectionDate2 = ui.input(label="Inspection date 2 :").classes("w-full")
        inspectionNote2 = ui.input(label="Inspection note 2 :").classes("w-full")
        ui.button('Add Nucleus data', on_click=addnewdata)



# EdIT FUNCTION
def editdata():
    pass

#DELETE FUNCTION
def deletebtn():
    pass
#add Button





