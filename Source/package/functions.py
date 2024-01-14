import re
from .data import widget

def convert_date(date):
    date_spearated = date.split('/')
    date_final =  str()
    date_final+=(date_spearated[2])
    date_final+='-'
    if int(date_spearated[0])<10:
        date_final+='0'
    date_final+=(date_spearated[0])
    date_final+='-'
    if int(date_spearated[1])<10:
        date_final+='0'
    date_final+=(date_spearated[1])
    return date_final


    
def contains_only_alphabets(string):
    for char in string:
        if char == '-' or char == ' ' or char == '_' or char == ',':
            continue
        if not char.isalpha():
            return False
    return True

def is_numeric_string(input_string):
    try:
        float(input_string)  # Try converting the string to a float
        return True  # If successful, the string contains only numbers
    except ValueError:
        return False  # If ValueError occurs, the string does not contain only numbers

def is_valid_email(email):
    # Regular expression pattern for email validation
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    # Use the re.match() function to check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False
    
    
def back(self, shouldSave=False):
        widget.removeWidget(widget.currentWidget())
        if shouldSave:
            self.save()
