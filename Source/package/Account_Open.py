from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi
from .functions import back, contains_only_alphabets
from .Zakaat import Zakaat
from . import data
from .data import Account_Types, Currency

class Account_Open(QDialog):
    def __init__(self):
        super(Account_Open, self).__init__()
        loadUi("UI/account.ui", self)
        self.back.clicked.connect(lambda:back(self, True))
        self.forward.clicked.connect(self.goto_zakat)
        self.update()

    def goto_zakat(self):
        if not self.validate():
            return False
        else:
            self.save()
            zakat = Zakaat()
            data.widget.addWidget(zakat)
            data.widget.setCurrentIndex(data.widget.currentIndex() + 1)
        
    def validate(self):
            data.accounttype = self.AccountBox.currentText()
            data.currencytype = self.CurrencyBox.currentText()
            data.title=self.title_entry.text()
            data.Us1=self.US1.isChecked()
            data.Us2=self.US2.isChecked()
            data.Us3=self.US3.isChecked()
            data.Us4=self.US4.isChecked()
        
            if not (data.accounttype == 'Account Type'or data.currencytype == "Select" or data.title == ''):
                print()
            elif not contains_only_alphabets(data.title):
                print()
            else:
                messagebox = QMessageBox()
                messagebox.setText('Information not Correct')
                messagebox.setIcon(QMessageBox.Critical)
                messagebox.setWindowTitle('Error')
                messagebox.show()
                messagebox.exec_()
                return False
                
            
            return True
            
    def save(self):
        
        data.accounttype = self.AccountBox.currentText()
        data.accounttype_index=0
        for i in Account_Types:
                if data.accounttype==i:
                    break 
                data.accounttype_index = data.accounttype_index + 1
                
        data.currencytype = self.CurrencyBox.currentText()
        data.currencytype_index=0
        for i in Currency:
            if data.currencytype==i:
                    break 
            data.currencytype_index = data.currencytype_index + 1
                
        data.title=self.title_entry.text()
        data.Us1=self.US1.isChecked()
        data.Us2=self.US2.isChecked()
        data.Us3=self.US3.isChecked()
        data.Us4=self.US4.isChecked()

    def update(self):
        
        self.AccountBox.setCurrentText(Account_Types[data.accounttype_index])
        self.CurrencyBox.setCurrentText(Currency[data.currencytype_index])
        self.title_entry.setText(data.title)
        self.US1.setChecked(data.Us1)
        self.US2.setChecked(data.Us2)
        self.US3.setChecked(data.Us3)
        self.US4.setChecked(data.Us4)