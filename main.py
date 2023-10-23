#pyuic5 GUI_main.ui -o GUI_main.py
#pyuic5 GUI_create.ui -o GUI_create.py
#pyuic5 GUI_Settings.ui -o GUI_settings.py
#import lib
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QMessageBox
import sys
from GUI_main import Ui_Main
from GUI_create import Ui_DLG_Create
from GUI_settings import Ui_DLG_Settings
from DBM import DBM
from CFM import CFM
db = DBM('Profiles.db')
CF = CFM('CFG.cfg')

app = QtWidgets.QApplication(sys.argv)
MAIN = QtWidgets.QMainWindow()
CRT = QtWidgets.QDialog()
STN = QtWidgets.QDialog()
ui_main = Ui_Main()
ui_CRT = Ui_DLG_Create()
ui_STN = Ui_DLG_Settings()
ui_main.setupUi(MAIN)
ui_CRT.setupUi(CRT)
ui_STN.setupUi(STN)
MAIN.show()




#MessageBox init
msgBox = QMessageBox()
msgBox.setText("You really want???")
msgBox.setWindowTitle("PZ-CMF")
msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

DBS = 0




def LoadAllProfiles():
    global DBS
    if DBS == 0:
        check()
    else:
        ui_main.CMBox_Profile.clear()
        ui_main.CMBox_Profile.addItems(list(map(str, db.GetProfilesName("NP"))))
    
def CreateDBFile():
    try:
        db.CreateDBProfiles()
        msgBox.setText("Successful create DataBase File!")
        msgBox.exec()
    except:
        msgBox.setText("Error when creating Database File!!!")
        msgBox.exec()

def Settings():
    STNList = db.GetSettings()
    print(STNList)
    ui_STN.CBox_Language.setCurrentText(str(STNList[0]))
    ui_STN.LNEdit_GSF.setText(str(STNList[1]))
    ui_STN.LNEdit_BF.setText(str(STNList[2]))
    STN.exec()

def check():
    global DBS
    DBS = db.CheckConnect()
    ui_main.PRGRSBR_DBF.setValue(DBS)
    if DBS == 0:
        db.CreateDBFile()

def DeleteProfile():
    ret = msgBox.exec_()
    if ret == QMessageBox.No:
        pass
    elif ret == QMessageBox.Yes:
        db.DeleteProfile(ui_main.CMBox_Profile.currentText(), "NP")
        LoadAllProfiles()

def SaveProfile():
    try:
        if ui_CRT.LNEdit_PN.displayText() != "" and ui_CRT.LNEdit_NSF.displayText() != "":
            db.CreateProfile(ui_CRT.LNEdit_PN.displayText(), ui_CRT.LNEdit_NSF.displayText())
        ui_CRT.LNEdit_PN.clear()
        ui_CRT.LNEdit_NSF.clear()
        LoadAllProfiles()
    except:
        msgBox.setText("Error when save profile!!!")
        msgBox.exec()

def SaveSettings():
    db.SaveSettings(ui_STN.CBox_Language.currentText(), ui_STN.LNEdit_GSF.displayText(), ui_STN.LNEdit_BF.displayText())
    
    

ui_STN.PSHBTN_SaveSettings.clicked.connect(SaveSettings)
ui_main.PSHBTN_Delete.clicked.connect(DeleteProfile)
ui_CRT.BTNBOX.accepted.connect(SaveProfile)
ui_STN.PSHBTN_SGSF.clicked.connect(lambda: ui_STN.LNEdit_GSF.setText(QtWidgets.QFileDialog.getExistingDirectory()))
ui_STN.PSHBBTN_SBF.clicked.connect(lambda: ui_STN.LNEdit_BF.setText(QtWidgets.QFileDialog.getExistingDirectory()))
ui_main.PSHBTN_Create.clicked.connect(CRT.exec)
ui_main.PSHBTN_Load.clicked.connect(LoadAllProfiles)
ui_main.PSHBTN_Settings.clicked.connect(Settings)
#ui_main.ACT_CreateDBF.changed.connect(CreateDBFile)
check()
LoadAllProfiles()
sys.exit(app.exec_())