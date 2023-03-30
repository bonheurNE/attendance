import os
import sys
import serial
from datetime import datetime
import json
import csv
import sqlite3
import time


from PySide6 import (QtWidgets, QtCore, QtGui)

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from views.ui_mainWindow import  *

class MonitorChanges(QThread):
    modified = Signal()
    def __init__(self, parent, csvfile):
        super().__init__()
        self.csvfile = csvfile
        self.status = True
        
    def run(self):
        # get the initial size of the csv file
        initial_csv_size = os.path.getsize(self.csvfile)
        
        while self.status:
            # get the current file size
            current_csv_size = os.path.getsize(self.csvfile)
            # check if the file size has changed
            if current_csv_size > initial_csv_size:
                # a new line has been added
                # manage the table view completion
                print("on modification")
                self.modified.emit()
                # update the new value of the initial size of the file
                initial_csv_size = current_csv_size
                
            else:
                pass
            
            time.sleep(1)
        sys.exit(-1)
        
class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.createFolders()
        self.createFiles()
        
        
        self.monitorCsvFileChanges()
        self.initialiseVariables()
        
        self.ui.pushButton.clicked.connect(lambda:self.startThread())
        self.ui.pushButton_2.clicked.connect(lambda:self.endThread())
        self.ui.pushButton_3.clicked.connect(lambda:self.populate())
        
        self.model = QStandardItemModel(self)
        self.ui.dataTableView.setModel(self.model)
        
        
    def initialiseVariables(self):
        self.scanned_roll_number = ""
        self.scanned_status = 1
        self.current_date = str(self.current_time())
        pass
    # fuction to manage scanning
    def scanned(self):
        return (self.scanned_roll_number,self.scanned_status,self.current_date)
    def closeEvent(self, event):
        # close the thread if the thread is open
        if self.status:
            self.endThread()
        else:
            pass
        
        # now finish the close event and close the window
        event.accept()
    @Slot()
    def populate(self):
        """
        for this part i think that the best idea would be to use the sqlite3 db th=able
        than i will take the roll number and check if it exist in the table 
        - if it exist we update the modified date and  we increment the attendance number 
        - if it does not exists we add that roll number as a number record
        """
        # create the connection to the db
        db_path = f"{self.document_main_path}/ATTENDANCES/attendances.db"
        
        connection = sqlite3.connect(db_path)
        
        # creating the cursor to use that db
        cursor = connection.cursor()
        
        roll_number = self.scanned_roll_number
        # sql statement to get all data into the database
        sql = """
        SELECT * FROM attendances WHERE rollNumber = ?;
        """
        
        cursor.execute(sql,(roll_number,))
        
        result = cursor.fetchone()
        
        # check if the data is in the table or not
        if result is not None:
            NEW_STATUS = int(result[2]) + 1
            # the data exists
            # update the data
            data = (NEW_STATUS, self.current_date, self.scanned_roll_number)
            
            # sql query
            sql3 = """
            UPDATE attendances SET status = ?,last_modified_date = ? WHERE rollNumber = ?;
            """
            # execute the update query
            cursor.execute(sql3, data)
            # Commit the transaction to save the changes to the database
            connection.commit()
        else:
            # the data does not exists
            data = (self.scanned_roll_number,self.scanned_status,self.current_date,self.current_date)
            # insert it as a new record
            sql2 = "INSERT INTO attendances (rollNumber,status,creation_date,last_modified_date) VALUES (?,?,?,?);"
            
            # execute the insert query
            cursor.execute(sql2,data)
            
            # Commit the transaction to save the changes to the database
            connection.commit()
            
        # close the cursor and the connection to the db
        cursor.close()
        connection.close()
            
        # function to manage serial communication data read and commitment to the csv file
        with open(self.csv_file_name, 'a', newline = "") as csv_f:
            writer = csv.writer(csv_f)
            
            # Write new rows of data to the CSV file
            writer.writerow(['202150126', 'TRUE', self.current_time()])
            csv_f.close() 
    @Slot()
    def endThread(self):
        self.status = False
        self.worker.terminate()
        time.sleep(1)
        
    @Slot()
    def startThread(self):
        self.status = True
        self.worker.start()
        """ with open(self.csv_file_name, 'a', newline = "") as csv_f:
            writer = csv.writer(csv_f)
            
            # Write new rows of data to the CSV file
            writer.writerow(['data1', 'data2', 'data3'])
            writer.writerow(['data4', 'data5', 'data6'])
            writer.writerow(['data6', 'data25', 'data33'])
            writer.writerow(['data7', 'data55', 'data64'])

            csv_f.close() """
    # function to get the current date and time as a string for data base
    def current_time(self):
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # function to change the model of the table view
    def manageTableView(self):
        pass
    
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
            current_date = current_date.strftime("%A %Y-%m-%d")
            
            # set The date to the date label
            self.ui.date.setText(str(current_date))
            
            # create the file name
            self.json_file_name = f"{self.document_main_path}/ATTENDANCES/ATTENDANCE-{current_date}.json"
            self.csv_file_name = f"{self.document_main_path}/ATTENDANCES/ATTENDANCE-{current_date}.csv"
            
            # check jso file exists if not create it else pass
            if not os.path.isfile(self.json_file_name):
                #generate json file
                dict = {}
                with open(self.json_file_name, 'w') as json_f:
                    json.dump(dict, json_f, indent=4)
            else:
                pass
            
            # check if the csv file exists if not create it else pass
            if not os.path.isfile(self.csv_file_name):
                # generate csv file
                data = ["ROLL NUMBER","STATUS","DATE"]
                with open(self.csv_file_name, 'xt', newline='') as csv_f:
                    # create writer 
                    writer = csv.writer(csv_f)
                    # write csv file headers
                    writer.writerow(data)
                # to make the file read-only mode 
                # os.chmod(csv_file_name,0o444)
            else:
                pass
            
            # create database and connect to it
            db_path = f"{self.document_main_path}/ATTENDANCES/attendances.db"
            
            connection = sqlite3.connect(db_path)
            
            # creating the cursor to use that db
            cursor = connection.cursor()
            
            # by using the cursor create the attendance table
            sql = """CREATE TABLE IF NOT EXISTS attendances 
                    (id INTEGER PRIMARY KEY, 
                    rollNumber TEXT, 
                    status INTEGER,
                    creation_date TEXT,
                    last_modified_date TEXT)"""
            cursor.execute(sql)
            
            # save changes to the db and close it
            connection.commit()
            connection.close()
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
    
    def monitorCsvFileChanges(self):
        def changeTabView():
            # clear the model first
            self.model.clear()
            
            """open the sqlite db table for attendance 
            get all the record inside and than convert them to the model
            than update the model and print it """
            with open(self.csv_file_name, 'r', newline='') as csv_f:
                reader = csv.reader(csv_f, delimiter=',')
                
                for row in reader:
                    items = [QStandardItem(field) for field in row]
                    self.model.appendRow(items)
            print("table mofied")
            
            
        def terminate():
            print("thread terminate")
            
        # get the initial size of the csv file
        """ initial_csv_size = os.path.getsize(self.csv_file_name)
        
        while True:
            # get the current file size
            current_csv_size = os.path.getsize(self.csv_file_name)
            # check if the file size has changed
            if current_csv_size > initial_csv_size:
                # a new line has been added
                # manage the table view completion
                self.manageTableView()
                # update the new value of the initial size of the file
                initial_csv_size = current_csv_size
                
            else:
                pass """
            
        #time.sleep(1)
        self.worker = MonitorChanges(self, self.csv_file_name)
        self.worker.finished.connect(terminate)
        self.worker.modified.connect(changeTabView)

        pass
    pass



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    sys.exit(app.exec())