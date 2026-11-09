# main.py
from nicegui import ui
import page_main
#import page_venvDisplayInspection
#try using page_other
#import page_otherb
import page_other
#-> None


def root():
    ui.label('Main page content')
    #ui.sub_pages({'/': page_main.content, '/venvDisplayInspection': page_venvDisplayInspection.content})
    ui.sub_pages({'/': page_main.content, '/other': page_other.content})
    ui.context.client.sub_pages_router.on_path_changed(
            lambda path: ui.notify(f'Navigated to {path}')
    )

def main():
 ui.label('Main page content')
 ui.link('Go to other page page_venvDisplayinspect', '/other')

#ui.run(root, port=8000)
ui.run(root)


