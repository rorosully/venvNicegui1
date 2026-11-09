#!/usr/bin/env python3
"""
sqlite_viewer.py - a small read-only web viewer for a SQLite database.

Pick any table or view from the dropdown and its full contents are shown in a
sortable, filterable, paginated grid. The database is opened in SQLite's
read-only mode, so nothing this program does can modify or lock your data.

-----------------------------------------------------------------------------
WHAT YOU NEED TO PROVIDE
-----------------------------------------------------------------------------

1. SQLITE_DB  (required)
   Environment variable holding the *filesystem path* to the database file.
   It is a plain path - NOT a sqlite:// / SQLAlchemy URL.

       export SQLITE_DB=/home/lisa/data/qos.sqlite

   Relative paths are resolved against the current working directory and a
   leading '~' is expanded, so these are all fine:

       export SQLITE_DB=./local.db
       export SQLITE_DB=~/data/qos.sqlite
       export SQLITE_DB=/var/lib/myapp/app.db

   The file must already exist. Read-only mode will not create one for you,
   and the process needs read permission on both the file and its directory.

2. SQLITE_VIEWER_PORT  (optional, default 8080)
   Only change this if 8080 is already in use on the machine.

       export SQLITE_VIEWER_PORT=8090

   The server always binds to 127.0.0.1 (loopback), so it is reachable only
   from this machine and needs no authentication. If you ever need to reach
   it from another host, change HOST below to '0.0.0.0' - but put a password
   or an SSH tunnel in front of it first, because anyone who can reach the
   port can read the whole database.

-----------------------------------------------------------------------------
INSTALL AND RUN (Linux)
-----------------------------------------------------------------------------

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

    export SQLITE_DB=/path/to/your.db
    python3 sqlite_viewer.py

Then open http://127.0.0.1:8080 (a browser tab is opened automatically if the
machine has a desktop session). Ctrl-C in the terminal stops the server.
"""

import os
import sqlite3
from contextlib import closing
from pathlib import Path

from nicegui import ui

# --- Settings you may want to tweak -----------------------------------------

HOST = '127.0.0.1'      # loopback only; see the SQLITE_VIEWER_PORT note above
PORT = int(os.environ.get('SQLITE_VIEWER_PORT', '8080'))
ROWS_PER_PAGE = 25      # grid page size; 0 would mean "one endless page"
NULL_DISPLAY = 'NULL'   # how SQL NULL is rendered, so it is distinguishable
                        # from an empty string stored in the column

# Every table is loaded in full, which is what you want for a small database.
# If some table ever grows into the hundreds of thousands of rows, add a
# 'LIMIT n' to the query in load_object() - the browser, not SQLite, is what
# will struggle first.

# --- Database access --------------------------------------------------------


def resolve_db_path() -> Path:
    """Read SQLITE_DB and fail with a clear message if it is unusable."""
    raw = os.environ.get('SQLITE_DB')
    if not raw:
        raise SystemExit(
            'SQLITE_DB is not set.\n'
            'Set it to the path of your SQLite file, e.g.:\n'
            '    export SQLITE_DB=/home/lisa/data/qos.sqlite'
        )
    path = Path(raw).expanduser().resolve()
    if not path.is_file():
        raise SystemExit(f'SQLITE_DB points at {path}, which is not an existing file.')
    return path


DB_PATH = resolve_db_path()

# file:...?mode=ro is SQLite's read-only open. as_uri() handles percent-encoding
# for paths containing spaces or other awkward characters.
DB_URI = f'{DB_PATH.as_uri()}?mode=ro'


def connect() -> sqlite3.Connection:
    """A fresh read-only connection. NiceGUI serves requests from several
    threads, and a SQLite connection is not safe to share across them, so we
    open one per query rather than keeping a global."""
    return sqlite3.connect(DB_URI, uri=True)


def list_objects() -> list[tuple[str, str]]:
    """Every user table and view in the database, as (name, 'table'|'view')."""
    sql = """
        SELECT name, type FROM sqlite_master
        WHERE type IN ('table', 'view') AND name NOT LIKE 'sqlite_%'
        ORDER BY type, name
    """
    with closing(connect()) as con:
        return [(row[0], row[1]) for row in con.execute(sql)]


def quote_identifier(name: str) -> str:
    """Safely inline a table name into SQL. Table names cannot be passed as
    bind parameters, so they are double-quoted with embedded quotes doubled."""
    return '"' + name.replace('"', '""') + '"'


def render(value: object) -> object:
    """Make one cell value safe and readable in the grid."""
    if value is None:
        return NULL_DISPLAY
    if isinstance(value, bytes):
        return f'<BLOB, {len(value)} bytes>'  # don't dump binary into the page
    return value


def load_object(name: str) -> tuple[list[dict], list[dict]]:
    """Return (column definitions, rows) for one table or view."""
    with closing(connect()) as con:
        cursor = con.execute(f'SELECT * FROM {quote_identifier(name)}')
        column_names = [description[0] for description in cursor.description]
        raw_rows = cursor.fetchall()

    columns = [
        {'name': col, 'label': col, 'field': col, 'align': 'left', 'sortable': True}
        for col in column_names
    ]
    rows = [
        # '__id__' is a synthetic key the grid needs to track rows; it is not
        # in the columns list above, so it stays hidden from the user.
        {'__id__': i, **{col: render(val) for col, val in zip(column_names, raw)}}
        for i, raw in enumerate(raw_rows)
    ]
    return columns, rows


# --- User interface ---------------------------------------------------------


@ui.page('/')
def index() -> None:
    objects = list_objects()

    with ui.header().classes('items-center justify-between px-4'):
        ui.label('SQLite viewer').classes('text-lg font-medium')
        ui.label(str(DB_PATH)).classes('text-xs opacity-70')

    if not objects:
        ui.label('This database contains no tables or views.').classes('m-8 text-lg')
        return

    # Dropdown labels show what each object is, e.g. "users  (table)".
    options = {name: f'{name}  ({kind})' for name, kind in objects}

    with ui.row().classes('w-full items-center gap-4 p-4'):
        picker = ui.select(
            options, value=objects[0][0], label='Table / view', with_input=True
        ).classes('w-96')
        search = ui.input(placeholder='Filter rows...').props('clearable dense outlined')
        ui.button(icon='refresh', on_click=lambda: show(picker.value)) \
            .props('flat round').tooltip('Reload from disk')
        summary = ui.label().classes('text-sm opacity-70')

    container = ui.column().classes('w-full px-4')

    def show(name: str | None) -> None:
        """Replace the grid with the contents of the selected table."""
        container.clear()
        if not name:
            return
        try:
            columns, rows = load_object(name)
        except sqlite3.Error as error:
            summary.text = ''
            with container:
                ui.label(f'Could not read "{name}": {error}').classes('text-red')
            return

        summary.text = f'{len(rows):,} rows x {len(columns)} columns'
        with container:
            table = ui.table(
                columns=columns,
                rows=rows,
                row_key='__id__',
                pagination={'rowsPerPage': ROWS_PER_PAGE},
            ).classes('w-full')
            # The filter box searches across every column of the loaded table.
            table.bind_filter_from(search, 'value')

    picker.on_value_change(lambda event: show(event.value))
    show(picker.value)


# NiceGUI may re-import this module in a worker process, hence '__mp_main__'.
if __name__ in {'__main__', '__mp_main__'}:
    ui.run(
        host=HOST,
        port=PORT,
        title='SQLite viewer',
        favicon='🗄️',
        reload=False,  # reload=True re-runs the module on every file save
        show=True,     # open a browser tab if there is a desktop session
    )
