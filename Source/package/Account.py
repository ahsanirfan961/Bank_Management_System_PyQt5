from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from .functions import back
from .Personal_Info import Personal_Info
from . import data


class Account(QDialog):
    
    def __init__(self, accountOpened):
        super(Account, self).__init__()
        loadUi("UI/OpenAccount.ui", self)
        self.back.clicked.connect(back)
        self.forward.setEnabled(False)
        self.newAccountButton.clicked.connect(self.goto_personal)
        self.accountSettingButton.clicked.connect(self.goto_personal)
        
        if accountOpened:
            self.accountSettingButton.setEnabled(True)
            self.accountSettingButton.setStyleSheet('''color: rgb(124, 112, 255);
                                                    font: 87 16pt "Segoe UI Black";''')
            self.newAccountButton.setEnabled(False)
            self.newAccountButton.setStyleSheet('''color: rgb(181, 181, 181);
                                                font: 87 16pt "Segoe UI Black";''')
            data.CurrentAccountCreated = True
        else:
            self.accountSettingButton.setEnabled(False)
            self.accountSettingButton.setStyleSheet('''color: rgb(181, 181, 181);
                                                    font: 87 16pt "Segoe UI Black";''')
            self.newAccountButton.setEnabled(True)
            self.newAccountButton.setStyleSheet('''color: rgb(124, 112, 255);
                                                font: 87 16pt "Segoe UI Black";''')
            data.CurrentAccountCreated = False

    def goto_personal(self):
        if data.CurrentAccountCreated:
            values = data.sqlManager.getRow(self, 'Personal_Info', ['FirstName','SecondName','FatherName','MotherName','Gender','DOB','Married','Nationality','Education','Residence','Profession','Designation','CNIC','CNIC_issue','CNIC_expiry','BirthPlace'], ['User_ID', data.CurrentUserID])[0]
            FirstName = values[0]
            SecondName = values[1]
            FatherName = values[2]
            MotherName = values[3]
            Gender = values[4]
            DOB = values[5]
            Married = values[6]
            Nationality = values[7]
            Education = values[8]
            Residence = values[9]
            Profession = values[10]
            Designation = values[11]
            CNIC = values[12]
            CNIC_issue = values[13]
            CNIC_expiry = values[14]
            BirthPlace = values[15]
        else:
            FirstName = ''
            SecondName = ''
            FatherName = ''
            MotherName = ''
            Gender = ''
            DOB = ''
            Married = ''
            Nationality = ''
            Education = ''
            Residence = ''
            Profession = ''
            Designation = ''
            CNIC = ''
            CNIC_issue = ''
            CNIC_expiry = ''
            BirthPlace = ''
        personal = Personal_Info(FirstName,SecondName,FatherName,MotherName,Gender,DOB,Married,Nationality,Education,Residence,Profession,Designation,CNIC,CNIC_issue,CNIC_expiry,BirthPlace)
        
        data.widget.addWidget(personal)
        data.widget.setCurrentIndex(data.widget.currentIndex() + 1)