# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_Settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DLG_Settings(object):
    def setupUi(self, DLG_Settings):
        DLG_Settings.setObjectName("DLG_Settings")
        DLG_Settings.resize(520, 160)
        self.LBL = QtWidgets.QLabel(DLG_Settings)
        self.LBL.setGeometry(QtCore.QRect(10, 10, 81, 21))
        self.LBL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LBL.setObjectName("LBL")
        self.CBox_Language = QtWidgets.QComboBox(DLG_Settings)
        self.CBox_Language.setGeometry(QtCore.QRect(100, 10, 101, 22))
        self.CBox_Language.setObjectName("CBox_Language")
        self.CBox_Language.addItem("")
        self.CBox_Language.addItem("")
        self.LN = QtWidgets.QFrame(DLG_Settings)
        self.LN.setGeometry(QtCore.QRect(0, 30, 451, 21))
        self.LN.setLineWidth(2)
        self.LN.setFrameShape(QtWidgets.QFrame.HLine)
        self.LN.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LN.setObjectName("LN")
        self.LN_2 = QtWidgets.QFrame(DLG_Settings)
        self.LN_2.setGeometry(QtCore.QRect(200, 0, 21, 91))
        self.LN_2.setLineWidth(2)
        self.LN_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.LN_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LN_2.setObjectName("LN_2")
        self.LBL_2 = QtWidgets.QLabel(DLG_Settings)
        self.LBL_2.setGeometry(QtCore.QRect(10, 40, 191, 21))
        self.LBL_2.setAlignment(QtCore.Qt.AlignCenter)
        self.LBL_2.setObjectName("LBL_2")
        self.CBox_DP = QtWidgets.QComboBox(DLG_Settings)
        self.CBox_DP.setGeometry(QtCore.QRect(10, 60, 191, 22))
        self.CBox_DP.setObjectName("CBox_DP")
        self.CBox_DP.addItem("")
        self.CBox_DP.addItem("")
        self.PSHBTN_SaveSettings = QtWidgets.QPushButton(DLG_Settings)
        self.PSHBTN_SaveSettings.setGeometry(QtCore.QRect(220, 50, 211, 31))
        self.PSHBTN_SaveSettings.setObjectName("PSHBTN_SaveSettings")
        self.LBL_3 = QtWidgets.QLabel(DLG_Settings)
        self.LBL_3.setGeometry(QtCore.QRect(220, 10, 171, 21))
        self.LBL_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LBL_3.setObjectName("LBL_3")
        self.SPNBox_NMB = QtWidgets.QSpinBox(DLG_Settings)
        self.SPNBox_NMB.setGeometry(QtCore.QRect(400, 10, 41, 22))
        self.SPNBox_NMB.setReadOnly(False)
        self.SPNBox_NMB.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.SPNBox_NMB.setKeyboardTracking(False)
        self.SPNBox_NMB.setProperty("showGroupSeparator", False)
        self.SPNBox_NMB.setMinimum(1)
        self.SPNBox_NMB.setMaximum(10)
        self.SPNBox_NMB.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.SPNBox_NMB.setObjectName("SPNBox_NMB")
        self.LBL_4 = QtWidgets.QLabel(DLG_Settings)
        self.LBL_4.setGeometry(QtCore.QRect(10, 100, 171, 21))
        self.LBL_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LBL_4.setObjectName("LBL_4")
        self.LBL_5 = QtWidgets.QLabel(DLG_Settings)
        self.LBL_5.setGeometry(QtCore.QRect(10, 130, 171, 21))
        self.LBL_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LBL_5.setObjectName("LBL_5")
        self.LNEdit_GSF = QtWidgets.QLineEdit(DLG_Settings)
        self.LNEdit_GSF.setGeometry(QtCore.QRect(190, 100, 251, 20))
        self.LNEdit_GSF.setObjectName("LNEdit_GSF")
        self.LNEdit_BF = QtWidgets.QLineEdit(DLG_Settings)
        self.LNEdit_BF.setGeometry(QtCore.QRect(190, 130, 251, 20))
        self.LNEdit_BF.setObjectName("LNEdit_BF")
        self.PSHBTN_SGSF = QtWidgets.QPushButton(DLG_Settings)
        self.PSHBTN_SGSF.setGeometry(QtCore.QRect(450, 100, 61, 23))
        self.PSHBTN_SGSF.setObjectName("PSHBTN_SGSF")
        self.PSHBBTN_SBF = QtWidgets.QPushButton(DLG_Settings)
        self.PSHBBTN_SBF.setGeometry(QtCore.QRect(450, 130, 61, 23))
        self.PSHBBTN_SBF.setObjectName("PSHBBTN_SBF")
        self.LN_4 = QtWidgets.QFrame(DLG_Settings)
        self.LN_4.setGeometry(QtCore.QRect(0, 80, 521, 21))
        self.LN_4.setLineWidth(2)
        self.LN_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.LN_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LN_4.setObjectName("LN_4")
        self.LN_3 = QtWidgets.QFrame(DLG_Settings)
        self.LN_3.setGeometry(QtCore.QRect(440, 0, 21, 91))
        self.LN_3.setLineWidth(2)
        self.LN_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.LN_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LN_3.setObjectName("LN_3")
        self.LN.raise_()
        self.LBL.raise_()
        self.CBox_Language.raise_()
        self.LN_2.raise_()
        self.LBL_2.raise_()
        self.CBox_DP.raise_()
        self.PSHBTN_SaveSettings.raise_()
        self.LBL_3.raise_()
        self.SPNBox_NMB.raise_()
        self.LBL_4.raise_()
        self.LBL_5.raise_()
        self.LNEdit_GSF.raise_()
        self.LNEdit_BF.raise_()
        self.PSHBTN_SGSF.raise_()
        self.PSHBBTN_SBF.raise_()
        self.LN_3.raise_()
        self.LN_4.raise_()

        self.retranslateUi(DLG_Settings)
        QtCore.QMetaObject.connectSlotsByName(DLG_Settings)

    def retranslateUi(self, DLG_Settings):
        _translate = QtCore.QCoreApplication.translate
        DLG_Settings.setWindowTitle(_translate("DLG_Settings", "PZ-CMF_Settings"))
        self.LBL.setText(_translate("DLG_Settings", "Language:"))
        self.CBox_Language.setItemText(0, _translate("DLG_Settings", "EN"))
        self.CBox_Language.setItemText(1, _translate("DLG_Settings", "RU"))
        self.LBL_2.setText(_translate("DLG_Settings", "Display Profiles Name by:"))
        self.CBox_DP.setItemText(0, _translate("DLG_Settings", "Name"))
        self.CBox_DP.setItemText(1, _translate("DLG_Settings", "Folder"))
        self.PSHBTN_SaveSettings.setText(_translate("DLG_Settings", "Save Settings"))
        self.LBL_3.setText(_translate("DLG_Settings", "Number maximum buckups:"))
        self.LBL_4.setText(_translate("DLG_Settings", "Your Game Server Folder:"))
        self.LBL_5.setText(_translate("DLG_Settings", "Your Buckup Folder:"))
        self.PSHBTN_SGSF.setText(_translate("DLG_Settings", "Select"))
        self.PSHBBTN_SBF.setText(_translate("DLG_Settings", "Select"))
