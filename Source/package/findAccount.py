from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi
from . import data
from .functions import back
from .Send_Money import Send_Money

class Find_Account(QDialog):
    
    def __init__(self):
        super(Find_Account, self).__init__()
        loadUi("UI/findAccount.ui", self)
        self.forward.setEnabled(False)
        self.back.clicked.connect(back)
        self.search.clicked.connect(self.check_id)
    
    def goto_money(self, id):
        temp = data.sqlManager.getRow(self, 'Personal_Info', ['FirstName', 'SecondName'], ['User_ID', id])
        receiverName = '{} {}'.format(temp[0][0], temp[0][1])
        money = Send_Money(id, receiverName)
        data.widget.addWidget(money)
        data.widget.setCurrentIndex(data.widget.currentIndex() + 1)

    def check_id(self):
        id = self.ID_entry.text()
        if data.sqlManager.getRow(self, 'Personal_Info', ['ID'], ['User_ID', id])!=[]:
            self.goto_money(id)
        else:
            messagebox = QMessageBox()
            messagebox.setText('Account not found!')
            messagebox.setIcon(QMessageBox.Critical)
            messagebox.setWindowTitle('Error')
            messagebox.show()
            messagebox.exec_()


    
    