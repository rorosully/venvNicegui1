import nicegui
from nicegui import ui

#17/6/26
# Ex 2 Elements

ui.label ('hello').classes('text-h1')
ui.link('https://nicegui.github.io', "https://pythonguis.com")
ui.chat_message("Hell", name = "python guis chatbot")

#markdown
ui.markdown (
    """
#MArkdown heading 1
**bold text**
*italic text*
'code' 
"""
)

ui.restructured_text(
    """
==========================
reStructuredText Heading 1
==========================
**bold text**
*italic text*
``code``
"""
)

ui.html("<strong>bold text using HTML tags</strong>")

#Control elements 
ui.button("Click me")

ui.run(title="NiceGUI Text Elements")

