from nicegui import ui
from pathlib import Path
from nicegui import app


#Sept '26 
# Image display from a folder on Linux laptop
# show the folder location

folder = Path(__file__).parent
#folder = Path('/home/aosulliv/Pictures/Nollaig_Japan_2025/kyoto_gardens/')
#folder = Path('/home/aosulliv/Pictures/Scotand1-2024')
ui.label(f"current Folder path: {folder})")


#Add the folder using static_files
#files = [f.name for f in folder.glob("*.jpg")]
#app.add_static_files('/temp', folder)
#app.add_static_files('')

#Use row container to hold images

#Images_container = ui.row().classes("full-flex item-denter") 

# Start adding images in a loop 
#for filename in files:
 #   with ui.card():
 #       ui.image(f"/temp/{filename}").style(f"width: 200px")
 #       ui.label(filename)

ui.run()

    