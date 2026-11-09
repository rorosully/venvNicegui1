from nicegui import ui
import page_venvDisplayInspection


@ui.page('/')
def index_page():
    ui.label('This is the main page')
    ui.link('Go to Page Two', '/second')

@ui.page('/second')
def second_page():
    ui.label('This is the second page')
    ui.link('Go to Main Page', '/')

#add code from yt tut
#jul '26 gives error
#
@ui.page('/inspection')
def inspection_page() -> None:
    page_venvDisplayInspection.content()
    

ui.run()