# -*- coding: utf-8 -*-
#Author: Zifeng Wang
#Date: 2018/04/04
#Python 3.6.2 AMD64
#All Rights Reserved, No Commercial Use.
#A Crawler for http://jsjtw.sh.gov.cn.
# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\导师制\GUI\SpiderRunner.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
import time

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(376, 326)
        self.Start_date = QtWidgets.QDateEdit(Form)
        self.Start_date.setGeometry(QtCore.QRect(90, 20, 110, 22))
        self.Start_date.setObjectName("Start_date")
        self.End_date = QtWidgets.QDateEdit(Form)
        self.End_date.setGeometry(QtCore.QRect(90, 80, 110, 22))
        self.End_date.setObjectName("End_date")
        self.RunButton = QtWidgets.QPushButton(Form)
        self.RunButton.setGeometry(QtCore.QRect(220, 20, 81, 81))
        self.RunButton.setObjectName("RunButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 71, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 72, 15))
        self.label_2.setObjectName("label_2")
        self.URLEdit = QtWidgets.QLineEdit(Form)
        self.URLEdit.setGeometry(QtCore.QRect(90, 140, 211, 21))
        self.URLEdit.setObjectName("URLEdit")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 170, 201, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 200, 141, 16))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(20, 140, 41, 20))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        self.RunButton.clicked.connect(Form.update)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.Start_date, self.End_date)
        Form.setTabOrder(self.End_date, self.RunButton)
        Form.setTabOrder(self.RunButton, self.URLEdit)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        now_day = time.strftime("%Y-%m-%d",time.localtime())
        default_start_day = '2017-01-01'
        self.End_date.setDate(QDate.fromString(now_day,'yyyy-MM-dd'))
        self.Start_date.setDate(QDate.fromString(default_start_day,'yyyy-MM-dd'))
        Form.setWindowTitle(_translate("Form", "Form"))
        self.RunButton.setText(_translate("Form", "开始运行"))
        self.URLEdit.setText("http://jsjtw.sh.gov.cn/gb/node2/n4/n14/n840/n918/u1ai175338.html")
        self.label.setText(_translate("Form", "起始日期"))
        self.label_2.setText(_translate("Form", "终止日期"))
        self.label_3.setText(_translate("Form", "注意:将浏览器地址框URL"))
        self.label_4.setText(_translate("Form", "复制并黏贴于上框内"))
        self.label_6.setText(_translate("Form", "URL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

