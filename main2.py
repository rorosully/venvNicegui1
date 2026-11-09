# main.py
from nicegui import ui
import page_main
import page_venvDisplayInspection

def root():
    ui.sub_pages({'/': page_main.content, '/venvDisplayInspection': page_venvDisplayInspection.content })

ui.run(root, port=8000)