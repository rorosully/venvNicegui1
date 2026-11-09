import sqlite3
import nicegui
from nicegui import ui
import header

#SCript to add new TReatment
# Aug 2026
# A) Add treatment 
conn = sqlite3.connect('mydb52023.db')
cursor = conn.cursor()

#create Footer
def create_footer() -> None:
    """Creates the application footer."""
    with ui.footer(elevated=True).classes(
        "bg-slate-700 text-white items-center justify-center p-4"
    ):
        ui.label("© 2025 MyApp Name. All rights reserved.")


#Move addNewData b4 content()
# Does it need to be moved, mayb its just adding global values required to work?
def addnewdata():
    global medicineName
    global apiary
    global dateAdministration
    global qtyGiven
    global hiveTreated
    global withdrawalPeriod
    global treatmentNote
    

    #print(f"apiaryName.value: {apiaryName.value}")
    #apiaryLocation = ui.input(label="Apiary location :").classes("w-full")
    #apiaryDistance = ui.input(label="Apiary distance :").classes("w-full")
    #apiaryDate = ui.input(label="Apiary date :").classes("w-full")
    #apiaryCost = ui.input(label="Apiary cost :").classes("w-full")
    #apiaryGPS = ui.input(label="Apiary GPS :").classes("w-full")
    try:
        cursor.execute('''INSERT INTO treatment 
                       (MEDICINE_NAME, APIARY, DATE_ADMINISTRATION, QTY_GIVEN, HIVE_TREATED, WITHDRAWAL_PERIOD, TREATMENT_NOTE) VALUES (?, ?, ?, ?, ?, ?, ?)''',
                       (medicineName.value, apiary.value, dateAdministration.value, qtyGiven.value, hiveTreated.value, withdrawalPeriod.value, treatmentNote.value))
        conn.commit()
#show success ADD
        ui.notify(f"success add a treatment data {medicineName.value}")
        print(f"{medicineName.value}")
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
        ui.notify(f"Error adding Treatment data: {str(e)}")
        conn.rollback()

#Display the input apiary fields
#Fields
def content():
    #Aug 26 causes an issue calling CreateHdr here"
    #header.create_header(left_drawer=ui.left_drawer(), title="Hive Entry")
    
    
    global medicineName
    global apiary
    global dateAdministration
    global qtyGiven
    global hiveTreated
    global withdrawalPeriod
    global treatmentNote
    
    medicineName = ui.input(label = 'Medicine name :')
    apiary = ui.input(label="Apiary location :").classes("w-full")
   
    dateAdministration = ui.date_input(label="Date administration :").classes("w-full")
    qtyGiven = ui.input(label="Quantity given :").classes("w-full")
    hiveTreated = ui.input(label="Hive treated :").classes("w-full")
    withdrawalPeriod = ui.input(label="Withdrawal period :").classes("w-full")
    treatmentNote = ui.input(label="Treatment note :").classes("w-full")
    
    ui.button('Add Treatment data', on_click=addnewdata)
    #add get all data button
    ui.button('Get All Treatment data', on_click=getAlldata)

    #header.create_header(left_drawer=ui.left_drawer(), title="Hive Entry")
        

    #list all data
    list_alldata = ui.column()

    #create_footer()

# EdIT FUNCTION
def editdata():
    pass

#DELETE FUNCTION
def deletebtn():
    pass
#add Button






#list all data
#list_alldata = ui.column()

#reDisplay all data from table 'hive'
def getAlldata():
    #Does list_alldata ned to be global?
    global list_alldata
    list_alldata = ui.column()
    cursor.execute("SELECT * FROM treatment")
    res = cursor.fetchall()
    #for row in results:
    #    ui.label(f"Apiary name: {row[1]}, Location: {row[2]}, Distance: {row[3]}, Date: {row[4]}, Cost: {row[5]}, GPS: {row[6]}")
    result = []
    for row in res:
       data = {}
       for i,col in enumerate(cursor.description):
            data[col[0]] = row[i]
       result.append(data)

 #      
    print(result) #ok, print to command line 

#getAlldata()
#CREATE CARD FOR SCREEN
    for x in result:
        with list_alldata:
  #CREATE CARD
            with ui.card():
                with ui.column():
                    with ui.row().classes("justify-between w-full") as carddata:
                        ui.label([x['MEDICINE_NAME']])
                        ui.label([x['APIARY']])
                        ui.label([x['DATE_ADMINISTRATION']])
                        ui.label([x['QTY_GIVEN']])
                        ui.label([x['HIVE_TREATED']])
                        ui.label([x['WITHDRAWAL_PERIOD']])
                        ui.label([x['TREATMENT_NOTE']])
                    with ui.row():
                        #AND CREATE EDIT AND DELETE BUTTONS
                        ui.button("Edit").on("click", lambda e, carddata=carddata: editdata(carddata))    
                        #DELETE BUTTONS
                        ui.button("Delete").on("click", lambda e, carddata=carddata: deletebtn(carddata)).classes("bg-red")


#add get all data button
#ui.button('Get All Hive data', on_click=getAlldata)


#ui.run()
