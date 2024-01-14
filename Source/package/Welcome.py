from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from . import data
from .SignUp import SignUp
from .SignIn import SignIn

# Welcome
class Welcome(QDialog):
    
    def __init__(self):
        super(Welcome, self).__init__()
        loadUi("UI/Welcome page.ui", self)
        self.createnew.clicked.connect(self.goto_signup)
        self.loginbutton.clicked.connect(self.goto_signin)
         
    def goto_signup(self):
        signup = SignUp()
        data.widget.addWidget(signup)
        data.widget.setCurrentIndex(data.widget.currentIndex() + 1)

    def goto_signin(self):
        signin = SignIn()
        data.widget.addWidget(signin)
        data.widget.setCurrentIndex(data.widget.currentIndex() + 1)

