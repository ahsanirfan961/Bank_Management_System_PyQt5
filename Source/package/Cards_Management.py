from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QTimer
from PyQt5.uic import loadUi
from . import data
from .functions import back
from .Card_Order import Card_Order
from .CardDetails import Card_Details

class Card_Management(QDialog):
    
    def __init__(self):
        super(Card_Management, self).__init__()
        loadUi("UI\card.ui", self)
        self.forward.setEnabled(False)
        self.back.clicked.connect(back)
        self.Visa_button.clicked.connect(lambda:self.goto_details('Visa Debit Card'))
        self.Paypak_button.clicked.connect(lambda:self.goto_details('Paypak Debit Card'))
        self.Mastercard_button.clicked.connect(lambda:self.goto_details('Mastercard Debit Card'))
 
        self.Visa_lock.clicked.connect(self.visaclicked)
        self.Paypak_lock.clicked.connect(self.Paypakclicked)
        self.Mastercard_lock.clicked.connect(self.Mastercardclicked)

        timer = QTimer(self)
        timer.singleShot(100, self.updateAll)
       
    def goto_details(self, type):
        cards = data.sqlManager.getRow(self, 'Card', ['Card_Type', 'Card_Title'], ['User_ID', data.CurrentUserID])
        if cards == []:
            details = Card_Order(type)
        else:
            cardExists = False
            for i in cards:
                if i[0] == type:
                    cardExists = True
                    title = i[1]
            if cardExists:
                details = Card_Details(type, title)
            else:
                details = Card_Order(type)
        data.widget.addWidget(details)
        data.widget.setCurrentIndex(data.widget.currentIndex() + 1)

    def visaclicked(self):
        if self.Visa_lock.isChecked():
            data.sqlManager.executeQuery(self, f"UPDATE Card SET Lock = 'True' WHERE User_ID = '{data.CurrentUserID}' AND Card_Type = 'Visa Debit Card';")
        else:
            data.sqlManager.executeQuery(self, f"UPDATE Card SET Lock = 'False' WHERE User_ID = '{data.CurrentUserID}' AND Card_Type = 'Visa Debit Card';")
        self.update(card_type='Visa')
            
    def Paypakclicked(self):
        if self.Paypak_lock.isChecked():
            data.sqlManager.executeQuery(self, f"UPDATE Card SET Lock = 'True' WHERE User_ID = '{data.CurrentUserID}' AND Card_Type = 'Paypak Debit Card';")
        else:
            data.sqlManager.executeQuery(self, f"UPDATE Card SET Lock = 'False' WHERE User_ID = '{data.CurrentUserID}' AND Card_Type = 'Paypak Debit Card';")
        self.update(card_type='Pay')
            
    def Mastercardclicked(self):
        if self.Mastercard_lock.isChecked():
            data.sqlManager.executeQuery(self, f"UPDATE Card SET Lock = 'True' WHERE User_ID = '{data.CurrentUserID}' AND Card_Type = 'Mastercard Debit Card';")
        else:
            data.sqlManager.executeQuery(self, f"UPDATE Card SET Lock = 'False' WHERE User_ID = '{data.CurrentUserID}' AND Card_Type = 'Mastercard Debit Card';")
        self.update(card_type='Master')

    def update(self, card_type):
        if card_type == 'Visa':
            exist = data.sqlManager.getRowAND(self, 'Card', ['Lock'], ['User_ID', 'Card_Type'], [data.CurrentUserID, 'Visa Debit Card'])
            if exist!=[]:
                if exist[0][0]:
                    self.Visa_label.setText("Locked")
                    self.Visa_lock.setChecked(True)
                else:
                    self.Visa_lock.setChecked(False)
                    self.Visa_label.setText("Active")
                self.Visa_label.setStyleSheet('font: 12pt "Segoe UI Black";color: rgb(0, 170, 0);')
                self.Visa_lock.setEnabled(True)
                    
            else:
                self.Visa_label.setText("InActive")
                self.Visa_label.setStyleSheet('font: 12pt "Segoe UI Black";color: red;')
                self.Visa_lock.setEnabled(False)
            

        if card_type == 'Pay':
            exist = data.sqlManager.getRowAND(self, 'Card', ['Lock'], ['User_ID', 'Card_Type'], [data.CurrentUserID, 'Paypak Debit Card'])
            if exist!=[]:
                if exist[0][0]:
                    self.Papak_label.setText("Locked")
                    self.Paypak_lock.setChecked(True)
                else:
                    self.Paypak_lock.setChecked(False)
                    self.Papak_label.setText("Active")
                self.Papak_label.setStyleSheet('font: 12pt "Segoe UI Black";color: rgb(0, 170, 0);')  
                self.Paypak_lock.setEnabled(True)                 
            else:
                self.Papak_label.setText("InActive")
                self.Papak_label.setStyleSheet('font: 12pt "Segoe UI Black";color: red;')
                self.Paypak_lock.setEnabled(False)

        if card_type == 'Master':
            exist = data.sqlManager.getRowAND(self, 'Card', ['Lock'], ['User_ID', 'Card_Type'], [data.CurrentUserID, 'Mastercard Debit Card'])
            if exist!=[]:
                if exist[0][0]:
                    self.Mastercard_label.setText("Locked")
                    self.Mastercard_lock.setChecked(True)
                else:
                    self.Mastercard_lock.setChecked(False)
                    self.Mastercard_label.setText("Active")
                self.Mastercard_label.setStyleSheet('font: 12pt "Segoe UI Black";color: rgb(0, 170, 0);')  
                self.Mastercard_lock.setEnabled(True)    
            else:
                self.Mastercard_label.setText("InActive")
                self.Mastercard_label.setStyleSheet('font: 12pt "Segoe UI Black";color: red;')
                self.Mastercard_lock.setEnabled(False)
        
    def updateAll(self):
        self.update(card_type='Visa')
        self.update(card_type='Pay')
        self.update(card_type='Master')

