from nicegui import events, ui

#example code
#Oct '26 works, you need to click "+" icon again after upload to see contents
with ui.dialog().props('full-width') as dialog:
    with ui.card():
        markdown = ui.markdown()

async def handle_upload(e: events.UploadEventArguments):
    markdown.content = await e.file.text()
    dialog.open()

ui.upload(on_upload=handle_upload, max_file_size=1_000_000) \
    .props('accept=.txt').classes('max-w-full')

ui.run()