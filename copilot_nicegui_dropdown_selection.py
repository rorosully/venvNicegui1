import sqlite3
from nicegui import ui

selected_name = None

def load_names_from_db(db_path='mydb52023.db', table_name='apiary', column_name='APIARY_NAME'):
    """Load names from SQLite database with error handling"""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(f'SELECT {column_name} FROM {table_name}')
        names = [row[0] for row in cursor.fetchall()]
        conn.close()
        return names
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []

def on_selection(name):
    """Handle selection from dropdown button"""
    global selected_name
    selected_name = name
    button.set_text(f'✓ {name}')
    status.set_text(f'Current selection: {selected_name}')
    menu.close()
    print(f"Selected name: {selected_name}")

# Load names from database
names = load_names_from_db()

# Create the UI
with ui.column().classes('w-full max-w-md m-auto p-6'):
    ui.label('Name Selection').classes('text-2xl font-bold mb-4')
    
    if names:
        # Create dropdown button with styling
        with ui.button(icon='person').props('no-caps color=primary') as button:
            button.set_text('Select a Name')
            with ui.menu() as menu:
                for name in names:
                    ui.menu_item(name, lambda n=name: on_selection(n))
        
        status = ui.label('No selection yet').classes('text-sm text-gray-600 mt-4 p-2')
    else:
        ui.label('No names found in database').classes('text-red-500')

ui.run()