from nicegui import ui
from pathlib import Path
from nicegui import app


#Sept '26 
# Image display from a folder on Linux laptop
# show the folder location
# had to create an images folder in the venv DIR otherwise got 'dir 
# does not exist ' error 


# add show SIze fn

def show(size):
    Images_container.clear()
    with Images_container:
        for filename in files:
            with ui.card():
                ui.image(f"/Images/{filename}").style(f"width: {size}px")
                ui.label(filename)



# try add fn with 'size' and 'folder' as args

#folder = Path(__file__).parent
#folder = Path('/home/aosulliv/Pictures/Nollaig_Japan_2025/kyoto_gardens/')
# Scotland 2024
#folder = Path('/home/aosulliv/Pictures/Scotand1-2024')
#images
#folder = Path('/home/aosulliv/PythonProjects/niceGui1/venvNicegui1/images')
#Drumchambo 2026
folder = Path('/home/aosulliv/PythonProjects/niceGui1/venvNicegui1/Images_joemooney_2026/')
#Bilbao Pyrenees Beara Way 2025
#folder = Path('/home/aosulliv/PythonProjects/niceGui1/venvNicegui1/Images_bilbao_pyrenees_2025/')
#ucc oct 2023
#folder = Path('/home/aosulliv/PythonProjects/niceGui1/venvNicegui1/Images_ucc_oct_2023/')
#Scotland Apr 2024
#folder = Path('/home/aosulliv/PythonProjects/niceGui1/venvNicegui1/Images_scotland_apr_2024/')
#Bilbao pyrenees iPhone 2025
#folder = Path('/home/aosulliv/PythonProjects/niceGui1/venvNicegui1/Images_bilbao_pyrenees_iPhone_2025/')



ui.label(f"current Folder path: {folder})")

with ui.row():
    ui.button('Show 100 px', on_click=lambda: show(100))
    ui.button('Show 200 px', on_click=lambda: show(200))
    ui.button('Show 400 px', on_click=lambda: show(400))
    ui.button('Show 600 px', on_click=lambda: show(600))
    ui.button('Show 800 px', on_click=lambda: show(800))
    
# try add a button for each folder
with ui.row():
    #ui.button('Show scotland2024', on_click=lambda: showScotland2024())
    ui.button('Show scotland2024', on_click=lambda: showScotland2024())
    

#Add the folder using static_files
files = [f.name for f in folder.glob("*.JPG" or "*.JPEG") if f.is_file()]
app.add_static_files('/Images', folder)
#app.add_static_files('')

#Use row container to hold images

Images_container = ui.row().classes("full-flex items-center") 

#call show fn
#remove this if there are buttons for each folder e.g.showScotland2024
show(200)

def showScotland2024():
    global folder
   
    Images_container.clear()
    folder = Path('/home/aosulliv/Pictures/Scotand1-2024')
    show(200)


ui.run()

    