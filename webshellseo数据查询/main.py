#!/usr/local/bin/python
#-*- coding: UTF-8 -*-

from uimain import *

import socket
socket.setdefaulttimeout(10)

from ctypes import *
#import win32ui
import thread
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

#        self.ui.spinBox.setRange(0, 2200)  #设置spinBox的值范围
#        self.ui.spinBox.setValue(2013)  #初始化
#        self.ui.spinBox.setEnabled(0)  #给改成禁用
        self.ui.cx_textEdit.setText(U"2013")
        self.ini() #初始化
        self.ini_data() #初始化数据
        #事件处理
        ##########################
        from class_top1 import top_1
        self.top_1=top_1(self.ui,self.model)
        #                      控件                                                       响应函数
        QtCore.QObject.connect(self.ui.pushButton_1, QtCore.SIGNAL(_fromUtf8("clicked()")),self.top_1.pushButton_1) #导入一句话
        QtCore.QObject.connect(self.ui.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")),self.top_1.pushButton_2) #显示全部数据
        QtCore.QObject.connect(self.ui.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")),self.top_1.pushButton_3) #删除数据
        QtCore.QObject.connect(self.ui.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")),self.top_1.pushButton_4) #测试webshell状态
        QtCore.QObject.connect(self.ui.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")),self.top_1.pushButton_5) #查询_外链收录\n(百度_360_搜狗)
        QtCore.QObject.connect(self.ui.pushButton_6, QtCore.SIGNAL(_fromUtf8("clicked()")),self.top_1.pushButton_6) #导出数据
        QtCore.QObject.connect(self.ui.comboBox_Button, QtCore.SIGNAL(_fromUtf8("clicked()")),self.top_1.comboBox_Button) #查询
        QtCore.QObject.connect(self.ui.pushButton_cx_xx, QtCore.SIGNAL(_fromUtf8("clicked()")),self.top_1.pushButton_cx_xx) #全部选择
        QtCore.QObject.connect(self.ui.pushButton_7, QtCore.SIGNAL(_fromUtf8("clicked()")),self.top_1.pushButton_7) #显示成功webshell
        QtCore.QObject.connect(self.ui.pushButton_8, QtCore.SIGNAL(_fromUtf8("clicked()")),self.top_1.pushButton_8) #显示失败webshell

        #QtCore.QObject.connect(self.ui.comboBox, QtCore.SIGNAL('activated(QString)'), self.OnActivated) #获取用户选择下拉列表内容
        QtCore.QObject.connect(self.ui.comboBox, QtCore.SIGNAL('currentIndexChanged(int)'), self.top_1.comboBox_index) #获取用户选择用户的ID

    def ini_data(self): #初始化数据
        self.ui.comboBox.addItem(u'==============')
        self.ui.comboBox.addItem(u'建站时间')
        self.ui.comboBox.addItem(u'br')
        self.ui.comboBox.addItem(u'pr')
        self.ui.comboBox.addItem(u'sr')
        self.ui.comboBox.addItem(u'百度收录')
        self.ui.comboBox.addItem(u'百度外链')
        self.ui.comboBox.addItem(u'360收录')
        self.ui.comboBox.addItem(u'360外链')
        self.ui.comboBox.addItem(u'搜狗收录')
        self.ui.comboBox.addItem(u'搜狗外链')
        self.ui.comboBox.addItem(u'bing收录')
        self.ui.comboBox.addItem(u'bing外链')
        self.ui.comboBox.addItem(u'百度来路ip')

    #初始化200
    def ini(self): #初始化
        self.model = QStandardItemModel()
        self.model.setColumnCount(7)     #列
        self.model.setRowCount(0)  #行  len(node)
        self.model.setHorizontalHeaderLabels([u'url地址',u'密码',u'状态',u'建站时间',u'br',u'pr',u'sr',u'百度收录',u'百度外链',u'360收录',u'360外链',
                                              u'搜狗收录',u'搜狗外链',u'bing收录',u'bing外链',u'百度来路ip'])
        self.ui.tableView.setModel(self.model)
        #self.tableView.resizeColumnsToContents()   #由内容调整列
        self.ui.tableView.setColumnWidth(0,300)  #设置表格的各列的宽度值
        self.ui.tableView.setColumnWidth(1,80)  #设置表格的各列的宽度值
        self.ui.tableView.setColumnWidth(2,50)  #设置表格的各列的宽度值
        self.ui.tableView.setColumnWidth(3,130)  #设置表格的各列的宽度值
        self.ui.tableView.setColumnWidth(4,50)  #设置表格的各列的宽度值
        self.ui.tableView.setColumnWidth(5,50)  #设置表格的各列的宽度值
        self.ui.tableView.setColumnWidth(6,50)  #设置表格的各列的宽度值
        self.ui.tableView.setColumnWidth(7,70)  #设置表格的各列的宽度值
        self.ui.tableView.setColumnWidth(8,70)  #设置表格的各列的宽度值
        self.ui.tableView.setColumnWidth(9,70)  #设置表格的各列的宽度值
        self.ui.tableView.setColumnWidth(10,70)  #设置表格的各列的宽度值
        self.ui.tableView.setColumnWidth(11,70)  #设置表格的各列的宽度值
        self.ui.tableView.setColumnWidth(12,70)  #设置表格的各列的宽度值
        self.ui.tableView.setColumnWidth(13,70)  #设置表格的各列的宽度值
        self.ui.tableView.setColumnWidth(14,70)  #设置表格的各列的宽度值
        self.ui.tableView.setColumnWidth(15,90)  #设置表格的各列的宽度值
        for i in range(0):  #调整行高度  len(node)
            self.ui.tableView.setRowHeight(i, 20)
        self.ui.tableView.setEditTriggers(QTableWidget.NoEditTriggers)  #设置表格的单元为只读属性，即不能编辑
        self.ui.tableView.setSelectionBehavior(QTableWidget.SelectRows) #点击选择是选择行//设置选中时为整行选中
        #self.tableView.setSelectionMode(QTableWidget.SingleSelection)  #禁止多行选择
        self.ui.tableView.setAlternatingRowColors(True)  #还是只可以选择单行（单列）
        #self.tableView.verticalHeader().hide() #隐藏行头


import time
from PyQt4 import QtCore, QtGui ,QtNetwork
from PyQt4.QtCore import *
#from ctypes import *
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