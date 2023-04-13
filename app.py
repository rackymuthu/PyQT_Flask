import sys
from PyQt5 import *
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication

PORT = 5000
ROOT_URL = 'http://localhost:{}'.format(PORT)
db = QSqlDatabase("QPSQL")
if not db.open():
    print("Unable to connect.")
    print('Last error', db.lastError().text())
else:
    print("Connection to the database successful")

class Window(QThread):

    def __init__(self):
        super(Window, self).__init__()
 
        self.setWindowTitle("Python Demo")
        self.setGeometry(100, 100, 300, 400)
        
        self.formGroupBox = QGroupBox("Form 1")
        self.notification_title = QLineEdit()
        self.notification_text = QLineEdit()
        self.notification_name = QLineEdit()
        self.createForm()
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonBox.accepted.connect(self.getInfo)
        self.buttonBox.rejected.connect(self.reject)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(self.buttonBox)
        
        mainLayout.addWidget(self.notification_name)
        mainLayout.addStretch()
        mainLayout.addWidget(self.notification_title)
        mainLayout.addStretch()
        mainLayout.addWidget(self.notification_text)
        mainLayout.addStretch()
        self.setLayout(mainLayout)


    def run(self):
        self.application.run(port=PORT)

def createGuiFor(application):
    qtapp = QApplication(sys.argv)
    webapp = Window(application)
    webapp.start()
    qtapp.aboutToQuit.connect(webapp.terminate)
    webview = QFormLayout()
    webview.load(QUrl(ROOT_URL))
    webview.show()
    webview.setWindowTitle("MyApp")
    webview.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
    return qtapp.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.exit(app.exec_())
    sys.exit(createGuiFor(app))