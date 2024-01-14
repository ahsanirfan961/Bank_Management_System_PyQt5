import pyodbc, sys
from PyQt5.QtWidgets import QMessageBox, QFrame, QLabel, QApplication, QDialog
from PyQt5.QtCore import Qt, QTimer, QEventLoop
from PyQt5.QtGui import QMovie
from PyQt5 import QtWidgets


class SQLManager():
    
    def __init__(self):
        with open('Configuration.config', 'r') as file:
            connection_string = str(file.read().strip())
        try:
            self.conn = pyodbc.connect(connection_string)
            print("Connected to SQL Server successfully!")
        except pyodbc.Error as e:
            print("Error connecting to SQL Server:", e) 
            messagebox = QMessageBox()
            messagebox.setText("Couldn't connect to the server!")
            messagebox.setIcon(QMessageBox.Critical)
            messagebox.setWindowTitle('Error')
            messagebox.show()
            messagebox.exec_()

        self.cursor = self.conn.cursor()
        self.loadingMovie = QMovie('Images/loading.gif')
        self.result = None
    
    def getRow(self, parent,  tableName, columns):
        frame = QFrame(parent)
        label = QLabel(frame)
        self.startLoading(parent, frame, label)
        columnNames = ', '.join(columns)
        query = f"SELECT {columnNames} FROM {tableName};"
        self.cursor.execute(query)
        self.stopLoading(frame, label)
        return self.cursor.fetchall()
    
    def getRow(self, parent, tableName, columns, defaultValue):
        self.result = None
        frame = QFrame(parent)
        label = QLabel(frame)
        self.startLoading(parent, frame, label)
        columnNames = ', '.join(columns)
        query = f"SELECT {columnNames} FROM {tableName} WHERE {defaultValue[0]} = '{defaultValue[1]}';"
        self.cursor.execute(query)
        self.result = self.cursor.fetchall()
        self.stopLoading(frame, label)
        return self.result
    
    def getRowNoLoad(self, parent, tableName, columns, defaultValue):
        columnNames = ', '.join(columns)
        query = f"SELECT {columnNames} FROM {tableName} WHERE {defaultValue[0]} = {defaultValue[1]};"
        self.cursor.execute(query)
        return self.cursor.fetchall()
        
    def getRowAND(self, parent, tableName, columns, defaultColumns, defaultValues):
        self.result = None
        frame = QFrame(parent)
        label = QLabel(frame)
        self.startLoading(parent, frame, label)
        columnNames = ', '.join(columns)
        conditions = []
        for i in range(0, len(defaultColumns)):
            conditions.append(f" {defaultColumns[i]} = '{defaultValues[i]}'")
        condition = ' AND '.join(conditions)
        query = f"SELECT {columnNames} FROM {tableName} WHERE{condition};"
        self.cursor.execute(query)
        self.result = self.cursor.fetchall()
        self.stopLoading(frame, label)
        return self.result
    
    def getRowOR(self, parent, tableName, columns, defaultColumns, defaultValues):
        self.result = None
        frame = QFrame(parent)
        label = QLabel(frame)
        self.startLoading(parent, frame, label)
        columnNames = ', '.join(columns)
        conditions = []
        for i in range(0, len(defaultColumns)):
            conditions.append(f" {defaultColumns[i]} = '{defaultValues[i]}'")
        condition = ' OR '.join(conditions)
        query = f"SELECT {columnNames} FROM {tableName} WHERE{condition};"
        self.cursor.execute(query)
        self.result = self.cursor.fetchall()
        self.stopLoading(frame, label)
        return self.result
    
    def insertRow(self, parent, tableName, columns, values):
        self.result = None
        frame = QFrame(parent)
        label = QLabel(frame)
        self.startLoading(parent, frame, label)
        columnNames = ', '.join(columns)
        columnValues = "', '".join(values)
        query = f"INSERT INTO {tableName}(ID, {columnNames}) VALUES ((SELECT MAX(ID)+1 FROM {tableName}), '{columnValues}');"
        self.cursor.execute(query)
        if self.cursor.rowcount >0:
            self.result = 1
            self.cursor.commit()
        self.stopLoading(frame, label)
        if self.cursor.rowcount>0:
            return True
        return False
    
    def updateRow(self, parent, tableName, columns, values, defaultValues):
        self.result = None
        frame = QFrame(parent)
        label = QLabel(frame)
        self.startLoading(parent, frame, label)
        conditions = []
        for i in range(0, len(columns)):
            conditions.append(f" {columns[i]} = '{values[i]}'")
        condition = ', '.join(conditions)
        query = f"UPDATE {tableName} SET {condition} WHERE {defaultValues[0]} = '{defaultValues[1]}';"
        self.cursor.execute(query)
        if self.cursor.rowcount >0:
            self.result = 1
            self.cursor.commit()
        self.stopLoading(frame, label)
        if self.cursor.rowcount>0:
            return True
        return False
    
    def executeQuery(self, parent, query):
        mode = query.split(' ', 1)[0]
        self.result = None
        frame = QFrame(parent)
        label = QLabel(frame)
        self.startLoading(parent, frame, label)
        self.cursor.execute(query)
        if mode == 'SELECT':
            self.result = self.cursor.fetchall()
        else:
            if self.cursor.rowcount > 0:
                self.cursor.commit()
                self.result = 1
        self.stopLoading(frame, label)
        if mode == 'SELECT':
            return self.result
        else:
            if self.cursor.rowcount > 0:
                return True
            else:
                False
    
    def startLoading(self, parent, frame, label):

        frame.setGeometry(540, 300, 120, 120)
        frame.setWindowFlag(Qt.WindowStaysOnTopHint)
        frame.setStyleSheet(f"border-radius: 20px;background-color: rgb(255, 255, 255);")
        
        label.setGeometry(10, 10, 100, 100)
        label.setWindowFlag(Qt.WindowStaysOnTopHint)
        label.setStyleSheet(f"border-radius: 20px;background-color: rgb(255, 255, 255);")
        label.setMovie(self.loadingMovie)
        
        label.show()
        frame.show()
        
        self.loadingMovie.start()
        self.timer = QTimer(parent)
        self.timer.start(1200)
    
    def stopLoading(self, frame, label):
        self.totalTimeLoaded = 1000
        loop = QEventLoop()
        self.timer.timeout.connect(lambda: self.increaseLoading(loop))
        loop.exec_()
        frame.hide()
        frame.deleteLater()
        label.deleteLater()
        self.loadingMovie.stop()
    
    def increaseLoading(self, loop):
        if self.totalTimeLoaded ==5000:
            loop.quit()
            return
        if(self.result == None):
            self.timer.start(500)
            self.totalTimeLoaded+=500
        else:
            loop.quit()
        

        
    

        
        