from PyQt5.QtWidgets import QApplication, QStackedWidget
import sys
from .SQL import SQLManager

# QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
# QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons


app = QApplication(sys.argv)

widget = QStackedWidget()

sqlManager = SQLManager()


Gender = (
    "Select",
    "Male",
    "Female",
    "Others"
)

Countries = (
    'Country'
    'Afghanistan',
    'Åland (Finland)',
    'Albania',
    'Algeria',
    'American Samoa (US)',
    'Andorra',
    'Angola',
    'Anguilla (BOT)',
    'Antigua and Barbuda',
    'Argentina',
    'Armenia',
    'Artsakh',
    'Aruba (Netherlands)',
    'Australia',
    'Austria',
    'Azerbaijan',
    'Bahamas',
    'Bahrain',
    'Bangladesh',
    'Barbados',
    'Belarus',
    'Belgium',
    'Belize',
    'Benin',
    'Bermuda (BOT)',
    'Bhutan',
    'Bolivia',
    'Bonaire (Netherlands)',
    'Bosnia and Herzegovina',
    'Botswana',
    'Brazil',
    'British Virgin Islands (BOT)',
    'Brunei',
    'Bulgaria',
    'Burkina Faso',
    'Burundi',
    'Cambodia',
    'Cameroon',
    'Canada',
    'Cape Verde',
    'Cayman Islands (BOT)',
    'Central African Republic',
    'Chad',
    'Chile',
    'China',
    'Christmas Island (Australia)',
    'Cocos (Keeling) Islands (Australia)',
    'Colombia',
    'Comoros',
    'Congo',
    'Cook Islands',
    'Costa Rica',
    'Croatia',
    'Cuba',
    'Curaçao (Netherlands)',
    'Cyprus',
    'Czech Republic',
    'Denmark',
    'Djibouti',
    'Dominica',
    'Dominican Republic',
    'DR Congo',
    'East Timor',
    'Ecuador',
    'Egypt',
    'El Salvador',
    'Equatorial Guinea',
    'Eritrea',
    'Estonia',
    'Eswatini',
    'Ethiopia',
    'Falkland Islands (BOT)',
    'Faroe Islands (Denmark)',
    'Fiji',
    'Finland',
    'France',
    'French Guiana (France)',
    'French Polynesia (France)',
    'Gabon',
    'Gambia',
    'Georgia',
    'Germany',
    'Ghana',
    'Gibraltar (BOT)',
    'Greece',
    'Greenland (Denmark)',
    'Grenada',
    'Guadeloupe (France)',
    'Guam (US)',
    'Guatemala',
    'Guernsey (Crown Dependency)',
    'Guinea',
    'Guinea-Bissau',
    'Guyana',
    'Haiti',
    'Honduras',
    'Hong Kong',
    'Hungary',
    'Iceland',
    'India',
    'Indonesia',
    'Iran',
    'Iraq',
    'Ireland',
    'Isle of Man (Crown Dependency)',
    'Israel',
    'Italy',
    'Ivory Coast',
    'Jamaica',
    'Japan',
    'Jersey (Crown Dependency)',
    'Jordan',
    'Kazakhstan',
    'Kenya',
    'Kiribati',
    'Kosovo',
    'Kuwait',
    'Kyrgyzstan',
    'Laos',
    'Latvia',
    'Lebanon',
    'Lesotho',
    'Liberia',
    'Libya',
    'Liechtenstein',
    'Lithuania',
    'Luxembourg',
    'Macau',
    'Madagascar',
    'Malawi',
    'Malaysia',
    'Maldives',
    'Mali',
    'Malta',
    'Marshall Islands',
    'Martinique (France)',
    'Mauritania',
    'Mauritius',
    'Mayotte (France)',
    'Mexico',
    'Micronesia',
    'Moldova',
    'Monaco',
    'Mongolia',
    'Montenegro',
    'Montserrat (BOT)',
    'Morocco',
    'Mozambique',
    'Myanmar',
    'Namibia',
    'Nauru',
    'Nepal',
    'Netherlands',
    'New Caledonia (France)',
    'New Zealand',
    'Nicaragua',
    'Niger',
    'Nigeria',
    'Niue',
    'Norfolk Island (Australia)',
    'North Korea',
    'North Macedonia',
    'Northern Cyprus',
    'Northern Mariana Islands (US)',
    'Norway',
    'Oman',
    'Pakistan',
    'Palau',
    'Palestine',
    'Panama',
    'Papua New Guinea',
    'Paraguay',
    'Peru',
    'Philippines',
    'Pitcairn Islands (BOT)',
    'Poland',
    'Portugal',
    'Puerto Rico (US)',
    'Qatar',
    'Réunion (France)',
    'Romania',
    'Russia',
    'Rwanda',
    'Saba (Netherlands)',
    'Saint Barthélemy (France)',
    'Saint Helena, Ascension and Tristan da Cunha (BOT)',
    'Saint Kitts and Nevis',
    'Saint Lucia',
    'Saint Martin (France)',
    'Saint Pierre and Miquelon (France)',
    'Saint Vincent and the Grenadines',
    'Samoa',
    'San Marino',
    'São Tomé and Príncipe',
    'Saudi Arabia',
    'Senegal',
    'Serbia',
    'Seychelles',
    'Sierra Leone',
    'Singapore',
    'Sint Eustatius (Netherlands)',
    'Sint Maarten (Netherlands)',
    'Slovakia',
    'Slovenia',
    'Solomon Islands',
    'Somalia',
    'South Africa',
    'South Korea',
    'South Sudan',
    'Spain',
    'Sri Lanka',
    'Sudan',
    'Suriname',
    'Svalbard and Jan Mayen (Norway)',
    'Sweden',
    'Switzerland',
    'Syria',
    'Taiwan',
    'Tajikistan',
    'Tanzania',
    'Thailand',
    'Togo',
    'Tokelau (NZ)',
    'Tonga',
    'Transnistria',
    'Trinidad and Tobago',
    'Tunisia',
    'Turkey',
    'Turkmenistan',
    'Turks and Caicos Islands (BOT)',
    'Tuvalu',
    'U.S. Virgin Islands (US)',
    'Uganda',
    'Ukraine',
    'United Arab Emirates',
    'United Kingdom',
    'United States',
    'Uruguay',
    'Uzbekistan',
    'Vanuatu',
    'Vatican City',
    'Venezuela',
    'Vietnam',
    'Wallis and Futuna (France)',
    'Western Sahara',
    'Yemen',
    'Zambia'
)

