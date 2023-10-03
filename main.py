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
msgBox = QMessageBox()
msgBox.setText("You really want???")
msgBox.setWindowTitle("PZ-CMF")
msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

DBS = 0
CFS = 0
OFS = 0



def LoadAllProfiles():
    global DBS
    if DBS == 0:
        check()
    else:
        ui_main.CMBox_Profile.clear()
        ui_main.CMBox_Profile.addItems(list(map(str, db.GetProfilesName(1))))
    
def CreateDBFile():
    try:
        db.CreateDBProfiles()
        msgBox.setText("Successful create DataBase File!")
        msgBox.exec()
    except:
        msgBox.setText("Error when creating Database File!!!")
        msgBox.exec()

def check():
    global DBS
    global CFS
    global OFS
    DBS = db.CheckConnect()
    ui_main.PRGRSBR_DBF.setValue(DBS)
    if DBS == 0:
        db.CreateDBProfiles()

def DeleteProfile():
    ret = msgBox.exec_()
    if ret == QMessageBox.No:
        pass
    elif ret == QMessageBox.Yes:
        db.DeleteProfile(ui_main.CMBox_Profile.currentText())
        LoadAllProfiles()

def SaveProfile():
    try:
        if ui_CRT.LNEdit_PN.displayText() != "" and ui_CRT.LNEdit_PTYG.displayText != "" and ui_CRT.LNEdit_PTYSG.displayText() != "":
            db.CreateProfile(ui_CRT.LNEdit_PN.displayText(), ui_CRT.LNEdit_PTYG.displayText(), ui_CRT.LNEdit_PTYSG.displayText())
            msgBox.setText("Successful Save!")
            msgBox.exec()
        ui_CRT.LNEdit_PN.clear()
        ui_CRT.LNEdit_PTYG.clear()
        ui_CRT.LNEdit_PTYSG.clear()
        LoadAllProfiles()
    except:
        msgBox.setText("Error when save profile!!!")
        msgBox.exec()



ui_main.PSHBTN_Delete.clicked.connect(DeleteProfile)
ui_CRT.BTNBOX.accepted.connect(SaveProfile)
ui_CRT.PSHBTN_SYSG.clicked.connect(lambda: ui_CRT.LNEdit_PTYSG.setText(QtWidgets.QFileDialog.getExistingDirectory()))
ui_CRT.PSHBTN_SYG.clicked.connect(lambda: ui_CRT.LNEdit_PTYG.setText(QtWidgets.QFileDialog.getExistingDirectory()))
ui_main.PSHBTN_Create.clicked.connect(CRT.exec)
ui_main.PSHBTN_Load.clicked.connect(LoadAllProfiles)
ui_main.ACT_CreateDBF.changed.connect(CreateDBFile)
check()
LoadAllProfiles()
sys.exit(app.exec_())