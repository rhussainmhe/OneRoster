import zipfile
import os.path

file_path = './roster'

class Unzipper:
    global file_path
    def roster_unzip(self):

        #Unzip file if ./roster doesn't exist

        if not os.path.exists(file_path):
            with zipfile.ZipFile('roster.zip', 'r') as roster_zip:
                roster_zip.extractall('roster')
