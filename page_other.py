# page_other.py
from nicegui import ui
#import plotly.graph_objects as go
#from state import traces, plot_update

def content():
        ui.label('Another page content')
        ui.link('Go to main page', '/')
        ui.separator()

        #fig = go.Figure()

        #for data in traces:
        #        fig.add_trace(go.Scatter(x=data['x'], y=data['y']))

        #plot = ui.plotly(fig)

        #def add_trace(data):
         #       fig.add_trace(go.Scatter(x=data['x'], y=data['y']))
        #        plot.update()

        #t_update.subscribe(add_trace)