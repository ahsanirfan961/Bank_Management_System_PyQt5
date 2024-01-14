from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QTableWidget
from PyQt5.QtCore import Qt, QTimer
from PyQt5.uic import loadUi
from . import data
from .functions import back
from datetime import date

class Statement(QDialog):
    def __init__(self, title, currency, address, cnic):
        super(Statement, self).__init__()
        loadUi("UI\E-Statement.ui", self)
        self.forward.setEnabled(False)
        self.back.clicked.connect(back)
        for i in range (0,5):
            if i == 1:
                self.table.setColumnWidth(i, 300)
                continue
            self.table.setColumnWidth(i,200)
        
        self.title.setText(title)
        self.currency.setText(currency)
        self.address.setText(address)
        self.cnic.setText(cnic)
        self.id.setText(str(data.CurrentUserID))
        
        timer = QTimer(self)
        timer.singleShot(100, self.update)
    
    def update(self):

        current_date = date.today()
        first_date_of_month = date(current_date.year, current_date.month, 1)

        i = data.sqlManager.executeQuery(self, f"SELECT date,description,debit,credit,balance FROM Statement WHERE User_ID = {data.CurrentUserID} AND date BETWEEN '{first_date_of_month}' AND '{current_date}' ORDER BY date DESC;")

        rows = len(i)

        for row in range(0,rows):
            self.table.insertRow(row)
            
            for column in range(self.table.columnCount()):
                item = QTableWidgetItem("{}".format(i[row][column]))
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self.table.setItem(row, column, item)




        