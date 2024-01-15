from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi
from .functions import back, contains_only_alphabets, is_numeric_string
import datetime
from PyQt5 import QtCore
from .Contact import Contact
from . import data

class Personal_Info(QDialog):
    
    def __init__(self,FirstName,SecondName,FatherName,MotherName,Gender,DOB,Married,Nationality,Education,Residence,Profession,Designation,CNIC,CNIC_issue,CNIC_expiry,BirthPlace):
        super(Personal_Info, self).__init__()
        loadUi("UI/PersonalInformation.ui", self)
        self.back.clicked.connect(back)
        self.forward.clicked.connect(self.goto_contact)
        if FirstName != '':
            self.NameBox.setEnabled(False)
            self.SNameBox.setEnabled(False)
            self.FNameBox.setEnabled(False)
            self.MNameBox.setEnabled(False)
            self.DOBBox.setEnabled(False)
            self.CNICBox.setEnabled(False)
            self.GenderBox.setEnabled(False)
            self.BirthPlace.setEnabled(False)
            self.NameBox.setText(FirstName)
            self.SNameBox.setText(SecondName)
            self.FNameBox.setText(FatherName)
            self.MNameBox.setText(MotherName)
            self.CNICBox.setText(CNIC)
            self.DesignationBox.setText(Designation)
            self.DOBBox.setDate(QtCore.QDate.fromString(DOB, 'yyyy-MM-dd'))
            self.GenderBox.setCurrentText(data.Gender[int(Gender)])
            self.EducationBox.setCurrentText(data.Education[int(Education)])
            print(Nationality)
            self.NationalityBox.setCurrentText(data.Countries[int(Nationality)])
            self.ProfessionBox.setCurrentText(data.Profession[int(Profession)])
            self.CNICDOBBox.setDate(QtCore.QDate.fromString(CNIC_issue, 'yyyy-MM-dd'))
            self.CNICDOEBOX.setDate(QtCore.QDate.fromString(CNIC_expiry, 'yyyy-MM-dd'))
            self.ResCountryBox.setCurrentText(data.Countries[int(Residence)])
            self.BirthPlace.setCurrentText(data.Countries[int(BirthPlace)])
            self.MaritalBox.setCurrentText(data.Marital_Status[int(Married)])
    
        self.setTabOrder()
        
        

    
    def setTabOrder(self):
        self.NameBox.setTabOrder(self.NameBox, self.SNameBox)
        self.SNameBox.setTabOrder(self.SNameBox, self.FNameBox)
        self.FNameBox.setTabOrder(self.FNameBox, self.MNameBox)
        self.MNameBox.setTabOrder(self.MNameBox, self.DOBBox)
        self.DOBBox.setTabOrder(self.DOBBox, self.CNICBox)
        self.CNICBox.setTabOrder(self.CNICBox, self.GenderBox)
        self.GenderBox.setTabOrder(self.GenderBox, self.MaritalBox)
        self.MaritalBox.setTabOrder(self.MaritalBox, self.EducationBox)
        self.EducationBox.setTabOrder(self.EducationBox, self.BirthPlace)
        self.BirthPlace.setTabOrder(self.BirthPlace, self.NationalityBox)
        self.NationalityBox.setTabOrder(self.NationalityBox, self.ResCountryBox)
        self.ResCountryBox.setTabOrder(self.ResCountryBox, self.ProfessionBox)
        self.ProfessionBox.setTabOrder(self.ProfessionBox, self.DesignationBox)
        self.DesignationBox.setTabOrder(self.DesignationBox, self.CNICDOBBox)
        self.CNICDOBBox.setTabOrder(self.CNICDOBBox, self.CNICDOEBOX)

    def validate(self):
        data.fname = self.NameBox.text()
        data.lname = self.SNameBox.text()
        data.fathername = self.FNameBox.text()
        data.mname = self.MNameBox.text()
        data.cnic = self.CNICBox.text()
        data.designation = self.DesignationBox.text()
        data.DOB = self.DOBBox.text()
        DOB_separated = data.DOB.split('/')
        data.gender = self.GenderBox.currentText()
        data.education = self.EducationBox.currentText()
        data.nationality = self.NationalityBox.currentText()
        data.profession = self.ProfessionBox.currentText()
        data.cnic_issue = self.CNICDOBBox.text()
        data.cnic_expiry = self.CNICDOEBOX.text()
        data.residence = self.ResCountryBox.currentText()
        data.birthplace = self.BirthPlace.currentText()
        data.marital = self.MaritalBox.currentText()
        
        currentDate = str(datetime.date.today())
        currentDateSep = currentDate.split('-')
        
        if data.fname == '' or data.lname == '' or data.fathername == '' or data.mname == '' or data.cnic == '' or data.designation == '' or data.gender == 'Gender' or data.education == 'Education' or data.nationality == 'Nationality' or data.profession == 'Job Title' or data.residence == 'Country' or data.birthplace == 'Place' or data.marital == 'Status':
            self.error.setText('All fields required!')
            return False
        else:
            self.error.setText('')
        
        if contains_only_alphabets(data.fname):
            self.error.setText("")
        else:
            self.error.setText("Invalid First Name!")
            return False
        
        if contains_only_alphabets(data.lname):
            self.error.setText("")
        else:
            self.error.setText("Invalid Last Name!")
            return False
        
        if contains_only_alphabets(data.fathername):
            self.error.setText("")
        else:
            self.error.setText("Invalid Father Name!")
            return False

        if contains_only_alphabets(data.mname):
            self.error.setText("")
        else:
            self.error.setText("Invalid Mother Name!")
            return False
        
        if contains_only_alphabets(data.designation):
            self.error.setText("")
        else:
            self.error.setText("Invalid Designation!")
            return False
        
        if len(data.cnic) != 13 and not is_numeric_string(data.cnic):
            self.error.setText("Invalid CNIC")
            return False
        else:
            self.error.setText("")
        
        if int(currentDateSep[0])-int(DOB_separated[2])>=18:
            if int(currentDateSep[0])-int(DOB_separated[2])==18:
                if int(currentDateSep[1])>= int(DOB_separated[0]):
                    if int(currentDateSep[2])>= int(DOB_separated[1]):
                        self.error.setText("")
                    else:
                         self.error.setText("Account holder must be at least 18 years old!")
                         return False
                else:
                    self.error.setText("Account holder must be at least 18 years old!")   
                    return False
        else:
            self.error.setText("Account holder must be at least 18 years old!")
            return False
        
        return True

    def goto_contact(self):
        if not self.validate():
            messageBox = QMessageBox()
            messageBox.setText("Information is not correct!")
            messageBox.setIcon(QMessageBox.Critical)
            messageBox.show()
            messageBox.exec_()
            return False
        else:
            self.save()
            if data.CurrentAccountCreated:
                values = data.sqlManager.getRow(self, 'Contact', ['City','PAddress','CAddress','Postal_Code','Mobile','Phone','Email'], ['User_ID', data.CurrentUserID])[0]
                City = values[0]
                PAddress = values[1]
                CAddress = values[2]
                Postal_Code = values[3]
                Mobile = values[4]
                Phone = values[5]
                Email = values[6]
            else:
                City = ''
                PAddress = ''
                CAddress = ''
                Postal_Code = ''
                Mobile = ''
                Phone = ''
                Email = ''
            contact = Contact(City,PAddress,CAddress,Postal_Code,Mobile,Phone,Email)
            data.widget.addWidget(contact)
            data.widget.setCurrentIndex(data.widget.currentIndex() + 1)

    def save(self):
                
        if True:
            data.fname = self.NameBox.text()
            data.lname = self.SNameBox.text()
            data.fathername = self.FNameBox.text()
            data.mname = self.MNameBox.text()
            data.cnic = self.CNICBox.text()
            data.designation = self.DesignationBox.text()
            data.DOB = self.DOBBox.text()
            data.gender = self.GenderBox.currentText()
            data.gender_index=0
            for i in data.Gender:
                if data.gender==i:
                    break     
                data.gender_index = data.gender_index + 1
                
            data.education = self.EducationBox.currentText()
            data.education_index=0
            for i in data.Education:
                if data.education==i: 
                    break
                data.education_index = data.education_index + 1
                
            data.nationality = self.NationalityBox.currentText()
            data.nationality_index=0
            for i in data.Countries:
                if data.nationality==i:
                    break
                data.nationality_index = data.nationality_index + 1
                
            data.profession = self.ProfessionBox.currentText()
            data.profession_index=0
            for i in data.Profession:
                if data.profession==i:
                    break
                data.profession_index = data.profession_index + 1
                
            data.cnic_issue = self.CNICDOBBox.text()
            data.cnic_expiry = self.CNICDOEBOX.text()
            
            data.residence = self.ResCountryBox.currentText()
            data.residence_index=0
            for i in data.Countries:
                if data.residence==i:
                    break
                data.residence_index = data.residence_index + 1
                 
            data.birthplace = self.BirthPlace.currentText()
            data.birthplace_index=0
            for i in data.Countries:
                if data.birthplace==i:
                    break
                data.birthplace_index = data.birthplace_index + 1
                
            data.marital = self.MaritalBox.currentText()
            data.marital_index=0
            for i in data.Marital_Status:
                if data.marital==i:
                    break
                data.marital_index = data.marital_index + 1