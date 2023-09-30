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
import sys
from GUI_main import Ui_Main

app = QtWidgets.QApplication(sys.argv)
MAIN = QtWidgets.QMainWindow()
ui = Ui_Main()
ui.setupUi(MAIN)
MAIN.show()








sys.exit(app.exec_())