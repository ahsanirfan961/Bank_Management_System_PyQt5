from PyQt5.QtWidgets import QDialog, QLineEdit
from PyQt5.uic import loadUi
from .SignUp import SignUp
from .MainMenu import MainMenu
from . import data



class SignIn(QDialog):

    def __init__(self):
        super(SignIn, self).__init__()
        loadUi("UI/signin.ui", self)
        self.signupButton.clicked.connect(self.goto_signup)
        self.signinButton.clicked.connect(self.goto_menu)
        self.eye_password.clicked.connect(self.passwordMask)
        self.email_entry.setTabOrder(self.email_entry, self.password_entry)
        self.password_entry.setTabOrder(self.password_entry,self.signinButton)
        
    def goto_signup(self):
        signup = SignUp()
        data.widget.addWidget(signup)
        data.widget.setCurrentIndex(data.widget.currentIndex() + 1)
   
    def goto_menu(self):
        username = self.email_entry.text()
        password = self.password_entry.text()

        if username != '' and password != '':
            login = data.sqlManager.getRowAND(self, 'Application_User', ['*'], ['Email', 'Password'], [username, password])
            if login!=[]:
                data.CurrentUserID = int(login[0][0])
                data.CurrentUserName = '{} {}'.format(login[0][1] , login[0][2])
                balance = data.sqlManager.getRow(self, 'Personal_Info', ['Balance'], ['User_ID', data.CurrentUserID])
                if balance!=[]:
                    data.CurrentBalance = balance[0][0]
                else:
                    data.CurrentBalance = 0
                menu = MainMenu()
                data.widget.addWidget(menu)
                data.widget.setCurrentIndex(data.widget.currentIndex() + 1)
            else:
                self.errorLabel.setText("Incorrect username or password!")
        else:
            self.errorLabel.setText("Please fill in all fields!")
                       
    def passwordMask(self):
        if self.eye_password.isChecked():
            self.password_entry.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password_entry.setEchoMode(QLineEdit.EchoMode.Password)