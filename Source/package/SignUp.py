from PyQt5.QtWidgets import QDialog, QLineEdit, QMessageBox
from PyQt5.uic import loadUi
from .functions import contains_only_alphabets
from . import data

class SignUp(QDialog):
    
    def __init__(self):
        super(SignUp, self).__init__()
        loadUi("UI/signup.ui", self)
        self.SignupButton.clicked.connect(self.signup)
        self.signin.clicked.connect(self.goto_signin)
        self.eye_password.clicked.connect(lambda: self.passwordMask(passwordBoxNumber=1))
        self.eye_repassword.clicked.connect(lambda: self.passwordMask(passwordBoxNumber=2))
        self.lname_entry.setTabOrder(self.fname_entry, self.lname_entry)
        self.lname_entry.setTabOrder(self.lname_entry, self.email_entry)
        self.lname_entry.setTabOrder(self.email_entry,self.password_entry)
        self.lname_entry.setTabOrder(self.password_entry,self.repassword_entry)
        self.repassword_entry.setTabOrder(self.repassword_entry,self.SignupButton)
                                     
    def goto_signin(self):
        while data.widget.currentIndex()!=0:
            data.widget.removeWidget(data.widget.currentWidget())
    
    def validate(self):
        firstname = self.fname_entry.text()
        lastname = self.lname_entry.text()
        email = self.email_entry.text()
        password = self.password_entry.text()
        repassword = self.repassword_entry.text()
        terms = self.terms.isChecked()
        
        if not contains_only_alphabets(firstname):
            self.fname_error.setText("Name is invalid!")
            return False
        else:
            self.fname_error.setText("")
            
        if not contains_only_alphabets(lastname):
            self.lname_error.setText("Name is invalid!")
            return False
        else:
            self.lname_error.setText("")
        
        if len(password)<8:
            self.error_password.setText("Password must of minimum 8 characters!")
            return False
        else:
            self.error_password.setText("")
        
        if repassword != password:
            self.error_repassword.setText("Password don't match!")
            return False
        else:
            self.error_repassword.setText("")

        if firstname == '' or lastname == '' or email == '' or password == '' or repassword == '':
            self.error.setText("All fields are required!")
            return False
        else:
            self.error.setText("")
        
        if terms:
            self.error.setText("")
        else:
            self.error.setText("Please agree to terms and conditions!")
            return False
        
        exist = data.sqlManager.getRow(self, 'Application_User', ['ID'], ['Email', email])!=[]
        if exist:
            self.email_error.setText("This username is already taken!")
            return False
        
        return True
        
    def signup(self):
        
        if self.validate():
            firstname = self.fname_entry.text()
            lastname = self.lname_entry.text()
            email = self.email_entry.text()
            password = self.password_entry.text()

            if data.sqlManager.insertRow(self, 'Application_User', ['First_Name', 'Last_name', 'Email', 'Password'], [firstname, lastname, email, password]):
                message = QMessageBox(self)
                message.setText("Login Account Created Successfully✅")
                message.setIcon(QMessageBox.Information)
                message.setWindowTitle('Congratulations')
                message.show()
                message.exec_()
                self.goto_signin()
            else:
                message = QMessageBox(self)
                message.setText("Couldn't create you account!\nPlease try again later")
                message.setIcon(QMessageBox.Critical)
                message.setWindowTitle('Error')
                message.show()
                message.exec_()

            

    def passwordMask(self, passwordBoxNumber):
        if passwordBoxNumber == 1:
            if self.eye_password.isChecked():
                self.password_entry.setEchoMode(QLineEdit.EchoMode.Normal)
            else:
                self.password_entry.setEchoMode(QLineEdit.EchoMode.Password)
        if passwordBoxNumber == 2:
            if self.eye_repassword.isChecked():
                self.repassword_entry.setEchoMode(QLineEdit.EchoMode.Normal)
            else:
                self.repassword_entry.setEchoMode(QLineEdit.EchoMode.Password)