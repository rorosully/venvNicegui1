import sqlite3

#AUG 26 Import this file for your DB
global conn
global cursor
global currDB
currDB = 'mydb52023.db'  # Set the current database name

#Aug 26 try putting DB conn in config but it gives an issue 
#for now just pass currDB value to the connection
#conn = sqlite3.connect('mydb52023.db')
#cursor = conn.cursor()