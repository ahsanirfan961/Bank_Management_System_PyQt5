from package.Welcome import Welcome
import sys 
from package.data import widget, app, sqlManager
from PyQt5.QtGui import QIcon


welcome = Welcome() 
widget.addWidget(welcome)
widget.setFixedHeight(700)
widget.setFixedWidth(1200) 
widget.setWindowIcon(QIcon('Images/Logo.png'))
widget.show()

try: 
    sys.exit(app.exec_())
except:
    sqlManager.cursor.close()
    print("Exiting")