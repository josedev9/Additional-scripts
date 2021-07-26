import requests
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
IN_prev,OUT_prev="0","0"
TIME_prev,LINES_prev=0,1
def fromstrtosecs(str):
    hour,minutes,seconds=str.split(":")
    return int(hour)*3600+int(minutes)*60+int(seconds)
def post(path,file_state):
    global IN_prev,OUT_prev,TIME_prev,LINES_prev
    url="http://10.161.9.64:1880/forusb"
    with open(path,"r+") as file:
        data=file.readlines()
        LINES_new=len(data)
        if LINES_new-LINES_prev==1 or file_state:
            IN_prev,OUT_prev,TIME_prev=IN_prev,OUT_prev,TIME_prev
        else:
            prev_more_data=data[-2].split("&")[0].split("-")[3]
            prev_raw=data[-2].split("&")[-2:]
            IN_prev=prev_raw[-2].split("=")[-1]
            OUT_prev=prev_raw[-1].split("=")[-1]
        more_data=data[-1].split("&")[0].split("-")[3]
        raw=data[-1].split("&")[-2:]
        IN_new=raw[-2].split("=")[-1]
        OUT_new=raw[-1].split("=")[-1]
        TIME_new=fromstrtosecs(more_data)
        print(IN_new,IN_prev)
        print(OUT_new,OUT_prev)
        print(TIME_new,TIME_prev)
        res_in=int(IN_new)-int(IN_prev)
        res_out=int(OUT_new)-int(OUT_prev)
        time=abs(TIME_new-TIME_prev) if LoggingEventHandler.new_file_created==True else TIME_new-TIME_prev
        print("RESULTS BELOW:")
        print(res_in)
        print(res_out)
        print(time)
        if (res_in!=0 and time>=1):
            requests.post(url,json=[{"IN":res_in},{"Camera":"Usb"}])
            #IN_prev=IN_new
            #TIME_prev=TIME_new
        if (res_out!=0 and time>=1):
            requests.post(url,json=[{"OUT":res_out},{"Camera":"Usb"}])
            #OUT_prev=OUT_new
            #TIME_prev=TIME_new 
            
        IN_prev=IN_new
        OUT_prev=OUT_new
        TIME_prev=TIME_new 
        LINES_prev=LINES_new
        return IN_prev,OUT_prev,TIME_prev,LINES_prev


class LoggingEventHandler(FileSystemEventHandler):
    """Logs all the events captured."""
    new_file_created=False

    def __init__(self, logger=None):
        super().__init__()

        self.logger = logger or logging.root

    """def on_moved(self, event):
        super().on_moved(event)

        what = 'directory' if event.is_directory else 'file'
        self.logger.info("Moved %s: from %s to %s", what, event.src_path,
                         event.dest_path)"""
      

    def on_created(self, event):
        super().on_created(event)

        what = 'directory' if event.is_directory else 'file'
        self.logger.info("Created %s: %s", what, event.src_path)
        self.new_file_created=True
        self.logger.info(f"new_file_created={self.new_file_created}")
        

    """def on_deleted(self, event):
        super().on_deleted(event)

        what = 'directory' if event.is_directory else 'file'
        self.logger.info("Deleted %s: %s", what, event.src_path)"""

    def on_modified(self, event):
        super().on_modified(event)
        what = 'directory' if event.is_directory else 'file'
        self.logger.info("Modified %s: %s", what, event.src_path)
        if what=="file":
            post(event.src_path,self.new_file_created)
            self.new_file_created=False
        
        

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = "/home/pi/Desktop/raspberry"
    event_handler = LoggingEventHandler()

    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


