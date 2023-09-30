#pyuic5 GUI_main.ui -o GUI_main.py
"""CREATE TABLE profiles (
    ID   INTEGER PRIMARY KEY AUTOINCREMENT,
    Name STRING,
    PGF  STRING,
    PSF  STRING
);
"""
#import lib
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QMessageBox
import sys
from GUI_main import Ui_Main
from DBM import DBM
db = DBM('Profiles.db')

app = QtWidgets.QApplication(sys.argv)
MAIN = QtWidgets.QMainWindow()
ui = Ui_Main()
ui.setupUi(MAIN)
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



def AddAllProfiles():
    global DBS
    if DBS == 0:
        check()
    else:
        ui.CMBox_Profile.addItems(list(map(str, db.GetProfilesName())))

def check():
    global DBS
    DBS = db.CheckConnect()
    ui.PRGRSBR_DBF.setValue(DBS)
    if DBS == 0:
        if msgBox.exec_() == QMessageBox.Yes:
            db.CreateDBProfiles()





AddAllProfiles()




ui.PSHBTN_Load.clicked.connect(AddAllProfiles)

sys.exit(app.exec_())