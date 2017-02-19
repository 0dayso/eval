# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Sat Oct 12 23:17:54 2013
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1197, 614)
        self.messagebox = QtGui.QTextEdit(Dialog)
        self.messagebox.setGeometry(QtCore.QRect(610, 400, 581, 211))
        self.messagebox.setObjectName(_fromUtf8("messagebox"))
        self.tableView = QtGui.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(10, 10, 1181, 381))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 420, 291, 131))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.tx_checkBox_3 = QtGui.QCheckBox(self.groupBox)
        self.tx_checkBox_3.setGeometry(QtCore.QRect(10, 60, 141, 16))
        self.tx_checkBox_3.setObjectName(_fromUtf8("tx_checkBox_3"))
        self.pb_pushButton_1 = QtGui.QPushButton(self.groupBox)
        self.pb_pushButton_1.setGeometry(QtCore.QRect(180, 10, 101, 71))
        self.pb_pushButton_1.setObjectName(_fromUtf8("pb_pushButton_1"))
        self.tx_checkBox_1 = QtGui.QCheckBox(self.groupBox)
        self.tx_checkBox_1.setGeometry(QtCore.QRect(10, 20, 141, 16))
        self.tx_checkBox_1.setObjectName(_fromUtf8("tx_checkBox_1"))
        self.pb_pushButton_2 = QtGui.QPushButton(self.groupBox)
        self.pb_pushButton_2.setGeometry(QtCore.QRect(10, 90, 131, 31))
        self.pb_pushButton_2.setObjectName(_fromUtf8("pb_pushButton_2"))
        self.pb_pushButton_3 = QtGui.QPushButton(self.groupBox)
        self.pb_pushButton_3.setGeometry(QtCore.QRect(150, 90, 131, 31))
        self.pb_pushButton_3.setObjectName(_fromUtf8("pb_pushButton_3"))
        self.tx_checkBox_2 = QtGui.QCheckBox(self.groupBox)
        self.tx_checkBox_2.setGeometry(QtCore.QRect(10, 40, 171, 16))
        self.tx_checkBox_2.setObjectName(_fromUtf8("tx_checkBox_2"))
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(310, 400, 291, 211))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(150, 20, 41, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tx_textEdit_1 = QtGui.QTextEdit(self.groupBox_2)
        self.tx_textEdit_1.setGeometry(QtCore.QRect(70, 10, 71, 31))
        self.tx_textEdit_1.setObjectName(_fromUtf8("tx_textEdit_1"))
        self.tx_textEdit_4 = QtGui.QTextEdit(self.groupBox_2)
        self.tx_textEdit_4.setGeometry(QtCore.QRect(10, 130, 271, 31))
        self.tx_textEdit_4.setObjectName(_fromUtf8("tx_textEdit_4"))
        self.checkBox_3 = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_3.setGeometry(QtCore.QRect(190, 20, 91, 20))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.pb_pushButton_6 = QtGui.QPushButton(self.groupBox_2)
        self.pb_pushButton_6.setGeometry(QtCore.QRect(180, 90, 101, 31))
        self.pb_pushButton_6.setObjectName(_fromUtf8("pb_pushButton_6"))
        self.pb_pushButton_7 = QtGui.QPushButton(self.groupBox_2)
        self.pb_pushButton_7.setGeometry(QtCore.QRect(10, 170, 131, 31))
        self.pb_pushButton_7.setObjectName(_fromUtf8("pb_pushButton_7"))
        self.tx_textEdit_2 = QtGui.QTextEdit(self.groupBox_2)
        self.tx_textEdit_2.setGeometry(QtCore.QRect(10, 50, 201, 31))
        self.tx_textEdit_2.setObjectName(_fromUtf8("tx_textEdit_2"))
        self.pb_pushButton_5 = QtGui.QPushButton(self.groupBox_2)
        self.pb_pushButton_5.setGeometry(QtCore.QRect(100, 90, 71, 31))
        self.pb_pushButton_5.setObjectName(_fromUtf8("pb_pushButton_5"))
        self.pb_pushButton_8 = QtGui.QPushButton(self.groupBox_2)
        self.pb_pushButton_8.setGeometry(QtCore.QRect(150, 170, 131, 31))
        self.pb_pushButton_8.setObjectName(_fromUtf8("pb_pushButton_8"))
        self.pb_pushButton_4 = QtGui.QPushButton(self.groupBox_2)
        self.pb_pushButton_4.setGeometry(QtCore.QRect(220, 50, 61, 31))
        self.pb_pushButton_4.setObjectName(_fromUtf8("pb_pushButton_4"))
        self.tx_textEdit_3 = QtGui.QTextEdit(self.groupBox_2)
        self.tx_textEdit_3.setGeometry(QtCore.QRect(10, 90, 81, 31))
        self.tx_textEdit_3.setObjectName(_fromUtf8("tx_textEdit_3"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 550, 291, 61))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 400, 271, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "一句话--自动--上传网页文件--自动访问--0.2无限制版本--铁杆国际-我是晚辈-定制--落雪设计", None))
        self.groupBox.setTitle(_translate("Dialog", "导入数据", None))
        self.tx_checkBox_3.setText(_translate("Dialog", "自动检测IP/地理位置", None))
        self.pb_pushButton_1.setText(_translate("Dialog", "手动选择\n"
"检测一句话\n"
"状态", None))
        self.tx_checkBox_1.setText(_translate("Dialog", "自动测试一句话状态", None))
        self.pb_pushButton_2.setText(_translate("Dialog", "导入一句话", None))
        self.pb_pushButton_3.setText(_translate("Dialog", "软件说明", None))
        self.tx_checkBox_2.setText(_translate("Dialog", "测试系统版本(延时10s启动)", None))
        self.groupBox_2.setTitle(_translate("Dialog", "上传/访问", None))
        self.label_2.setText(_translate("Dialog", "/s(秒)", None))
        self.tx_textEdit_1.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10</p></body></html>", None))
        self.tx_textEdit_4.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">123.php?del=123456</p></body></html>", None))
        self.checkBox_3.setText(_translate("Dialog", "隐藏访问URL", None))
        self.label.setText(_translate("Dialog", "延时/超时:", None))
        self.pb_pushButton_6.setText(_translate("Dialog", "访问上传URL路径", None))
        self.pb_pushButton_7.setText(_translate("Dialog", "设置URL路径(带参数)", None))
        self.tx_textEdit_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">c:/123.php</p></body></html>", None))
        self.pb_pushButton_5.setText(_translate("Dialog", "上传文件", None))
        self.pb_pushButton_8.setText(_translate("Dialog", "访问URL路径(带参数)", None))
        self.pb_pushButton_4.setText(_translate("Dialog", "选择文件", None))
        self.tx_textEdit_3.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">123.php</p></body></html>", None))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">按住CTRL或SHIFT选择要操作的URL</span></p><p align=\"center\"><span style=\" font-size:14pt;\">和选择文件夹或文件是一样的</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">=====================================</span></p></body></html>", None))

