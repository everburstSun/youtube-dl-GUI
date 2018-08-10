# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_design.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(650, 501)
        self.ExtractBtn = QtWidgets.QPushButton(Form)
        self.ExtractBtn.setGeometry(QtCore.QRect(556, 40, 92, 32))
        self.ExtractBtn.setFocusPolicy(QtCore.Qt.TabFocus)
        self.ExtractBtn.setObjectName("ExtractBtn")
        self.DownloadBtn = QtWidgets.QPushButton(Form)
        self.DownloadBtn.setGeometry(QtCore.QRect(534, 354, 113, 32))
        self.DownloadBtn.setObjectName("DownloadBtn")
        self.AddrEdit = QtWidgets.QLineEdit(Form)
        self.AddrEdit.setGeometry(QtCore.QRect(84, 44, 471, 21))
        self.AddrEdit.setObjectName("AddrEdit")
        self.AddrLbl = QtWidgets.QLabel(Form)
        self.AddrLbl.setGeometry(QtCore.QRect(20, 47, 54, 16))
        self.AddrLbl.setObjectName("AddrLbl")
        self.PxyEdit = QtWidgets.QLineEdit(Form)
        self.PxyEdit.setGeometry(QtCore.QRect(84, 14, 111, 21))
        self.PxyEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.PxyEdit.setObjectName("PxyEdit")
        self.ProxyLbl = QtWidgets.QLabel(Form)
        self.ProxyLbl.setGeometry(QtCore.QRect(36, 17, 41, 16))
        self.ProxyLbl.setObjectName("ProxyLbl")
        self.PxyClrBtn = QtWidgets.QPushButton(Form)
        self.PxyClrBtn.setGeometry(QtCore.QRect(556, 10, 92, 32))
        self.PxyClrBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.PxyClrBtn.setObjectName("PxyClrBtn")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 80, 631, 271))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(126)
        self.tableWidget.verticalHeader().setVisible(False)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(10, 390, 631, 101))
        self.textBrowser.setObjectName("textBrowser")
        self.SeleLbl = QtWidgets.QLabel(Form)
        self.SeleLbl.setGeometry(QtCore.QRect(10, 363, 141, 16))
        self.SeleLbl.setObjectName("SeleLbl")
        self.SeleEdit = QtWidgets.QLineEdit(Form)
        self.SeleEdit.setGeometry(QtCore.QRect(150, 360, 111, 21))
        self.SeleEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.SeleEdit.setText("")
        self.SeleEdit.setObjectName("SeleEdit")

        self.retranslateUi(Form)
        self.PxyClrBtn.clicked.connect(self.AddrEdit.clear)
        self.AddrEdit.returnPressed.connect(self.ExtractBtn.click)
        self.SeleEdit.returnPressed.connect(self.DownloadBtn.click)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.AddrEdit, self.ExtractBtn)
        Form.setTabOrder(self.ExtractBtn, self.DownloadBtn)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Video Downloader"))
        self.ExtractBtn.setText(_translate("Form", "Extract"))
        self.DownloadBtn.setText(_translate("Form", "Download"))
        self.AddrLbl.setText(_translate("Form", "Address:"))
        self.PxyEdit.setText(_translate("Form", "127.0.0.1:1087"))
        self.ProxyLbl.setText(_translate("Form", "Proxy:"))
        self.PxyClrBtn.setText(_translate("Form", "Clear"))
        self.SeleLbl.setText(_translate("Form", "Selected format code:"))

