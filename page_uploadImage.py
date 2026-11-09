from nicegui import ui,events

#import a text file and display it
#Oct '26

#Does there need to be a 'content() fn as standard for a page
# issue: can choose text file but not displlayed
# result: you need to click icon again after upload to see contents
#def uploads(e: events.UploadEventArguments):
def content(e: events.UploadEventArguments):
    
    
    # Read the content of the file
    #text = e.content.read().decode('utf-8')
    text = e.content.read()

    #print the file
    print(text) #nothing printed
    
    markdown.set_content(text)
# Why there a "." before \ ? Its not in uploadextfile ex.py pge_
#ui.uploas(on_upload=uploads,
ui.upload(auto_upload=True,on_upload=content,
           on_rejected =lambda:ui.notify('Only text files accepted')).\
           props("accept=.txt").\
           classes("max-w-full")

markdown = ui.markdown('Choose text file')
#use main3.py
#ui.run()
