import sqlite3
import nicegui
from nicegui import ui

#import pywebview

#SCript to add new Hive Inspection 
# June 2026
conn = sqlite3.connect('mydb52023.db')
cursor = conn.cursor()

#try positioning the Labels to make 2 Columns 
#Positioning uses TailWind classes 
# following 2 lines displays on middle of page
#ui.label('Hello Tailwind!') \
 #   .classes('border p-4 absolute top-[50%] left-[50%] translate-x-[-50%] translate-y-[-50%]')

# Use ui.row to display two columns ARG "w-300" is the width overall
# ARG "col-4 border" is the ratio of each column

#Add a header for the page
# this should go into a separate file header.py and be imported into this file
def create_header(left_drawer: ui.left_drawer, title: str) -> None:
    """Creates the application header."""
    with ui.header(elevated=True).classes("items-center justify-between bg-slate-700"):
        with ui.row().classes("items-center"):
            ui.button(on_click=lambda: left_drawer.toggle(), icon="menu").props(
                "flat color=white"
            )
            ui.label(title).classes("text-h5")
#create_header(left_drawer=ui.left_drawer(), title="Add Inspection Data")

with ui.row(wrap=False).classes("w-300"):
    with ui.column().classes("col-4 border"):
        
        hiveNumber = ui.input(label = 'Hive number :').classes("justify-between w-full")
        inspectionNumber = ui.input(label="Inspection number :").classes("text-center")
        queen = ui.input(label="Queen source:").classes("w-full")
        inspectionDate = ui.input(label="Inspection date :").classes("w-[calc(25%-2px)] bg-yellow")
        #swarmed = ui.input(label="Swarmed Y/N :")
    with ui.column().classes("col-4 border"):

        qpl = ui.input(label="QPL, number frames brood :").classes("w-full")
        colour = ui.input(label="Colour:").classes("w-full")
        queenCells = ui.input(label="Queen cells:").classes("w-full")
        disease = ui.input(label="Disease:").classes("w-full")
        supers = ui.input(label="number of Supers:").classes("w-full")
        temper = ui.input(label="Temper:").classes("right:40px;").classes("w-[calc(25%-2px)] bg-yellow")
        steady = ui.input(label="Steady:").classes("w-full").classes("w-[calc(25%-2px)] bg-yellow")
        broodPattern = ui.input(label="Brood pattern:").classes("w-full").classes("w-[calc(25%-2px)] bg-yellow")
        pollen = ui.input(label="Pollen:").classes("w-full").classes("w-[calc(25%-2px)] bg-green")
        combBuilding = ui.input(label="Comb building:").classes("w-full").classes("w-[calc(25%-2px)] bg-yellow")
    with ui.column().classes("col-4 border"):
        notes = ui.textarea(label="Notes:",placeholder='Inspection notes').classes("w-full")

def addnewdata():
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
        cursor.execute('''INSERT INTO inspection 
                       (HIVE_NO, INSPECT_NO, QUEEN, DATE,   QPL, COLOUR, CELLS, DISEASE, SUPERS, TEMPER, STEADY, BROOD_PATTERN, POLLEN, COMB_BUILD, NOTES) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)''', 
                       (hiveNumber.value, inspectionNumber.value, queen.value, inspectionDate.value,  qpl.value, colour.value, queenCells.value, disease.value, supers.value, temper.value, steady.value, broodPattern.value, pollen.value, combBuilding.value,notes.value))
        conn.commit()
#show success ADD
        ui.notify(f"success add Inspection data {hiveNumber.value}")
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

ui.button('Add Inspection data', on_click=addnewdata)

def create_header(left_drawer: ui.left_drawer, title: str) -> None:
    """Creates the application header."""
    with ui.header(elevated=True).classes("items-center justify-between bg-slate-700"):
        with ui.row().classes("items-center"):
            ui.button(on_click=lambda: left_drawer.toggle(), icon="menu").props(
                "flat color=white"
            )
            ui.label(title).classes("text-h5")



#list all data
list_alldata = ui.column()

#reDisplay all data from table
def getAlldata():
    cursor.execute("SELECT * FROM inspection WHERE HIVE_NO = ?", (hiveNumber.value,))
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
                        ui.label([x['INSPECT_NO']])
                        ui.label([x['QUEEN']])
                        ui.label([x['DATE']])
                        ui.label([x['QPL']])
                        ui.label([x['COLOUR']])
                        #ui.label([x['CELLS']])
                        #ui.label([x['DISEASE']])
                        #ui.label([x['SUPERS']])
                        #ui.label([x['SWARMED']])
                        #ui.label([x['NUM_NUCS_MADE']])
                        #ui.label([x['QUEEN_SOURCE']])
                    with ui.row():
                        #AND CREATE EDIT AND DELETE BUTTONS
                        ui.button("Edit").on("click", lambda e, carddata=carddata: editdata(carddata))    
                        #DELETE BUTTONS
                        ui.button("Delete").on("click", lambda e, carddata=carddata: deletebtn(carddata)).classes("bg-red")

#       CALL function when app first open or running
# Does this display all existing data ?  
#getAlldata()


#add get all data button
ui.button('Get all Inspection data for this hive', on_click=getAlldata)


ui.run()
