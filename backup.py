# this is a work in progress 
# need to modify code to watch for folder too
# add if statements for file orgnisation
# files to watch for includes ".txt", ".img", ".png",".zip"
# potencial fiz for thingecerse files is to move and up-zip or un-zip and move


# Created on 21/10/2022
# By Tosin Abiiba

# this is the base templet 


from ast import pattern
from genericpath import isfile
from hashlib import new
import os
import watchdog.events
import watchdog.observers
import shutil

from macpath import split

class Handler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self) :
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns= ['.jpg','.mp4','.stl'],
                                                    ignore_directories= False, case_sensitive= True )
    
    # def on_created(self, event):
    #     if os.path() == '.jpg':
    #       print(f"JPEG was moved to the JPEG backup folder")
    #       shutil.move(event.src_path, r'/Users/tosinabiiba/Desktop/backed_up/JPEG')
    
    # def on_created(self, event):
    #     if pattern == '.mp4':
    #       print(f"JPEG was moved to the Video backup folder")
    #       shutil.move(event.src_path, r'/Users/tosinabiiba/Desktop/backed_up/VIDEO')
          
    # def on_created(self, event):
    #     if pattern == '.stl':
    #       print(f"JPEG was moved to the STL backup folder")
    #       shutil.move(event.src_path, r'/Users/tosinabiiba/Desktop/backed_up/STL')
    
    # def on_created(self, event):
    #     print(f"File was created at {event.src_path}")
    #     shutil.move(event.src_path, r'/Volumes/TDRIVE/Backup')
    
    def on_modified(self, event):
        for filename in os.path.isfile(r'/Users/tosinabiiba/Downloads'):
            i = 1
            if filename != backed_up:
                new_name = filename
                split_name = filename.split('.')
                file_exists = os.path.isfile(r'/Users/tosinabiiba/Desktop/backed_up' + '/' + new_name )
                while file_exists:
                    i += 1
                    new_name = os.path.splitext(r'/Users/tosinabiiba/Downloads' + '/' + new_name)[0] + str(i) + os.
                    # continue from here
        
    def on_deleted(self, event):
        print(f"File was deleted at {event.src_path}")

event_handler = Handler ()
observer = watchdog.observers.Observer()
observer.schedule(event_handler, r'/Users/tosinabiiba/Downloads', recursive= False)
observer.start()
observer.join()