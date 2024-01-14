from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi
from .functions import back
from . import data

class Card_Details(QDialog):
    
    def __init__(self, type, title):
        super(Card_Details, self).__init__()
        loadUi("UI\cardDetails.ui", self)
        self.forward.setEnabled(False)
        self.back.clicked.connect(back)
        self.title.setText(title)
        self.type = type
        if type == 'Visa Debit Card':
            self.card.setPixmap(QPixmap('Images/Visa_Empty.png'))
        elif type == 'Paypak Debit Card':
            self.card.setPixmap(QPixmap('Images/Pay_Empty.png'))
        else:
            self.card.setPixmap(QPixmap('Images/Master_Empty.png'))
        self.View_button.clicked.connect(self.viewDetails)
            
    def viewDetails(self):
        details = data.sqlManager.getRowAND(self, 'Card', ['Number', 'Expr', 'CVV'], ['User_ID', 'Card_Type'], [data.CurrentUserID, self.type])[0]
        self.number.setText(details[0])
        self.exp.setText(details[1])
        self.cvv.setText(details[2])
        self.View_button.setEnabled(False)