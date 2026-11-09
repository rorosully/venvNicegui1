# state.py
from nicegui import Event

traces = []
plot_update = Event[dict]()