#pyuic5 GUI_main.ui -o GUI_main.py
#import lib
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread
import sys
from GUI_main import Ui_main

app = QtWidgets.QApplication(sys.argv)
STRT = QtWidgets.QMainWindow()
ui = Ui_main()
ui.setupUi(STRT)
STRT.show()








sys.exit(app.exec_())