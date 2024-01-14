from package.Welcome import Welcome
import sys
from package.data import widget, app, sqlManager


welcome = Welcome() 
widget.addWidget(welcome)
widget.setFixedHeight(700)
widget.setFixedWidth(1200) 
widget.show()

try: 
    sys.exit(app.exec_())
except:
    sqlManager.cursor.close()
    print("Exiting")