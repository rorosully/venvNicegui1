# page_main.py
from nicegui import ui
from random import random
from state import traces, plot_update

def content():
    ui.label('Main Menu')
    #ui.link('Go to Add New Apiary', '/other')
    #.link('Go to Add New Hive', '/other2')
    #ui.link('Go to Add New Inspection', '/other3')
    #ui.link('Go to Add New Todo', '/other4')
    #ui.separator()
    #try use a Dropdown to select a page to go to

    with ui.dropdown_button('Open Hive options!', auto_close=True):
         ui.link('Go to Add New Hive', '/other2')
         ui.separator()
         ui.link('Go to Show + Update Hive details','/other11')
         ui.separator()
         ui.link('Go to Show All your Hive details','/other14')
    ui.separator()
    with ui.dropdown_button('Open Apiary options!', auto_close=True):
        ui.link('Go to Add Apiary', '/other')
        ui.separator()
    with ui.dropdown_button('Open Inspection options!', auto_close=True):
        ui.link('Go to Add Inspection', '/other3')
        ui.separator() 
        ui.link('Go to Show Inspection details', '/other13')
        ui.separator()
    with ui.dropdown_button('Open Nucleus options!', auto_close=True):
        ui.link('Go to Add Nucleus', '/other5')
        ui.separator()
    with ui.dropdown_button('Open Todo options!', auto_close=True):
         ui.link('Go to Add Todo', '/other4')
         ui.separator()
         #ui.separator()
         ui.link('Go to Show Todo details','/other12')
    with ui.dropdown_button('Open Treatment options!', auto_close=True):
         ui.link('Go to Add Treatment', '/other6')
         ui.separator()
         ui.link('Go to Show Treatment details', '/other15')
    with ui.dropdown_button('Export data', auto_close=True):
                  ui.link('Go to Export data', '/other17')
    with ui.dropdown_button('Import files', auto_close=True):
                    #redo for csv   ui.link('Go to Import Files', '/other16')
                  ui.link('Go to Import Files', '/other18') 

    def add_trace():
        data = {'x': [1, 2, 3], 'y': [random(), random(), random()]}
        traces.append(data)
        plot_update.emit()

    ui.button('Add trace', on_click=add_trace)