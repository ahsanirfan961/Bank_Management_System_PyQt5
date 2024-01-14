from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi
from .data import Countries
from .functions import back, is_numeric_string, is_valid_email, convert_date
from .Account_Open import Account_Open
from . import data

class Contact(QDialog):
    
    def __init__(self,City,PAddress,CAddress,Postal_Code,Mobile,Phone,Email):
        super(Contact, self).__init__()
        loadUi("UI/contact.ui", self)
        self.back.clicked.connect(lambda: back(self, shouldSave=True))
        self.forward.clicked.connect(self.goto_account_open)
        if data.CurrentAccountCreated:
            self.paddress_entry.setEnabled(False)
            self.countryBox.setEnabled(False)
            self.forward.setEnabled(False)
            self.dhoka.setGeometry(0,0,0,0)
            self.phone_entry.setText(Phone)
            self.mobile_entry.setText(Mobile)
            self.email_entry.setText(Email)
            self.paddress_entry.setText(PAddress)
            self.caddress_entry.setText(CAddress)
            self.postalcode_entry.setText(Postal_Code)
            self.city_entry.setText(City)
        else:
            self.phone_entry.setText(data.phone)
            self.mobile_entry.setText(data.mobile)
            self.email_entry.setText(data.email)
            self.paddress_entry.setText(data.paddress)
            self.caddress_entry.setText(data.caddress)
            self.postalcode_entry.setText(data.postalcode)
            self.city_entry.setText(data.city)
        self.Save.clicked.connect(lambda: self.save(update=True))

    def validate(self):
        data.phone = self.phone_entry.text()
        data.mobile = self.mobile_entry.text()
        data.email = self.email_entry.text()
        permenant_address = self.paddress_entry.text()
        current_address = self.caddress_entry.text()
        data.postalcode = self.postalcode_entry.text()
        data.city = self.city_entry.text()
        data.country = self.countryBox.currentText()
        
        if data.phone == '' or data.mobile == '' or data.email == '' or permenant_address == '' or current_address == '' or data.postalcode == '' or data.city == '' or data.country == 'Country':
            self.error.setText('All field required!')
            return False
        else:
            self.error.setText('')
            
        if is_numeric_string(data.phone) and len(data.phone)==10:
            self.error.setText("")
        else:
            self.error.setText("Invalid data.phone number!")
            return False
        
        if is_numeric_string(data.mobile)and (len(data.mobile)==11 or len(data.mobile)==13):
            self.error.setText("")
        else:
            self.error.setText("Invalid data.mobile number!")
            return False
        
        if is_numeric_string(data.postalcode):
            self.error.setText("")
        else:
            self.error.setText("Invalid postal code!")
            return False
        
        if is_valid_email(data.email):
            self.error.setText("")
        else:
            self.error.setText("Invalid data.email address!")
            return False
        
        return True
        
    def goto_account_open(self):
        if not self.validate():
            messageBox = QMessageBox()
            messageBox.setText("Information is not correct!")
            messageBox.setIcon(QMessageBox.Critical)
            messageBox.show()
            messageBox.exec_()
            return False
        else:
            self.save()
            account_open = Account_Open()
            data.widget.addWidget(account_open)
            data.widget.setCurrentIndex(data.widget.currentIndex() + 1)

    def save(self, update=False): 
        data.country = self.countryBox.currentText()
        data.country_index=0
        for i in Countries:
                if data.country==i:
                    break   
                data.country_index = data.country_index + 1  
        data.city = self.city_entry.text()
        data.paddress = self.paddress_entry.text()
        data.caddress = self.caddress_entry.text()
        data.phone = self.phone_entry.text()
        data.mobile=self.mobile_entry.text()
        data.postalcode = self.postalcode_entry.text()
        data.email = self.email_entry.text()
        
        if update:
             
            data.sqlManager.updateRow(self, 'Personal_Info',['Education','Nationality','Profession','Residence','Married','Designation  ','CNIC_issue','CNIC_expiry'], [data.education_index,data.nationality_index,data.profession_index,data.residence_index,data.marital_index,data.designation ,convert_date(data.cnic_issue) ,convert_date(data.cnic_expiry)],['User_ID', data.CurrentUserID])
            
            data.sqlManager.updateRow(self, 'Contact', ['City', 'CAddress', 'Postal_Code', 'Mobile', 'Phone', 'Email'], [data.city, data.caddress, data.postalcode, data.mobile, data.phone, data.email], ['user_ID', data.CurrentUserID])
            
            messageBox = QMessageBox()
            messageBox.setText("Saved Succesfully!")
            messageBox.setIcon(QMessageBox.Information)
            messageBox.show()
            messageBox.exec_()
            for i in range(0,2):
                data.widget.removeWidget(data.widget.currentWidget())
                       
        
