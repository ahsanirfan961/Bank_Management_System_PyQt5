from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi
from .functions import back
from . import data

class Profile_Settings(QDialog):
    
    def __init__(self, firstName, lastName, username, mobile):
        super(Profile_Settings, self).__init__()
        loadUi("UI/Profile.ui", self)
        self.back.clicked.connect(back)
        self.Save.clicked.connect(self.save)
        self.update_password.clicked.connect(self.updatePassword)
        self.fname_entry.setTabOrder(self.fname_entry, self.lname_entry)
        self.lname_entry.setTabOrder(self.lname_entry, self.username_entry)
        self.username_entry.setTabOrder(self.username_entry, self.mobile_entry)
        self.mobile_entry.setTabOrder(self.mobile_entry, self.Save)
        self.Save.setTabOrder(self.Save, self.oldpassword_entry)
        self.oldpassword_entry.setTabOrder(self.oldpassword_entry, self.password_entry)
        self.password_entry.setTabOrder(self.password_entry, self.repassword_entry)
        self.repassword_entry.setTabOrder(self.repassword_entry, self.update_password)
        self.fname_entry.setText(firstName)
        self.lname_entry.setText(lastName)
        self.username_entry.setText(username)
        self.mobile_entry.setText(str(mobile))
             
    def save(self):

        fname = self.fname_entry.text()
        lname = self.lname_entry.text()
        username = self.username_entry.text()
        mobile = self.mobile_entry.text()
        
        if data.sqlManager.updateRow(self, 'Application_User', ['First_Name', 'Last_Name', 'Email'], [fname, lname, username], ['ID', data.CurrentUserID]) and data.sqlManager.updateRow(self, 'Contact', ['Mobile'], [mobile], ['ID', data.CurrentUserID]):
            messageBox = QMessageBox()
            messageBox.setText("Saved Successfully!\nLogin again to reflect change!")
            messageBox.setIcon(QMessageBox.Information)
            messageBox.show()
            messageBox.exec_()
        else:
            messageBox = QMessageBox()
            messageBox.setText("Couldn't update account informaation at this time!\nPlease try agian later")
            messageBox.setIcon(QMessageBox.Critical)
            messageBox.show()
            messageBox.exec_()
        
    def updatePassword(self):

        oldPassword = self.oldpassword_entry.text()
        newPassword = self.password_entry.text()
        repassword = self.repassword_entry.text()
        
        if oldPassword == data.sqlManager.getRow(self, 'Application_User', ['Password'], ['ID', data.CurrentUserID])[0][0]:
            self.error.setText("")
            if newPassword == repassword and newPassword!='':
                self.error.setText("")
                if data.sqlManager.updateRow(self, 'Application_User', ['Password'], [newPassword], ['ID', data.CurrentUserID]):
                    messageBox = QMessageBox()
                    messageBox.setText("Saved Successfully!\nLog in again to reflect changes!")
                    messageBox.setWindowTitle('Password Update Information')
                    messageBox.setIcon(QMessageBox.Information)
                    messageBox.show()
                    messageBox.exec_()
                else:
                    messageBox = QMessageBox()
                    messageBox.setText("Couldn't change password at this time!\nPlease try again later")
                    messageBox.setWindowTitle('Password Update Information')
                    messageBox.setIcon(QMessageBox.Critical)
                    messageBox.show()
                    messageBox.exec_()
            elif newPassword=='':
                    self.error.setText("Please enter new data.password")
            else:
                self.error.setText("New passwords don't match!")
        else:
            self.error.setText("Old data.password not correct!")