from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from .Cards_Management import Card_Management
from .Personal_Info import Personal_Info
from .Cheque import Cheque
from .Account import Account
from .Profile_Settings import Profile_Settings
from . import data
from .findAccount import Find_Account
from .Statement import Statement


class MainMenu(QDialog):
    
    def __init__(self):
        super(MainMenu, self).__init__()
        loadUi("UI\menu.ui", self)
        # self.addimages()
        
        self.Namelbl.setText(data.CurrentUserName)
        self.IDlbl.setText(str(data.CurrentUserID))
        self.Card.clicked.connect(self.goto_card_management)
        self.Accounts.clicked.connect(self.goto_account)
        self.Profile.clicked.connect(self.goto_profile)
        self.Cheque.clicked.connect(self.goto_cheque)
        self.logout.clicked.connect(self.goto_signin)
        self.SendButton.clicked.connect(self.goto_find)
        self.balancelbl.setText(str(data.CurrentBalance))
        self.pushButton.clicked.connect(self.updatebalance)
        self.StatementButton.clicked.connect(self.goto_statement)

        if data.sqlManager.getRowNoLoad(self, 'Personal_Info', ['*'], ['User_ID', data.CurrentUserID])!=[]:
            data.CurrentAccountCreated = True
        else:
            data.CurrentAccountCreated = False
        
        if data.CurrentAccountCreated:
            self.Card.setEnabled(True)
            self.Cheque.setEnabled(True)
            self.SendButton.setEnabled(True)
            self.pushButton.setEnabled(True)
            self.StatementButton.setEnabled(True)
        else:
            self.Card.setEnabled(False)
            self.Cheque.setEnabled(False)
            self.SendButton.setEnabled(False)
            self.pushButton.setEnabled(False)
            self.StatementButton.setEnabled(False)

    def goto_card_management(self):
        card = Card_Management()
        data.widget.addWidget(card)
        data.widget.setCurrentIndex(data.widget.currentIndex() + 1)

    def goto_account(self):
        accountOpened = data.sqlManager.getRow(self, 'Personal_Info', ['ID'], ['User_ID', data.CurrentUserID])!=[]
        account = Account(accountOpened)
        data.widget.addWidget(account)
        data.widget.setCurrentIndex(data.widget.currentIndex() + 1)

    def goto_personal(self):
        personal = Personal_Info()
        data.widget.addWidget(personal)
        data.widget.setCurrentIndex(data.widget.currentIndex() + 1)

    def goto_cheque(self):
        cheque = Cheque()
        data.widget.addWidget(cheque)
        data.widget.setCurrentIndex(data.widget.currentIndex() + 1)

    def goto_profile(self):
        values = data.sqlManager.getRow(self, 'Application_User', ['First_Name', 'Last_Name', 'Email'], ['ID', data.CurrentUserID])[0]
        firstName = values[0]
        lastName = values[1]
        username = values[2]
        values = data.sqlManager.getRow(self, 'Contact', ['Mobile'], ['User_ID', data.CurrentUserID])
        if values!=[]:
            mobile = values[0][0]
        else:
            mobile = ''
        profile = Profile_Settings(firstName, lastName, username, mobile)
        data.widget.addWidget(profile)
        data.widget.setCurrentIndex(data.widget.currentIndex() + 1)
    
    def goto_signin(self):
        while data.widget.currentIndex()!=0:
            data.widget.removeWidget(data.widget.currentWidget())
    
    def goto_find(self):
        find = Find_Account()
        data.widget.addWidget(find)
        data.widget.setCurrentIndex(data.widget.currentIndex() + 1)
    
    def goto_statement(self):
        temp = data.sqlManager.getRow(self, 'Account', ['Title', 'Currency'], ['User_ID', data.CurrentUserID])
        title = str(temp[0][0])
        currency = str(data.Currency[int(temp[0][1])])
        address = data.sqlManager.getRow(self, 'Contact', ['PAddress'], ['User_ID', data.CurrentUserID])[0][0]
        cnic = data.sqlManager.getRow(self, 'Personal_Info',['CNIC'], ['User_ID', data.CurrentUserID])[0][0]
        statement = Statement(title, currency, address, cnic)
        data.widget.addWidget(statement)
        data.widget.setCurrentIndex(data.widget.currentIndex() + 1)

    def updatebalance(self):
        data.CurrentBalance = data.sqlManager.getRow(self, 'Personal_Info', ['Balance'], ['User_ID', data.CurrentUserID])[0][0]
        self.balancelbl.setText(str(data.CurrentBalance))

           