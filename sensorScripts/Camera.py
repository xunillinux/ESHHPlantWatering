
import os
import subprocess
import time
import logging

class Camera:

    def __init__(self):
        self.photoPathDirectory = "/var/www/html"

    def TakePhoto(self):
        self.ensure_dir(self.photoPathDirectory)
        photoName = "photos/img" + time.strftime("%Y%m%d-%H%M%S") + ".jpg"
        photoPath = self.photoPathDirectory + "/" + photoName
        command = "/usr/bin/sudo /usr/bin/raspistill -o " + photoPath
        logging.info("Camera.py: Taking photo: "+photoPath)

        return_code = subprocess.check_call(command, shell=True)
        
        return photoName
    
    def ensure_dir(self, file_path):
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)