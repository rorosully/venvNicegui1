import sqlite3
import nicegui
from nicegui import ui
import header

#COnfig
#import configDB
from configDB import currDB

#SCript to show new Hive 
# June 2026
# A) show hive 
conn = sqlite3.connect(currDB)
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
        cursor.execute('SELECT * FROM hive WHERE HIVE_NO = ?', (hiveNumber.value,))
    
            
        res = cursor.fetchall()
        if len(res) == 0:
                ui.notify(f"No hive found with number {hiveNumber.value}")
        else:
            print(res)
            apiary.value = res[0][1]
            dateCreated.value = res[0][2]
            supers.value = res[0][3]
            swarmed.value = res[0][4]
            numNucsMade.value = res[0][5]
            queenSource.value = res[0][6]

       
#show success  data {hiveNumber.value}")
        print(f"{hiveNumber, hiveNumber.value}")
         #ui.notify(f"success Hive data {hiveNumber.value}")




    except Exception as e:
        ui.notify(f"Error showing Hive data: {str(e)}")
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

    #try add on_change to dateDreated to get updated value
    hiveNumber = ui.input(label = 'Hive number :')
    apiary = ui.input(label="Apiary location :").classes("w-full")
    #dateCreated = ui.input(label="Date created :").classes("w-full")
    dateCreated = ui.date_input(label="Date created :").classes("w-full")
    #supers = ui.input(label="Supers :").classes("w-full").bind_value(globals(), 'supers')
    supers = ui.input(label="Supers :").classes("w-full")
    #supers = ui.input('Supers', validation={'Too long': lambda v: len(v) < 3})
    swarmed = ui.input(label="Swarmed:").classes("w-full")
    numNucsMade = ui.input(label="Number nucs made :").classes("w-full")
    #numNucsMade = ui.input('Number of Nucs Made', validation={'Too long': lambda v: len(v) < 3})
    queenSource = ui.input(label="Queen source:").classes("w-full")
    ui.button('Show Hive data', on_click=addnewdata)
    #Nov '26 add Update button
    ui.button('Update Hive data', on_click=editdata)
    #add get all data button
    ui.button('Get All Hive data', on_click=getAlldata)

    #header.create_header(left_drawer=ui.left_drawer(), title="Hive Entry")
        

    #list all data
    list_alldata = ui.column()

    #create_footer()

# EdIT FUNCTION
def editdata():
    global hiveNumber
    global apiary
    global dateCreated
    global supers
    global swarmed
    global numNucsMade
    global queenSource
    #Update hive record
    #THE new values for ui.input are not updated when changed
    try:
        print(f"apiary.value: {apiary.value}")
        print(f"dateCreated: {dateCreated}")
        print(f"supers.value: {supers.value}")
        #UPDATE statement runs but doesn't update the DB fields
        #cursor.execute('''UPDATE  hive
        #                  SET APIARY = 'apiary.value', DATE_CREATED = 'dateCreated.value', SUPERS = 'supers.value', SWARMED = 'swarmed.value', NUM_NUCS_MADE = 'numNucsMade.value', QUEEN_SOURCE = 'queenSource.value'
        #                 WHERE HIVE_NO = "hiveNumber.value" ''')
        #the following UPDATE statement works,maybe something to do with SQLite3 versions
        cursor.execute('''UPDATE hive
                          SET APIARY = ?, DATE_CREATED = ?, SUPERS = ?, SWARMED = ?,
                          NUM_NUCS_MADE = ?, QUEEN_SOURCE = ?
                          WHERE HIVE_NO = ?''',
                          (apiary.value, dateCreated.value, supers.value, swarmed.value, numNucsMade.value, queenSource.value, hiveNumber.value))
                
        conn.commit()
    
           
    #show success  data {hiveNumber.value}")
        print(f"{hiveNumber, hiveNumber.value}")
        ui.notify(f"success Hive data updated {hiveNumber.value}")
          
    except Exception as e:
        ui.notify(f"Error updating Hive data: {str(e)}")
        conn.rollback()

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
