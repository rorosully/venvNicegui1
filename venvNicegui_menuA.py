#!/usr/bin/env python3

#import os
#import sys
#import os.path

import sqlite3
import nicegui
from nicegui import ui

#extra imports from Zuaberzerg ex
import asyncio
import platform
import shlex

# what does subprocess do?
#import subprocess

# Menu for control
#July 2026 



with ui.row(wrap=False).classes("w-300"):
    with ui.column().classes("col-4 border"):
        
        hiveNumber = ui.input(label = 'Hive number :').classes("justify-between w-full")
        #ui.button('python3 hello.py', on_click=lambda: run_command('python3 hello.py')).props('no-caps')
        #swarmed = ui.input(label="Swarmed Y/N :")
        ##on_click=lambda: ('python3 hello.py')).props('no-caps')
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





        #displayHiveButton = ui.button(label = 'Display Hives').classes("justify-between w-full").on_click(displayHives)


def displayHives():
    #os.system('python3 venvNicegui_displayHive.py')
    #following line from niceGui github
   # #ui.button('python3 hello.py', on_click=lambda: run_command('python3 hello.py')).props('no-caps')
    qpl = ui.input(label="QPL number brood frames :").classes("w-full")
    #subprocess.run([sys.executable,'venvNicegui_addHive.py'])
    
def addHive():
    qpl = ui.input(label="QPL number brood frames :").classes("w-full")
    #subprocess.run([sys.executable,'venvNicegui_addHive.py'])
   