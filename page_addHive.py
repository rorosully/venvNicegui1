import sqlite3
import nicegui
from nicegui import ui
import header

#SCript to add new Hive 
# June 2026
# A) Add hive 
# Nov '26 add Client-side validation fo input
conn = sqlite3.connect('mydb52023.db')
cursor = conn.cursor()

#SElect a table
#cursor.execute("SELECT * FROM apiary where APIARY_NAME = 'saleen'")
#results = cursor.fetchall()

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
        print(f"apiaryName.value: {hiveNumber.value}, apiary.value: {apiary.value}, dateCreated.value: {dateCreated.value}, supers.value: {supers.value}, swarmed.value: {swarmed.value}, numNucsMade.value: {numNucsMade.value}, queenSource.value: {queenSource.value}")
        cursor.execute('''INSERT INTO hive 
                       (HIVE_NO, APIARY, DATE_CREATED, SUPERS, SWARMED, NUM_NUCS_MADE, QUEEN_SOURCE) VALUES (?, ?, ?, ?, ?, ?, ?)''', 
                       (hiveNumber.value, apiary.value, dateCreated.value, supers.value, swarmed.value, numNucsMade.value, queenSource.value))
        conn.commit()
#show success ADD
        ui.notify(f"success add a Hive data {hiveNumber.value}")
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
        #get_Alldata()



    except Exception as e:
        ui.notify(f"Error adding Hive data: {str(e)}")
        conn.rollback()

#Display the input apiary fields
#Fields
def content():
    #Aug 26 causes an issue calling CreateHdr here"
    #header.create_header(left_drawer=ui.left_drawer(), title="Hive Entry")
    
    
    global hiveNumber
    global apiary
    global dateCreated
    global supers
    global swarmed
    global numNucsMade
    global queenSource
    
    #hiveNumber = ui.input(label = 'Hive number :')
    #hiveNumber = ui.input(label = 'Hive number :', validation={'Hive number is required': lambda v: len(v) >= 1})
    hiveNumber = ui.input('Hive number :', validation={'Hive number is required': lambda v: len(v) >= 1})
    apiary = ui.input(label="Apiary location :").classes("w-full")
   #dateCreated = ui.input(label="Date created :").classes("w-full")
    dateCreated = ui.date_input(label="Date created :").classes("w-full")
    #on_change=lambda e: dateCreated.set_text('you typed: ' + e.value),
    #supers = ui.input(label="Supers :").classes("w-full"),validation={'Input too long': lambda value: len(value) < 3}
    #supers = ui.input('name', validation={'Too long': lambda v: len(v) < 3}).without_auto_validation()
    supers = ui.input('Supers', validation={'Too long': lambda v: len(v) < 3})

    swarmed = ui.input(label="Swarmed:").classes("w-full")
    #numNucsMade = ui.input(label="Number nucs made :").classes("w-full")
    numNucsMade = ui.input('Number of Nucs Made', validation={'Too long': lambda v: len(v) < 3})
    
    queenSource = ui.input(label="Queen source:").classes("w-full")
    ui.button('Add Hive data', on_click=addnewdata)
    #add get all data button
    ui.button('Get All Hive data', on_click=getAlldata)

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
    cursor.execute("SELECT * FROM hive")
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


#add get all data button
#ui.button('Get All Hive data', on_click=getAlldata)


#ui.run()
