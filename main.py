import os
import sys
import serial
from datetime import datetime
import json
import csv


from PySide6 import (QtWidgets, QtCore, QtGui)

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from views.ui_mainWindow import  *

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.createFolders()
        self.createFiles()
        
    def createFolders(self):
        # creating the main folder on the Document Folder of the PC
        # get the document folder path
        self.document_main_path = os.path.join(os.path.expanduser("~"), "Documents")
        
        # create the ATTENDANCES folder into the document folder
        os.makedirs(f"{self.document_main_path}/ATTENDANCES", exist_ok=True)
        pass
    def createFiles(self):
        # function to ceate json and csv files
        def createFile():
            # get the current date 
            current_date = datetime.now()
            current_date = current_date.strftime("%A, %Y-%m-%d")
            
            # set The date to the date label
            self.ui.date.setText(str(current_date))
            
            # create the file name
            date_name = current_date = current_date.strftime("%A %Y-%m-%d")
            json_file_name = f"{self.document_main_path}/ATTENDANCES/ATTENDANCE-{date_name}.json"
            csv_file_name = f"{self.document_main_path}/ATTENDANCES/ATTENDANCE-{date_name}.csv"
            
            #generate json file
            dict = {}
            with open(json_file_name, 'w') as json_f:
                json.dump(dict, json_f, indent=4)
            
            # generate csv file
            data = ["ROLL NUMBER","STATUS"]
            with open(csv_file_name, 'w', newline='') as csv_f:
                # create writer 
                writer = csv.writer(csv_f)
                # write csv file headers
                writer.writerow(data)
            pass
        # check if there is th attendance folder into the document main folder , 
        # if not create it by calling the createFolder function
        
        path =  f"{self.document_main_path}/ATTENDANCES"
        if os.path.exists(path):
            # create the csv and json file for each day date
            createFile()
        else:
            # create the folder and then create file
            self.createFolders()
            createFile()
        pass
    pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    sys.exit(app.exec())