# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_create.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DLG_Create(object):
    def setupUi(self, DLG_Create):
        DLG_Create.setObjectName("DLG_Create")
        DLG_Create.resize(570, 130)
        self.BTNBOX = QtWidgets.QDialogButtonBox(DLG_Create)
        self.BTNBOX.setGeometry(QtCore.QRect(440, 0, 121, 71))
        self.BTNBOX.setOrientation(QtCore.Qt.Vertical)
        self.BTNBOX.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.BTNBOX.setCenterButtons(True)
        self.BTNBOX.setObjectName("BTNBOX")
        self.LBL = QtWidgets.QLabel(DLG_Create)
        self.LBL.setGeometry(QtCore.QRect(10, 10, 161, 21))
        self.LBL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LBL.setObjectName("LBL")
        self.LNEdit_PN = QtWidgets.QLineEdit(DLG_Create)
        self.LNEdit_PN.setGeometry(QtCore.QRect(180, 10, 251, 20))
        self.LNEdit_PN.setObjectName("LNEdit_PN")
        self.LBL_3 = QtWidgets.QLabel(DLG_Create)
        self.LBL_3.setGeometry(QtCore.QRect(10, 100, 161, 21))
        self.LBL_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LBL_3.setObjectName("LBL_3")
        self.LBL_2 = QtWidgets.QLabel(DLG_Create)
        self.LBL_2.setGeometry(QtCore.QRect(10, 70, 161, 21))
        self.LBL_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LBL_2.setObjectName("LBL_2")
        self.LNEdit_PTYG = QtWidgets.QLineEdit(DLG_Create)
        self.LNEdit_PTYG.setGeometry(QtCore.QRect(180, 100, 251, 20))
        self.LNEdit_PTYG.setReadOnly(True)
        self.LNEdit_PTYG.setObjectName("LNEdit_PTYG")
        self.LNEdit_PTYSG = QtWidgets.QLineEdit(DLG_Create)
        self.LNEdit_PTYSG.setGeometry(QtCore.QRect(180, 70, 251, 20))
        self.LNEdit_PTYSG.setFrame(True)
        self.LNEdit_PTYSG.setReadOnly(True)
        self.LNEdit_PTYSG.setObjectName("LNEdit_PTYSG")
        self.PSHBTN_SYSG = QtWidgets.QPushButton(DLG_Create)
        self.PSHBTN_SYSG.setGeometry(QtCore.QRect(440, 70, 71, 23))
        self.PSHBTN_SYSG.setObjectName("PSHBTN_SYSG")
        self.PSHBTN_SYG = QtWidgets.QPushButton(DLG_Create)
        self.PSHBTN_SYG.setGeometry(QtCore.QRect(440, 100, 71, 23))
        self.PSHBTN_SYG.setObjectName("PSHBTN_SYG")
        self.LBL_4 = QtWidgets.QLabel(DLG_Create)
        self.LBL_4.setGeometry(QtCore.QRect(10, 40, 161, 21))
        self.LBL_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LBL_4.setObjectName("LBL_4")
        self.LNEdit_NSF = QtWidgets.QLineEdit(DLG_Create)
        self.LNEdit_NSF.setGeometry(QtCore.QRect(180, 40, 251, 20))
        self.LNEdit_NSF.setReadOnly(False)
        self.LNEdit_NSF.setObjectName("LNEdit_NSF")

        self.retranslateUi(DLG_Create)
        self.BTNBOX.accepted.connect(DLG_Create.accept) # type: ignore
        self.BTNBOX.rejected.connect(DLG_Create.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(DLG_Create)

    def retranslateUi(self, DLG_Create):
        _translate = QtCore.QCoreApplication.translate
        DLG_Create.setWindowTitle(_translate("DLG_Create", "PZ-CMF_Create"))
        self.LBL.setText(_translate("DLG_Create", "Profile name:"))
        self.LBL_3.setText(_translate("DLG_Create", "Patch to your game:"))
        self.LBL_2.setText(_translate("DLG_Create", "Patch to your save game:"))
        self.PSHBTN_SYSG.setText(_translate("DLG_Create", "Select"))
        self.PSHBTN_SYG.setText(_translate("DLG_Create", "Select"))
        self.LBL_4.setText(_translate("DLG_Create", "Name your server folder:"))
