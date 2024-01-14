from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi
from . import data
from .functions import back
import datetime


class Send_Money(QDialog):
    
    def __init__(self, receiverId, receiverName):
        super(Send_Money, self).__init__()
        loadUi("UI/Sendmoney.ui", self)
        self.back.clicked.connect(back)
        self.forward.setEnabled(False)
        self.sendertxt.setEnabled(False)
        self.Receivertxt.setEnabled(False)
        self.ReceiverID.setEnabled(False)
        self.Send_Money.clicked.connect(self.send_money)
        
        self.receiverId = receiverId

        self.sendertxt.setText(data.CurrentUserName)
        self.Receivertxt.setText(receiverName)
        self.ReceiverID.setText(receiverId)

    def send_money(self):
        amount = self.Amount.text()   
        
        if int(amount) <= int(data.CurrentBalance):
            balance = int(data.CurrentBalance) - int(amount)
            if data.sqlManager.updateRow(self, 'Personal_Info', ['Balance'], [balance], ['User_ID', data.CurrentUserID]):
                receiverbalance = data.sqlManager.getRow(self, 'Personal_Info', ['Balance'], ['User_ID', self.receiverId])[0][0]
                receiverbalance = int(receiverbalance)+int(amount)
                if data.sqlManager.updateRow(self, 'Personal_Info', ['Balance'], [receiverbalance],['User_ID', self.receiverId]):
                    currentDate = str(datetime.date.today())
                    
                    description = 'Online Cash Transferred from 0000{} to 0000{}'.format(data.CurrentUserID, self.receiverId)
                    
                    data.sqlManager.insertRow(self, 'Statement', ['User_ID', 'date', 'description', 'debit', 'balance'], [str(data.CurrentUserID), currentDate, description, amount, str(balance)])
                    
                    data.sqlManager.insertRow(self, 'Statement', ['User_ID', 'date', 'description', 'credit', 'balance'], [str(self.receiverId), currentDate, description, amount, str(receiverbalance)])

                    messagebox = QMessageBox()
                    messagebox.setText('Money Sent Successfully!')
                    messagebox.setIcon(QMessageBox.Information)
                    messagebox.setWindowTitle('Congratulations😁')
                    messagebox.show()
                    messagebox.exec_()
                else:
                    messagebox = QMessageBox()
                    messagebox.setText('Could not tranfer money\nPlease try again later!')
                    messagebox.setIcon(QMessageBox.Critical)
                    messagebox.setWindowTitle('Error')
                    messagebox.show()
                    messagebox.exec_()
            else:
                messagebox = QMessageBox()
                messagebox.setText('Could not tranfer money\nPlease try again later!')
                messagebox.setIcon(QMessageBox.Critical)
                messagebox.setWindowTitle('Error')
                messagebox.show()
                messagebox.exec_()
        else:
            messagebox = QMessageBox()
            messagebox.setText('Not Enough Balance!')
            messagebox.setIcon(QMessageBox.Critical)
            messagebox.setWindowTitle('Error')
            messagebox.show()
            messagebox.exec_()



        
        





