# this is a work in progress 
# need to modify code to watch for folder too
# add if statements for file orgnisation
# files to watch for includes ".jpg", ".img", ".png",".zip"
# potencial fiz for thingecerse files is to move and up-zip or un-zip and move
#
# smb://192.168.1.78


# Created on 21/10/2022
# By Tosin Abiiba

# this is the base templet 
import os
import shutil
import watchdog.events
import watchdog.observers

class Handler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        watchdog.events.PatternMatchingEventHandler.__init__(self,
                                                             patterns=['*.jpeg', '*.png', '*.pdf', '*.docx', '*.txt', '*.mp3', '*.mp4', '*.dmg', '*.exe', '*.stl', '*.gcode', '*.iso', '*.zip', '*.html', '*.xlsx'],
                                                             ignore_directories=True,
                                                             case_sensitive=True)

    def on_modified(self, event):
        file_path = event.src_path
        file_name, file_ext = os.path.splitext(file_path)
        if file_ext in ('.jpeg', '.png'):
            shutil.move(file_path, '/Users/tosinabiiba/Desktop/backed_up/Images')
        elif file_ext == '.pdf':
            shutil.move(file_path, '/Users/tosinabiiba/Desktop/backed_up/pdf')
        elif file_ext == '.docx':
            shutil.move(file_path, '/Users/tosinabiiba/Desktop/backed_up/documents')
        elif file_ext == '.txt':
            shutil.move(file_path, '/Users/tosinabiiba/Desktop/backed_up/texts')
        elif file_ext in ('.mp3', '.mp4'):
            shutil.move(file_path, '/Users/tosinabiiba/Desktop/backed_up//media')
        elif file_ext in ('.dmg', '.exe'):
            shutil.move(file_path, '/Users/tosinabiiba/Desktop/backed_up/software')
        elif file_ext in ('.stl', '.gcode'):
            shutil.move(file_path, '/Users/tosinabiiba/Desktop/backed_up/3Dprints')
        elif file_ext == '.iso':
            shutil.move(file_path, '/Users/tosinabiiba/Desktop/backed_up/iso')
        elif file_ext == '.zip':
            shutil.unpack_archive(file_path, '/Users/tosinabiiba/Desktop/backed_up/zips')
        elif file_ext == '.html':
            shutil.move(file_path, '/Users/tosinabiiba/Desktop/backed_up/html')
        elif file_ext == '.xlsx':
            shutil.move(file_path, '/Users/tosinabiiba/Desktop/backed_up/excel')
        else:
            print(f"Ignoring file with extension {file_ext}: {file_path}")

    def on_deleted(self, event):
        print(f"File was deleted at {event.src_path}")

event_handler = Handler()
observer = watchdog.observers.Observer()
observer.schedule(event_handler, '/Users/tosinabiiba/Downloads', recursive=False)
observer.start()
observer.join()
