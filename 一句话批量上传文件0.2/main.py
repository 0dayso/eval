#!/usr/local/bin/python
#-*- coding: UTF-8 -*-

from uimain import *

import socket
socket.setdefaulttimeout(10)

from ctypes import *
import win32ui
user32 = windll.LoadLibrary('user32.dll')               # 加载动态链接库
#user32.MessageBoxW(0,c_wchar_p("1111111"), c_wchar_p("QQ:23456789"), 0)   # 调用MessageBoxA函数

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class Start(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        #http://www.cnblogs.com/caomingongli/archive/2011/09/19/2181842.html    这个不错   PyQt之自定义无边框窗口遮盖任务栏显示问题
        flags = 0  #设置禁止最大化
        flags|= Qt.WindowMinimizeButtonHint  #设置禁止最大化
        self.setWindowFlags(flags)  #设置禁止最大化
        #self.setWindowTitle(u'')  #设置标题
        self.ini() #初始化
        #事件处理
        ##########################
        from class_top1 import top1
        self.top1=top1(self.ui,self.model)
        #                      控件                                                       响应函数
        QtCore.QObject.connect(self.ui.pb_pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")),self.top1.Button) #导入一句话
        QtCore.QObject.connect(self.ui.tx_checkBox_1, QtCore.SIGNAL(_fromUtf8("clicked()")), self.test_checkBox)  #复选框
        QtCore.QObject.connect(self.ui.pb_pushButton_1, QtCore.SIGNAL(_fromUtf8("clicked()")), self.top1.Button_2) #手动测试一句话
        QtCore.QObject.connect(self.ui.pb_pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.top1.Button_4) #选择文件
        QtCore.QObject.connect(self.ui.pb_pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.top1.Button_5) #上传文件
        QtCore.QObject.connect(self.ui.pb_pushButton_6, QtCore.SIGNAL(_fromUtf8("clicked()")), self.top1.Button_6) #访问上传文件URL路径
        QtCore.QObject.connect(self.ui.pb_pushButton_7, QtCore.SIGNAL(_fromUtf8("clicked()")), self.top1.Button_7) #设置URL路径(带参数)
        QtCore.QObject.connect(self.ui.pb_pushButton_8, QtCore.SIGNAL(_fromUtf8("clicked()")), self.top1.Button_8) #访问URL路径(带参数)
        QtCore.QObject.connect(self.ui.pb_pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.mess) #软件说明
        ##########################


    def mess(self): #软件说明
        user32.MessageBoxW(0,c_wchar_p(u"一句话--自动--批量上传网页文件--自动访问\n0.2无限制版本\nQQ群:142168763\n落雪设计\n主要针对站内站繁殖器 做其他的也可以"), c_wchar_p(u"软件说明"), 0)   # 调用MessageBoxA函数

    def test_checkBox(self):  #自动手动
        if self.ui.tx_checkBox_1.isChecked():
            self.ui.pb_pushButton_1.setEnabled(0)  #给改成禁用
        else:
            self.ui.pb_pushButton_1.setEnabled(1)

    #初始化
    def ini(self): #初始化
        self.messbx(u'欢迎使用--一句话批量自动上传--自动访问器--TIME:%s'%(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
        self.messbx(u"一句话--自动--上传网页文件--自动访问--0.2无限制版本--QQ群:142168763--落雪设计")
        self.messbx(u"懒虫版--站内站繁殖器")
        self.messbx(u"目前只支持--PHP 一句话")
        self.ui.tx_checkBox_1.setChecked( True )    #设置复选框为选择状态
        self.ui.tx_checkBox_2.setChecked( True )   #设置复选框为选择状态
        self.ui.tx_checkBox_3.setChecked( True )   #设置复选框为选择状态
        #self.ui.checkBox_3.setChecked( True )  #隐藏访问URL
        self.ui.pb_pushButton_1.setEnabled(0)  #给改成禁用
        self.ui.checkBox_3.setEnabled(0)  #给改成禁用
        self.ui.tx_textEdit_3.setEnabled(0)  #给改成禁用
        #self.ui.checkBox.setEnabled(0)  #给改成禁用
        #self.ui.checkBox_2.setEnabled(0)  #给改成禁用

        self.model = QStandardItemModel()
        self.model.setColumnCount(7)     #列
        self.model.setRowCount(0)  #行  len(node)
        self.model.setHorizontalHeaderLabels([u'一句话地址',u'密码',u'状态',u'操作系统',u'上传URL路径',u'访问URL路径(带参数)',u'IP/地址位置'])
        self.ui.tableView.setModel(self.model)
        #self.tableView.resizeColumnsToContents()   #由内容调整列
        self.ui.tableView.setColumnWidth(0,300)  #设置表格的各列的宽度值
        self.ui.tableView.setColumnWidth(1,50)  #设置表格的各列的宽度值
        self.ui.tableView.setColumnWidth(2,35)  #设置表格的各列的宽度值
        self.ui.tableView.setColumnWidth(3,60)  #设置表格的各列的宽度值
        self.ui.tableView.setColumnWidth(4,240)  #设置表格的各列的宽度值
        self.ui.tableView.setColumnWidth(5,240)  #设置表格的各列的宽度值
        self.ui.tableView.setColumnWidth(6,200)  #设置表格的各列的宽度值
        for i in range(0):  #调整行高度  len(node)
            self.ui.tableView.setRowHeight(i, 20)
        self.ui.tableView.setEditTriggers(QTableWidget.NoEditTriggers)  #设置表格的单元为只读属性，即不能编辑
        self.ui.tableView.setSelectionBehavior(QTableWidget.SelectRows) #点击选择是选择行//设置选中时为整行选中
        #self.tableView.setSelectionMode(QTableWidget.SingleSelection)  #禁止多行选择
        self.ui.tableView.setAlternatingRowColors(True)  #还是只可以选择单行（单列）
        #self.tableView.verticalHeader().hide() #隐藏行头


    def messbx(self,data):
        self.ui.messagebox.append(data)




import time
from PyQt4 import QtCore, QtGui ,QtNetwork
from PyQt4.QtCore import *
from ctypes import *
from PyQt4.QtGui import *
#import QtNetwork
user32 = windll.LoadLibrary('user32.dll')               # 加载动态链接库
#user32.MessageBoxW(0,c_wchar_p("1111111"), c_wchar_p("QQ:23456789"), 0)   # 调用MessageBoxA函数
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    #lang = QtCore.QTranslator()
    #lang.load("qt_zh_CN.qm")
    #app.installTranslator(lang)#载入中文字体需要从qt安装目录里复制PyQt4\translations\qt_zh_CN.qm
    myapp = Start()
    myapp.show()
    sys.exit(app.exec_())
