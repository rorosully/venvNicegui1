import sqlite3
from nicegui import ui

#my DB import stmt
from configDB import currDB

#SCript to showTodo 
# Aug 2026
#database = configDB.currDB


def load_from_sqlite(db_path: str, table_name: str) -> tuple[list[dict], list[dict]]:
    """
    Load data from SQLite table and return columns and rows for NiceGui table.
    
    Args:
        db_path: Path to the SQLite database file
        table_name: Name of the table to read
        
    Returns:
        Tuple of (columns, rows) formatted for NiceGui
    """
    #insert my DB conn OCt2 4 line
    database = currDB
    conn = sqlite3.connect('mydb52023.db')
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

   # conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row  # Return rows as dictionaries
    cursor = conn.cursor()
    
    # Get column information
    cursor.execute(f"PRAGMA table_info({table_name})")
    column_info = cursor.fetchall()
    
    # Format columns for NiceGui
    columns = [
        {
            'name': col[1],
            'label': col[1].replace('_', ' ').title(),
            'field': col[1]
        }
        for col in column_info
    ]
    
    # Fetch all rows
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = [dict(row) for row in cursor.fetchall()]
    
    conn.close()
    
    return columns, rows


# Example usage

#remove if __name_ line ,cause error
#if __name__ == '__main__':
if __name__ in {"__main__", "__mp_main__"}:    
    # Configuration
    #DB_PATH = 'example.db'
    #my DB
    DB_PATH = 'mydb52023.db'

    #TABLE_NAME = 'users'
    #my table
    TABLE_NAME = 'todo'
    
    # Create sample database if it doesn't exist
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                age INTEGER
            )
        ''')
        cursor.execute("DELETE FROM users")  # Clear existing data
        cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
                      ('Alice Johnson', 'alice@example.com', 30))
        cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
                      ('Bob Smith', 'bob@example.com', 27))
        cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
                      ('Charlie Brown', 'charlie@example.com', 35))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error creating sample database: {e}")
    
    # Load data from database
    columns, rows = load_from_sqlite(DB_PATH, TABLE_NAME)
    
    # Build the UI
    ui.label('SQLite Table Viewer').style('font-size: 24px; font-weight: bold')
    
    # Display table
    ui.table(
        columns=columns,
        rows=rows,
        #rows_per_page=10,
        pagination=True,
        selection='single'
    )
    
    # Display record count
    ui.label(f'Total Records: {len(rows)}')
    
    # Run the application
    ui.run()