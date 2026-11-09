# main.py
from nicegui import ui
import page_main
import page_addApiary
import page_addHive
import page_addInspection
import page_addtodo
import page_addNucleus
import page_addTreatment

#Display pages
import page_displayHive
import page_displayTodo_Table_2
#import page_DisplayTodo3
import page_displayInspection
import page_DisplayAllHives
import page_displayAllTreatments
#import page_uploadImage
#import page_uploadTextfileexample
import page_exportData1
import page_importData1

import header
from state import traces, plot_update

#Does a sub page need to be called "page_nnn"? NO 
#import page_venvDisplayInspection
# I don't have an '/other' dir. Why is it working ? 

def root():
    header.create_header(left_drawer=ui.left_drawer(), title="Main Menu")

    ui.sub_pages({'/': page_main.content, '/other': page_addApiary.content,
                 '/other2': page_addHive.content, 
                 '/other3': page_addInspection.content ,
                 '/other4': page_addtodo.content,
                 '/other5': page_addNucleus.content,
                 '/other6': page_addTreatment.content,
                 '/other11': page_displayHive.content,
                 #'/other12': page_displayTodo.content,
                 '/other12': page_displayTodo_Table_2.content,
                 '/other13': page_displayInspection.content,
                 '/other14': page_DisplayAllHives.content,
                 '/other15': page_displayAllTreatments.content,
                 #'/other16': page_uploadImage.content})
                 #'/other16': page_uploadTextfileexample.content})
                 '/other17': page_exportData1.content,
                 '/other18': page_importData1.content})
    ui.context.client.sub_pages_router.on_path_changed(
        lambda path: ui.notify(f'Navigated to {path}')
    )

#header.create_header(left_drawer=ui.left_drawer(), title="Main Page")
#issue 7/Oct get Errno 98 address already in use
# change port to 8010 and Ok, why did it not f happen before, 'lsof -i' shows > 1 'LISTEN
ui.run(root, port=8000)
