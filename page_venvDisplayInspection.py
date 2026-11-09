# page_venvDisplayInspection.py
import sqlite3
import nicegui
from nicegui import ui

#import pywebview

#SCript to display/update  Hive Inspection 
# June 2026
conn = sqlite3.connect('mydb52023.db')
cursor = conn.cursor()

#SElect a table
#cursor.execute("SELECT * FROM apiary where APIARY_NAME = 'saleen'")
#results = cursor.fetchall()

#Display the input apiary fields
#Fields
#try positioning the Labels to make 2 Columns 
#Positioning uses TailWind classes 
# following 2 lines displays on middle of page
#ui.label('Hello Tailwind!') \
 #   .classes('border p-4 absolute top-[50%] left-[50%] translate-x-[-50%] translate-y-[-50%]')

# Use ui.row to display two columns ARG "w-300" is the width overall
# ARG "col-4 border" is the ratio of each column

ui.link('Back to Main page', '/')

def content():
    with ui.row(wrap=False).classes("w-300"):
        with ui.column().classes("col-4 border"):
            
            hiveNumber = ui.input(label = 'Hive number :').classes("justify-between w-full")
            inspectionNumber = ui.input(label="Inspection number :").classes("text-center")
            queen = ui.input(label="Queen :").classes("w-full")
            inspectionDate = ui.input(label="Inspection date :").classes("w-[calc(25%-2px)] bg-yellow")
            #swarmed = ui.input(label="Swarmed Y/N :")
        with ui.column().classes("col-4 border"):

            qpl = ui.input(label="QPL number brood frames :").classes("w-full")
            colour = ui.input(label="Colour:").classes("w-full")
            queenCells = ui.input(label="Queen cells:").classes("w-full")
            disease = ui.input(label="Disease:").classes("w-full")
            supers = ui.input(label="number ofSupers:").classes("w-full")
            temper = ui.input(label="Temper:").classes("right:40px;")
            steady = ui.input(label="Steady:").classes("w-full")
            broodPattern = ui.input(label="Brood pattern:").classes("w-full")
            pollen = ui.input(label="Pollen:").classes("w-full")
            combBuilding = ui.input(label="Comb building:").classes("w-full")
            notes = ui.input(label="Notes:").classes("w-full")

#Display Inspection data 


def displayData():
    global hiveNumber
    global inspectionNumber
    global queen
    global inspectionDate
    #global swarmed
    global qpl
    global colour
    global queenCells
    global disease
    global supers
    global temper
    global steady
    global broodPattern
    global pollen
    global combBuilding
    global notes
  
    try:
                         
        cursor.execute('''SELECT * FROM inspection where HIVE_NO = ? AND INSPECT_NO = ?''', (hiveNumber.value, inspectionNumber.value))
    #show success ADD
        
        print(f"{hiveNumber, hiveNumber.value}")
         #ui.notify(f"successNumberd Apiary data {apiaryName.value}")

        rows = cursor.fetchall()
        if rows:
            for row in rows:

                queen.value = row[2]
                inspectionDate.value = row[3]
                qpl.value = row[4]
                colour.value = row[5]
                queenCells.value = row[6]
                disease.value = row[7]
                supers.value = row[8]
                temper.value = row[9]
                steady.value = row[10]
                broodPattern.value = row[11]
                pollen.value = row[12]
                combBuilding.value = row[13]
                notes.value = row[14]
                
                ui.notify(f"success  display Inspection data {hiveNumber.value}")
                #ui.label(f"Hive number: {row[0]}, Apiary: {row[1]}, Date created: {row[2]}, Supers: {row[3]}, Swarmed: {row[4]}, Number nucs made: {row[5]}, Queen source: {row[6]}")
        else:
            ui.notify(f"No data found for Hive number {hiveNumber.value}")
    except Exception as e:
        ui.notify(f"Error displaying Inspection data: {str(e)}")
        conn.rollback()

def updateData():
    global hiveNumber
    global inspectionNumber
    global queen
    global inspectionDate
    #global swarmed
    global qpl
    global colour
    global queenCells
    global disease
    global supers
    global temper
    global steady
    global broodPattern
    global pollen
    global combBuilding
    global notes
    
    try:

        cursor.execute('''UPDATE  inspection 
                       SET QUEEN = ?, DATE = ?, QPL = ?, COLOUR = ?, CELLS = ?, DISEASE = ?, SUPERS = ?, TEMPER = ?, STEADY = ?, BROOD_PATTERN = ?, POLLEN = ?, COMB_BUILD = ? , NOTES = ?
                       WHERE HIVE_NO = ? AND INSPECT_NO = ?''', 
                       (queen.value, inspectionDate.value, qpl.value, colour.value, queenCells.value, disease.value, supers.value, temper.value, steady.value, broodPattern.value, pollen.value, combBuilding.value, notes.value, hiveNumber.value, inspectionNumber.value))
        conn.commit()
#show success ADD
        ui.notify(f"success update Inspection data {hiveNumber.value}")
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
       # get_Alldata()



    except Exception as e:
        ui.notify(f"Error adding Inspection data: {str(e)}")
        conn.rollback()

# EdIT FUNCTION
def editdata():
    pass

#DELETE FUNCTION
def deletebtn():
    pass
#add Button

ui.button('Display Inspection data', on_click=displayData)

ui.button('Update Inspection data', on_click=updateData)




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



