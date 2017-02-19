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
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #http://www.cnblogs.com/caomingongli/archive/2011/09/19/2181842.html    这个不错   PyQt之自定义无边框窗口遮盖任务栏显示问题
        flags = 0  #设置禁止最大化
        flags|= Qt.WindowMinimizeButtonHint  #设置禁止最大化
        self.setWindowFlags(flags)  #设置禁止最大化
        #self.setWindowTitle(u'')  #设置标题
        self.ini() #初始化
        self.ini_data() #初始化
        #事件处理
        ##########################
        from class_top1 import top_1
        self.top_1=top_1(self.ui,self.model)
        from eval_PHP_ASP_ASPX import eval_p_a_a
        self.eval_p_a_a=eval_p_a_a(self.ui,self.model)
        #                      控件                                                       响应函数
        QtCore.QObject.connect(self.ui.maim_pushButton_1, QtCore.SIGNAL(_fromUtf8("clicked()")),self.top_1.dr_yjh_Button) #导入一句话
        QtCore.QObject.connect(self.ui.main_pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")),self.top_1.Button_2) #测试一句话\n(并存入数据库)
        QtCore.QObject.connect(self.ui.SQLite_pushButton_1, QtCore.SIGNAL(_fromUtf8("clicked()")),self.top_1.SQLite_Button_1) #显示全部数据
        QtCore.QObject.connect(self.ui.SQLite_pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")),self.top_1.SQLite_Button_2) #显示一句话成功数据
        QtCore.QObject.connect(self.ui.SQLite_pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")),self.top_1.SQLite_Button_3) #显示一句话失败数据
        QtCore.QObject.connect(self.ui.SQLite_pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")),self.top_1.SQLite_Button_4) #导出选择的一句话
        QtCore.QObject.connect(self.ui.SQLite_pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")),self.top_1.SQLite_Button_5) #删除选择的一句话
        QtCore.QObject.connect(self.ui.main_pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")),self.top_1.Button_3) #br pr sogo
        QtCore.QObject.connect(self.ui.main_pushButton_PHP, QtCore.SIGNAL(_fromUtf8("clicked()")),self.eval_p_a_a.Button_php) #执行PHP代码
        QtCore.QObject.connect(self.ui.main_pushButton_ASP, QtCore.SIGNAL(_fromUtf8("clicked()")),self.eval_p_a_a.Button_ASP) #执行ASP代码

        QtCore.QObject.connect(self.ui.comboBox, QtCore.SIGNAL('activated(QString)'), self.OnActivated) #获取用户选择下拉列表内容
        QtCore.QObject.connect(self.ui.comboBox, QtCore.SIGNAL('currentIndexChanged(int)'), self.top_1.comboBox_index) #获取用户选择用户的ID
        QtCore.QObject.connect(self.ui.comboBox_Button, QtCore.SIGNAL(_fromUtf8("clicked()")),self.top_1.comboBox_Button_sql) #查询操作

#        self.ui.SQLite_tableView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
#        self.ui.SQLite_tableView.customContextMenuRequested[QtCore.QPoint].connect(self.myListWidgetContext)
        self.ui.SQLite_tableView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.SQLite_tableView.customContextMenuRequested[QtCore.QPoint].connect(self.myListWidgetContext)

    def OnActivated(self,txt):
        if txt==u"一句话地址":
            self.ui.comboBox_text.setText("http://127.0.0.1/xx.php")
        if txt==u"密码":
            self.ui.comboBox_text.setText("123456")
        if txt==u"状态":
            self.ui.comboBox_text.setText("ok")
        if txt==u"操作系统":
            self.ui.comboBox_text.setText("WinNT")
        if txt==u"br":
            self.ui.comboBox_text.setText("1")
        if txt==u"pr":
            self.ui.comboBox_text.setText("1")
        if txt==u"Sogou":
            self.ui.comboBox_text.setText("1")
        if txt==u"IP/地址位置":
            self.ui.comboBox_text.setText(U"只能是英文或者数字")

    def myListWidgetContext(self, point):
#        print 'aaa'
#        popMenu = QtGui.QMenu()
#        popMenu.addAction(QtGui.QAction(u'导入一句话', self))
#        popMenu.addAction(QtGui.QAction(u'导出选择一句话', self))
#        popMenu.addAction(QtGui.QAction(u'删除选择一句话', self))
#        popMenu.exec_(QtGui.QCursor.pos())
        #self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.menu=QtGui.QMenu(self)
        menu1=self.menu.addAction(u'导入一句话')
        menu1.triggered.connect(self.top_1.dr_yjh_Button)
        menu2=self.menu.addAction(u'导出选择一句话')
        menu2.triggered.connect(self.top_1.SQLite_Button_4)
        menu3=self.menu.addAction(u'删除选择一句话')
        menu3.triggered.connect(self.top_1.SQLite_Button_5)
        #self.menu.exec_(self.mapToGlobal(QtCore.QPoint(240,230)))
        self.menu.exec_(QtGui.QCursor.pos())

    def open_txt(self,name):  #打开文件
        try:
            xxx = file(name, 'r')
            return xxx.read()
        except Exception, e:
            return ""

    def ini_data(self): #初始化数据
        #self.ui.messagebox.setEnabled(0)  #给改成禁用
        self.ui.messagebox.append(u"欢迎使用 落雪技术支持作品 QQ:2602159946----TIME:%s"%(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
        self.ui.statusbar.showMessage(u"欢迎使用 落雪技术支持作品 QQ:2602159946----TIME:%s"%(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
        #self.ui.textEdit_PHP_data.setText(u"echo \"落雪技术支持QQ：2602159946\";")  #转化下防止中文路径
        php_data=self.open_txt("data.php")
        if len(php_data)>=1:
            data=u"%s"%(php_data)
            self.ui.textEdit_PHP_data.setText(data)
        else:
            self.ui.textEdit_PHP_data.setText(u"<?php\necho \"落雪技术支持QQ：2602159946\";\n?>")

        asp_data=self.open_txt("data.asp")
        if len(asp_data)>=1:
            data=u"%s"%(str(asp_data))
            self.ui.textEdit_ASP_data.setText(data)
        else:
            self.ui.textEdit_ASP_data.setText(u"--------------------")

        self.ui.comboBox.addItem(u'一句话地址')
        self.ui.comboBox.addItem(u'密码')
        self.ui.comboBox.addItem(u'状态')
        self.ui.comboBox.addItem(u'操作系统')
        self.ui.comboBox.addItem(u'br')
        self.ui.comboBox.addItem(u'pr')
        self.ui.comboBox.addItem(u'Sogou')
        self.ui.comboBox.addItem(u'IP/地址位置')

        self.ui.comboBox_text.setText("http://127.0.0.1/xx.php")

    #初始化200
    def ini(self): #初始化
        self.model = QStandardItemModel()
        self.model.setColumnCount(7)     #列
        self.model.setRowCount(0)  #行  len(node)
        self.model.setHorizontalHeaderLabels([u'一句话地址',u'密码',u'状态',u'操作系统',u'br',u'pr',u'sr',u'IP/地址位置',u'添加时间',u'最新操作时间'])
        self.ui.SQLite_tableView.setModel(self.model)
        #self.tableView.resizeColumnsToContents()   #由内容调整列
        self.ui.SQLite_tableView.setColumnWidth(0,380)  #设置表格的各列的宽度值
        self.ui.SQLite_tableView.setColumnWidth(1,70)  #设置表格的各列的宽度值
        self.ui.SQLite_tableView.setColumnWidth(2,50)  #设置表格的各列的宽度值
        self.ui.SQLite_tableView.setColumnWidth(3,100)  #设置表格的各列的宽度值
        self.ui.SQLite_tableView.setColumnWidth(4,50)  #设置表格的各列的宽度值
        self.ui.SQLite_tableView.setColumnWidth(5,50)  #设置表格的各列的宽度值
        self.ui.SQLite_tableView.setColumnWidth(6,60)  #设置表格的各列的宽度值
        self.ui.SQLite_tableView.setColumnWidth(7,300)  #设置表格的各列的宽度值
        self.ui.SQLite_tableView.setColumnWidth(8,170)  #设置表格的各列的宽度值
        self.ui.SQLite_tableView.setColumnWidth(9,170)  #设置表格的各列的宽度值
        for i in range(0):  #调整行高度  len(node)
            self.ui.SQLite_tableView.setRowHeight(i, 20)
        self.ui.SQLite_tableView.setEditTriggers(QTableWidget.NoEditTriggers)  #设置表格的单元为只读属性，即不能编辑
        self.ui.SQLite_tableView.setSelectionBehavior(QTableWidget.SelectRows) #点击选择是选择行//设置选中时为整行选中
        #self.tableView.setSelectionMode(QTableWidget.SingleSelection)  #禁止多行选择
        self.ui.SQLite_tableView.setAlternatingRowColors(True)  #还是只可以选择单行（单列）
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


