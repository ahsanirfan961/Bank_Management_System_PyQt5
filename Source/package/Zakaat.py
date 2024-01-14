from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi
from .functions import back, convert_date
from . import data

class Zakaat(QDialog):
    
    def __init__(self):
        super(Zakaat, self).__init__()
        loadUi("UI/Zakatdetails.ui", self)
        self.forward.setEnabled(False)
        self.back.clicked.connect(lambda: back(self, shouldSave=True))
        self.Save.clicked.connect(self.save)
        self.update()

    def validate(self):
        data.zakat = self.zakatBox.isChecked()
        exemptiontype = self.ComboBox.currentText()
        if data.zakat == True:
            if  exemptiontype == 'Select':
                messagebox = QMessageBox()
                messagebox.setText('Information not Correct')
                messagebox.setIcon(QMessageBox.Critical)
                messagebox.setWindowTitle('Error')
                messagebox.show()
                messagebox.exec_()
                return False
        return True  
        
    def save(self):

        # Inserting personal information
        
        data.sqlManager.insertRow(self, 'Personal_Info', ['User_ID', 'FirstName', 'SecondName', 'FatherName', 'MotherName', 'Gender', 'DOB', 'Married', 'Nationality', 'Education', 'Residence', 'Profession', 'Designation', 'CNIC', 'CNIC_issue', 'CNIC_expiry', 'BirthPlace', 'Balance'], [str(data.CurrentUserID), str(data.fname), str(data.lname), str(data.fathername), str(data.mname), str(data.gender_index), str(convert_date(data.DOB)), str(data.marital_index), str(data.nationality_index), str(data.education_index), str(data.residence_index), str(data.profession_index), str(data.designation),str(data.cnic), str(convert_date(data.cnic_issue)), str(convert_date(data.cnic_expiry)), str(data.birthplace_index), str(0)])
        
        # Inserting Contact Details
        
        data.sqlManager.insertRow(self, 'Contact', ['User_ID','Country','City','PAddress','CAddress','Postal_Code','Mobile','Phone','Email'], [str(data.CurrentUserID), str(data.country_index), str(data.city), str(data.paddress), str(data.caddress),str(data.postalcode), str(data.mobile), str(data.phone), str(data.email)])

        # Inserting account details
        
        data.sqlManager.insertRow(self, 'Account', ['User_ID','Type','Currency','Title','US_Nationality','US_Birth','US_Address','US_link'], [str(data.CurrentUserID),str(data.accounttype_index),str(data.currencytype_index),str(data.title),str(data.Us1),str(data.Us2),str(data.Us3),str(data.Us4)])

        #Saving Zakat Information

        data.zakat = self.zakatBox.isChecked()
        exemptiontype = self.ComboBox.currentText()
        data.exemptiontype_index=0
        for i in data.ExemptionType:
                if exemptiontype==i:
                    break
                data.exemptiontype_index = data.exemptiontype_index + 1
        data.zakatinfo= self.textEdit.text()

        if data.zakat == True:
            data.sqlManager.insertRow(self, 'Zakaat', ['User_ID','Zakat_Exemption','Exemption_type','AdditionalInfo'], [str(data.CurrentUserID),str(data.zakat),str( data.exemptiontype_index),str(data.zakatinfo)])
        else:
            data.sqlManager.insertRow(self, 'Zakaat', ['User_ID','Zakat_Exemption'], [str(data.CurrentUserID),str(data.zakat)])
        
        messagebox = QMessageBox()
        messagebox.setText('Successfully Saved\nLogin again to reflect changes!')
        messagebox.setIcon(QMessageBox.Information)
        messagebox.setWindowTitle('Saved')
        messagebox.show()
        messagebox.exec_()

        for x in range(0,4):
            while data.widget.currentIndex()!=0:
                data.widget.removeWidget(data.widget.currentWidget())
        
    def update(self):
        self.zakatBox.setChecked(data.zakat)
        self.ComboBox.setCurrentText(data.ExemptionType[data.exemptiontype_index])
        self.textEdit.setText(data.zakatinfo)
    