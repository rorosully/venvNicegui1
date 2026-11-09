# main.py
from nicegui import ui
import page_main
import page_otherc
import page_addApiary
from state import traces, plot_update

#Does a sub page need to be called "page_nnn"? NO 
#import page_venvDisplayInspection
# I don't have an '/other' dir. Why is it working ? 

def root():
    ui.sub_pages({'/': page_main.content, '/other': page_otherc.content,
                 '/other2': page_addApiary.content })
    ui.context.client.sub_pages_router.on_path_changed(
        lambda path: ui.notify(f'Navigated to {path}')
    )
ui.run(root, port=8000)
