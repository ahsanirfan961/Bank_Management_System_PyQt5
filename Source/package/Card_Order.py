from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi
from .functions import back, is_numeric_string,contains_only_alphabets
from . import data
import random


class Card_Order(QDialog):
    type_card = str()
    def __init__(self, type):
        super(Card_Order, self).__init__()
        loadUi("UI/card2.ui", self)
        self.back.clicked.connect(back)
        self.forward.setEnabled(False)
        self.type_entry.setText(type)
        self.type_card = type
        self.Save.clicked.connect(self.save)
        self.type_entry.setTabOrder(self.type_entry, self.title_entry)
        self.title_entry.setTabOrder(self.title_entry, self.tpin_check)
        self.tpin_check.setTabOrder(self.tpin_check, self.tpin_entry)

    def validate(self):
        title = self.title_entry.text()
        tpin_entry = self.tpin_entry.text()
        tpin_check = self.tpin_check.isChecked()
        
        if title == '':
            self.error.setText('Please enter a title!')
            return False
        else:
            self.error.setText('')
            if contains_only_alphabets(title):
                self.error.setText('')
            else:
                self.error.setText('Title can only contain alphabets!')
                return False
        
        if tpin_entry != '' and is_numeric_string(tpin_entry):
            self.error.setText('')
        else:
            self.error.setText('T-PIN can only contain numbers')
            return False
        
        return True
    
    def save(self):
        if self.validate():

            Cardtitle = self.title_entry.text()
            T_PIN = self.tpin_entry.text()
            T_PIN_check = self.tpin_check.isChecked()
            Card_Type = self.type_entry.text()
            cardNumber = f"{random.randint(2000, 9999)}    {random.randint(1000, 9999)}    {random.randint(1000, 9999)}    {random.randint(1000, 9999)}"
            cvv = f"{random.randint(100, 999)}"
            emonth = random.randint(1,12)
            eyear = random.randint(23, 50)
            expiry = ''
            if emonth<10:
                expiry+='0'
            expiry+=str(emonth)
            expiry+='/'
            expiry+=str(eyear)
             
            if data.sqlManager.insertRow(self, 'Card', ['User_ID', 'T_PIN_check', 'T_PIN', 'Card_Title', 'Card_Type', 'Lock', 'Number', 'Expr', 'CVV'], [str(data.CurrentUserID), str(T_PIN_check), T_PIN, Cardtitle, Card_Type, 'false', cardNumber, expiry, cvv]):
                message = QMessageBox(self)
                message.setText("Card Isseud Successfully✅")
                message.setIcon(QMessageBox.Information)
                message.setWindowTitle('Congratulations')
                message.show()
                message.exec_()
            
            data.widget.removeWidget(data.widget.currentWidget())
            data.widget.removeWidget(data.widget.currentWidget())