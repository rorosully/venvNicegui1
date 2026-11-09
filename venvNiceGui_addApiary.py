import sqlite3
import nicegui
from nicegui import ui
#june 2026 - Add apiary
# A) Add Apiary
# B) DisplAY ALL Apiary data
conn = sqlite3.connect('mydb52023.db')
cursor = conn.cursor()

#SElect a table
#cursor.execute("SELECT * FROM apiary where APIARY_NAME = 'saleen'")
#results = cursor.fetchall()

#Display the input apiary fields
#Fields

#Do i have to define vars, error "local var 'apiaryName' ref'ed b4 assignment"
#global apiaryName
#global apiaryLocation
#g#lobal apiaryDistance
#global apiaryDate
#global apiaryCost
#global apiaryGPS

#apiaryName = ""
#apiaryLocation = ""
# = ""
##apiaryDate = ""
#apiaryCost = ""
#apiaryGPS = ""

apiaryName = ui.input(label = 'Apiary name :')
apiaryLocation = ui.input(label="Apiary location :").classes("w-full")
apiaryDistance = ui.input(label="Apiary distance :").classes("w-full")
apiaryDate = ui.input(label="Apiary date :").classes("w-full")
apiaryCost = ui.input(label="Apiary cost :").classes("w-full")
apiaryGPS = ui.input(label="Apiary GPS :").classes("w-full")


def addnewdata():
    global apiaryName 
    global apiaryLocation
    global apiaryDistance
    global apiaryDate
    global apiaryCost
    global apiaryGPS

    print(f"apiaryName.value: {apiaryName.value}")
    #apiaryLocation = ui.input(label="Apiary location :").classes("w-full")
    #apiaryDistance = ui.input(label="Apiary distance :").classes("w-full")
    #apiaryDate = ui.input(label="Apiary date :").classes("w-full")
    #apiaryCost = ui.input(label="Apiary cost :").classes("w-full")
    #apiaryGPS = ui.input(label="Apiary GPS :").classes("w-full")
    try:
        cursor.execute('''INSERT INTO apiary (APIARY_NAME, LOCATION, DISTANCE, DATE, COST, GPS) VALUES (?, ?, ?, ?, ?, ?)''', 
                       (apiaryName.value, apiaryLocation.value, apiaryDistance.value, apiaryDate.value, apiaryCost.value, apiaryGPS.value))
        conn.commit()
#show success ADD
        ui.notify(f"success add Apiary data {apiaryName.value}")
        print(f"{apiaryName, apiaryLocation.value}")
         #ui.notify(f"success add Apiary data {apiaryName.value}")
#CLear input fields #input fields not cleared by using following code
        #apiaryName = "" 
        apiaryLocation = ""
        apiaryDistance = ""
        apiaryDate = ""
        apiaryCost = ""
        apiaryGPS = ""
    except Exception as e:
        ui.notify(f"Error adding Apiary data: {str(e)}")
        conn.rollback()


#reDisplay all data from table
def getAlldata():
    cursor.execute("SELECT * FROM apiary")
    results = cursor.fetchall()
    for row in results:
        ui.label(f"Apiary name: {row[1]}, Location: {row[2]}, Distance: {row[3]}, Date: {row[4]}, Cost: {row[5]}, GPS: {row[6]}")


#add Button

ui.button('Add Apiary data', on_click=addnewdata)

#add get all data button
ui.button('Get All Apiary data', on_click=getAlldata)


ui.run()
