import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEvent, FileSystemEventHandler

from_dir = "C:/Users/sheri/Downloads"
to_dir = "C:/Document_Files"

class FileEventHandler(FileSystemEventHandler) :
    
    def on_create(self, event) :
        print(f"Hey, {event.src_path}has been created!")
    
    def on_deleted(self, event) :
        print(f"Ops! Someone deleted {event.src_path}!")

    def on_modified(self, event) :
        print(f"Someone has modified {event.src_path}")   

    def on_moved(self, event) :
        print(f"The {event.src_path} has been moved.")

event_handler = FileEventHandler()

Observer = Observer()

Observer.schedule(event_handler, from_dir, recursive=True)

Observer.start()

list_of_files = os.listdir(from_dir)
#print(list_of_files)


for file_name in list_of_files:
    name,extension = os.path.splitext(file_name)
    if extension == '':
        continue
    if extension in ['.gif','.png','jpg','jpeg','jfif']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + 'image_files'
        path3 = to_dir + '/' + "image_files" + '/' + file_name
        if os.path.exists(path2):
            print("moving"+file_name+"......")    
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving"+file_name+"......")  
            shutil.move(path1,path3)

try : 
    while True : 
        time.sleep(2)
        print("running....")
except KeyboardInterrupt :
    print("stopped!")
    Observer.stop()
