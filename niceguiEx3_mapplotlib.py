from matplotlib import pyplot as plt
from nicegui import ui

#Data elements
time = [1, 2, 3, 4, 5, 6]
temperature = [30, 32, 34, 32, 33, 31]

columns = [
    {
        "name":"time",
        "label": "Time(min)",
        "field":"time",
        "sortable": True,
        "align": "right",

    },
    {
        "name": "temperature",
        "label": "Temperature(°C)",
        "field": "temperature",
        "required": True,
        "align": "right",
    }, 

]
rows = [{time:t, temperature:temp}for t, temp in zip(time, temperature)]
        
ui.table(columns=columns, rows= rows, row_key="time")

with ui.pyplot(figsize=(5, 4)):
        plt.plot(time, temperature, "-o", color="blue", label="Temperature")
        plt.title("Temperature vs Time")
        plt.xlabel("Time (min)")
        plt.ylabel("temperature (°C)")
        plt.ylim(25, 40)
        plt.legend()
ui.run()



