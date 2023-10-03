#pyuic5 GUI_main.ui -o GUI_main.py
#pyuic5 GUI_create.ui -o GUI_create.py
#import lib
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QMessageBox
import sys
from GUI_main import Ui_Main
from GUI_create import Ui_DLG_Create
from DBM import DBM
db = DBM('Profiles.db')

app = QtWidgets.QApplication(sys.argv)
MAIN = QtWidgets.QMainWindow()
CRT = QtWidgets.QDialog()
ui_main = Ui_Main()
ui_CRT = Ui_DLG_Create()
ui_main.setupUi(MAIN)
ui_CRT.setupUi(CRT)
MAIN.show()




#MessageBox init
msg = QMessageBox()
msg.setIcon(QMessageBox.Critical)
msg.setText("Error")
msg.setInformativeText("LOL")
msg.setWindowTitle("Error")
msg.setStandardButtons(QMessageBox.Ok)

msgBox = QMessageBox()
msgBox.setText("You want create DB or Config file?")
msgBox.setWindowTitle("PZ-CMF")
msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
msgBox.setDefaultButton(QMessageBox.No)
msgBox.setEscapeButton(QMessageBox.No)

DBS = 0
CFS = 0
OFS = 0



def LoadAllProfiles():
    global DBS
    if DBS == 0:
        check()
    else:
        try:
            ui_main.CMBox_Profile.clear()
        except:
            pass
        ui_main.CMBox_Profile.addItems(list(map(str, db.GetProfilesName())))
        
def CeateProfileUI():
    MAIN.setEnabled(0)
    CRT.exec()
    MAIN.setEnabled(1)
    
def CreateDBFile():
    db.CreateDBProfiles()

def check():
    global DBS
    global CFS
    global OFS
    DBS = db.CheckConnect()
    ui_main.PRGRSBR_DBF.setValue(DBS)
    if DBS == 0:
        if msgBox.exec_() == QMessageBox.Yes:
            db.CreateDBProfiles()









ui_main.PSHBTN_Create.clicked.connect(CeateProfileUI)
ui_main.PSHBTN_Load.clicked.connect(LoadAllProfiles)
ui_main.ACT_CreateDBF.changed.connect(CreateDBFile)
check()
LoadAllProfiles()
sys.exit(app.exec_())