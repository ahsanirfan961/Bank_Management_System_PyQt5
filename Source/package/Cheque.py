from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi
from . import data
from .functions import back

class Cheque(QDialog):
    def __init__(self):
        super(Cheque, self).__init__()
        loadUi("UI/ChequeBook.ui", self)
        self.forward.setEnabled(False)
        self.back.clicked.connect(back)
        self.Save.clicked.connect(self.validate)
        self.YesBox.clicked.connect(self.validate)
        self.NoBox.clicked.connect(self.validate)
        self.Save.clicked.connect(self.save)
    
    def validate(self):
        yes = self.YesBox.isChecked()
        no = self.NoBox.isChecked()
        n_checkbooks = self.checkBooks.value()
        checks = self.checks.currentText()
            
        
        if yes == False and no == False:
            self.error.setText("Please select \'Yes\' or \'No\'!")
            return False
        else:
            self.error.setText("")
        
        if yes == True and no == True:
            self.YesBox.setChecked(False)
            self.NoBox.setChecked(False)
            
        if no == True:
            self.checkBooks.setEnabled(False)
            self.checks.setEnabled(False)
            self.specialInstructions.setEnabled(False)
            self.standingInstructions.setEnabled(False)
            self.Save.setEnabled(False)
        if yes == True:
            self.checkBooks.setEnabled(True)
            self.checks.setEnabled(True)
            self.specialInstructions.setEnabled(True)
            self.standingInstructions.setEnabled(True)   
            self.Save.setEnabled(True)
            
        special1 = self.specialInstructions.text()
        special2 = self.standingInstructions.text()
        
        if special1 == "" or special2 =="":
            self.error.setText("Write None in instructions, if none!")
            return False
        
        return True
    
    def save(self):
    
        if self.validate():
            yes = self.YesBox.isChecked()
            no = self.NoBox.isChecked()
            n_checkbooks = self.checkBooks.value()
            checks = self.checks.currentText()
            special1 = self.specialInstructions.text()
            special2 = self.standingInstructions.text()

            data.sqlManager.insertRow(self, 'Cheque',['User_ID',' No_of_Chequebook',' checks',' Special1',' Special2'], [str(data.CurrentUserID), str(n_checkbooks), checks, special1, special2])

            messagebox = QMessageBox()
            messagebox.setText('Successfully Ordered!')
            messagebox.setIcon(QMessageBox.Information)
            messagebox.setWindowTitle('Saved')
            messagebox.show()
            messagebox.exec_()