Marital_Status = (
    "Status",
    "Married",
    "UnMarried",
    "Others"
)

Profession = (
    "Job Title",
    "Govt Service",
    "Private Service",
    "House wife",
    "UnEmployed",
    "Agriculture",
    "Student",
    "Self Employed",
    "Others"
)

Education = ("Select", "No Education", "Below Matric", "Matric/O'Level", "Intermediate/A'Level", "Graduate", "Post Graduate", "Others")

Account_Types = (
    "Account Type"
    ,"Current Account"
    ,"Good Citizen Account"
    ,"Mukammal Current Account"
    ,"Business Partner Account "
    ,"Basic Banking Account"
    ,"E-Transiction Account"
    ,"Employe Banking Current Account"
    ,"Employe Banking Current Plus Account"
    ,"Urooj Account",
    "Mahana Amdani Saving Account",
    "Unisaver Plus Account",
    "First Minor Account",
    "Zindagi Account (for 60 & above)",
    "Employee Banking Saving  Account",
"Others")

Currency = (
    "Select",
    "PKR",
    "$ US Dollar",
    "Euro",
    "Pound",
    "UAE Dirham",
    "Saudi Riyal",
    "Chinese Yuan",
    "Others"
)

ExemptionType = (
    "Select",
    "Non-Muslim",
    "Foreigner",
    "Due to Fiqh",
    "Others"
)

CurrentUserID = 0
CurrentUserName=''
CurrentBalance = 0
CurrentAccountCreated = False
username = ''
fname = ''
lname = ''
fathername = ''
mname = ''
cnic = ''
designation = ''
DOB = ''
gender = ''
gender_index=0  
education =''
education_index=0
nationality = ''
nationality_index=0
profession =''
profession_index=0
cnic_issue =''
cnic_expiry=''
residence =''
residence_index=0
birthplace =''
birthplace_index=0
marital = ''
marital_index=0
country = ''
country_index=0
city = ''
paddress = ''
caddress = ''
phone = ''
mobile = ''
postalcode = ''
email = ''
password = ''
accounttype_index=0
currencytype_index=0
title = ''
Us1 = False
Us2 = False
Us3 = False
Us4 = False
zakat = False
zakatinfo=''
exemptiontype_index=0
Visa_Lock=0
Mastercard_Lock=0
Paypak_Lock=0
Card_Type=''
Cardtitle=''
T_PIN_check=False
T_PIN=''
checks=''
check1=''
check2=''
findaccount_id = ''

table = []