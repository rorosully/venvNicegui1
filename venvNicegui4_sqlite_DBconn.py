import sqlite3
import nicegui
from nicegui import ui

conn = sqlite3.connect('mydb52023.db')
cursor = conn.cursor()

#SElect a table
cursor.execute("SELECT * FROM apiary where APIARY_NAME = 'saleen'")
results = cursor.fetchall()

#Display the apiary for 1 row
#Fields

ui.label('Apiary name :' + str(results[0][1]))
ui.label('Apiary location :' +str(results[0][2]))
ui.label('Apiary distance :' +str(results[0][3]))
ui.label('Apiary date :' +str(results[0][4]))
ui.label('Apiary cost : ' +str(results[0][5]))
ui.label('Apiary GPS :' +str(results[0][5]))

ui.run()
