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
import sys,os
#import platform
#import tkMessageBox
user32 = windll.LoadLibrary('user32.dll')               # 加载动态链接库
#user32.MessageBoxW(0,c_wchar_p("1111111"), c_wchar_p("QQ:2602159946"), 0)   # 调用MessageBoxA函数
import Csqlite3  #数据库操作
import urllib #转换成网络格式
import ConfigParser  #INI读取数据
import thread
import random
import br_pr_sogo #查询
import baidu_360_sougo_wl_sl #查询_外链收录\n(百度_360_搜狗)
import g  #公用文件
import yijuhua

class   top_1(object):
    def __init__(self,ui,model):
        self.ui=ui
        self.model=model
        #数据库链接
        self.sql3=Csqlite3.C_sqlite3()
        self.sql3.mysqlite3_open()
        self.comboBox_index_int=0 #保存用户选择的ID

    def comboBox_index(self,data): #获取用户选择用户的ID
        self.comboBox_index_int=data

    #添加数据
    def tableView_add(self,ints,s1=None,s2=None,s3=None,s4=None,s5=None,s6=None,s7=None,s8=None,s9=None,s10=None,s11=None,s12=None,s13=None,s14=None,s15=None,s16=None):  #添加数据
        try:
            #红色：(255,0,0)
            #绿色：(0,255,0)  11
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
            if not s8==None:
                self.model.setItem(ints, 7, QStandardItem(s8))
            if not s9==None:
                self.model.setItem(ints, 8, QStandardItem(s9))
            if not s10==None:
                self.model.setItem(ints, 9, QStandardItem(s10))
            if not s11==None:
                self.model.setItem(ints, 10, QStandardItem(s11))
            if not s12==None:
                self.model.setItem(ints, 11, QStandardItem(s12))
            if not s13==None:
                self.model.setItem(ints, 12, QStandardItem(s13))
            if not s14==None:
                self.model.setItem(ints, 13, QStandardItem(s14))
            if not s15==None:
                self.model.setItem(ints, 14, QStandardItem(s15))
            if not s16==None:
                self.model.setItem(ints, 15, QStandardItem(s16))

            if s3=="No" or s3=="null":  #红色  #改变背景色
                self.model.item(ints,0).setBackground(QColor(255, 0, 0))#//改变背景色
                self.model.item(ints,1).setBackground(QColor(255, 0, 0))#//改变背景色
                self.model.item(ints,2).setBackground(QColor(255, 0, 0))#//改变背景色
                self.model.item(ints,3).setBackground(QColor(255, 0, 0))#//改变背景色
                self.model.item(ints,4).setBackground(QColor(255, 0, 0))#//改变背景色
                self.model.item(ints,5).setBackground(QColor(255, 0, 0))#//改变背景色
                self.model.item(ints,6).setBackground(QColor(255, 0, 0))#//改变背景色
                self.model.item(ints,7).setBackground(QColor(255, 0, 0))#//改变背景色
                self.model.item(ints,8).setBackground(QColor(255, 0, 0))#//改变背景色
                self.model.item(ints,9).setBackground(QColor(255, 0, 0))#//改变背景色
                self.model.item(ints,10).setBackground(QColor(255, 0, 0))#//改变背景色
                self.model.item(ints,11).setBackground(QColor(255, 0, 0))#//改变背景色
                self.model.item(ints,12).setBackground(QColor(255, 0, 0))#//改变背景色
                self.model.item(ints,13).setBackground(QColor(255, 0, 0))#//改变背景色
                self.model.item(ints,14).setBackground(QColor(255, 0, 0))#//改变背景色
                self.model.item(ints,15).setBackground(QColor(255, 0, 0))#//改变背景色
            if s3=="None":
                self.model.item(ints,0).setBackground(QColor(178,178,178))#//改变背景色
                self.model.item(ints,1).setBackground(QColor(178,178,178))#//改变背景色
                self.model.item(ints,2).setBackground(QColor(178,178,178))#//改变背景色
                self.model.item(ints,3).setBackground(QColor(178,178,178))#//改变背景色
                self.model.item(ints,4).setBackground(QColor(178,178,178))#//改变背景色
                self.model.item(ints,5).setBackground(QColor(178,178,178))#//改变背景色
                self.model.item(ints,6).setBackground(QColor(178,178,178))#//改变背景色
                self.model.item(ints,7).setBackground(QColor(178,178,178))#//改变背景色
                self.model.item(ints,8).setBackground(QColor(178,178,178))#//改变背景色
                self.model.item(ints,9).setBackground(QColor(178,178,178))#//改变背景色
                self.model.item(ints,10).setBackground(QColor(178,178,178))#//改变背景色
                self.model.item(ints,11).setBackground(QColor(178,178,178))#//改变背景色
                self.model.item(ints,12).setBackground(QColor(178,178,178))#//改变背景色
                self.model.item(ints,13).setBackground(QColor(178,178,178))#//改变背景色
                self.model.item(ints,14).setBackground(QColor(178,178,178))#//改变背景色
                self.model.item(ints,15).setBackground(QColor(178,178,178))#//改变背景色
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

    def pushButton_1(self):  #导入数据
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

    def pushButton_2(self):  #显示全部数据
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
            s3=u"%s"%(urllib.unquote(str(line[3])))
            s15=u"%s"%(str(line[15]))
            self.tableView_add(int_id,s0,str(line[1]),str(line[2]),s3,str(line[4]),str(line[5]),str(line[6]),str(line[7]),str(line[8]),str(line[9]),str(line[10]),str(line[11]),str(line[12]),str(line[13]),str(line[14]),s15)  #添加数据
            int_id+=1
        cur.close()  #关闭游标

    def pushButton_3(self):  #删除数据
        int_model = self.ui.tableView.selectionModel()  #获取选中编号
        model = self.ui.tableView.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
        if len(int_model.selectedRows())==0:
            user32.MessageBoxW(0,c_wchar_p(u"请选择有效内容"), c_wchar_p(u"提示"), 0)   # 调用MessageBoxA函数
            return
        for index in int_model.selectedRows():       #// 对于被选中的每一行
            try:
                int_index=index.row()#获取行号
                s0= model.data(model.index(int_index,0)).toString()  #urllib.quote(str(s0))
                sql_data="delete from url where url='%s'"%(str(s0))
                self.sql3.mysqlite3_delete(sql_data)
            except BaseException, e:
                print(str(e))
        self.pushButton_2() #显示状态OK

    def pushButton_4(self): #查询\WEBSHELL 状态
        int_model = self.ui.tableView.selectionModel()  #获取选中编号
        if len(int_model.selectedRows())==0:
            user32.MessageBoxW(0,c_wchar_p(u"请选择有效内容"), c_wchar_p(u"提示"), 0)   # 调用MessageBoxA函数
            return
        thread.start_new_thread(self.br_pr_sogo_4,())  #测试一句话是否连接成功

    def br_pr_sogo_4(self):  #查询\WEBSHELL 状态
        self.ui.pushButton_4.setEnabled(0)  #给改成禁用
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
                    #self.tableView_add(int_index,None,None,u"ok",None,None,None,data_time)  #添加数据
                    #sql_data="update shell set zts3='ok',time2s7='%s' where urls1='%s' and passwods2='%s'"%(data_time,str(s0),str(s1))
                    #yijuhua_win_linux(url,PASS): #URL地址 ，密码   返回操作系统
                    self.tableView_add(int_index,None,None,u"ok")  #添加数据urllib.quote(str(s0))
                    sql_data="update url set zt='ok' where url='%s' and passwod='%s'"%(str(s0),str(s1))
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
        self.ui.pushButton_4.setEnabled(1)

    def pushButton_5(self): #查询_外链收录\n(百度_360_搜狗)
        int_model = self.ui.tableView.selectionModel()  #获取选中编号
        if len(int_model.selectedRows())==0:
            user32.MessageBoxW(0,c_wchar_p(u"请选择有效内容"), c_wchar_p(u"提示"), 0)   # 调用MessageBoxA函数
            return
        thread.start_new_thread(self.br_pr_sogo_5,())  #测试一句话是否连接成功

    def br_pr_sogo_5(self):  #获取 百度 谷歌  搜狗  权重
        self.ui.pushButton_5.setEnabled(0)  #给改成禁用
        int_model = self.ui.tableView.selectionModel()  #获取选中编号
        model = self.ui.tableView.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
        for index in int_model.selectedRows():       #// 对于被选中的每一行
            try:
                data1=""
                int_index=index.row()#获取行号
                s0= model.data(model.index(int_index,0)).toString()
                url=br_pr_sogo.get_domain(str(s0),0)

                if self.ui.checkBox_1.isChecked():  #建站时间
                    url_time=baidu_360_sougo_wl_sl.url_time(url)  #查询域名注册时间
                    url_time2=u"%s"%(url_time)
                    data1+="urltime='%s',"%(urllib.quote(str(url_time)))
                    self.tableView_add(int_index,None,None,None,url_time2)  #添加数据
                if self.ui.checkBox_2.isChecked():  #br
                    baidu_br=br_pr_sogo.baidu_br(url)
                    if int(baidu_br)<=0:
                        #print "0000000000000000000000000"
                        baidu_br=br_pr_sogo.aizhan_br(url)
                    data1+="br='%s',"%(baidu_br)
                    self.tableView_add(int_index,None,None,None,None,baidu_br)  #添加数据
                if self.ui.checkBox_3.isChecked():  #pr
                    google_pr=br_pr_sogo.google_pr(url)
                    data1+="pr='%s',"%(google_pr)
                    self.tableView_add(int_index,None,None,None,None,None,google_pr)  #添加数据
                if self.ui.checkBox_4.isChecked():  #sr
                    sogo=br_pr_sogo.sogo(url)
                    data1+="sr='%s',"%(sogo)
                    self.tableView_add(int_index,None,None,None,None,None,None,sogo)  #添加数据
                if self.ui.checkBox_5.isChecked():  #百度收录
                    baidu_sl=baidu_360_sougo_wl_sl.baidu_sl(url) #百度收录数量
                    data1+="baidus1='%s',"%(baidu_sl)
                    self.tableView_add(int_index,None,None,None,None,None,None,None,baidu_sl)  #添加数据
                if self.ui.checkBox_6.isChecked():  #百度外链
                    baidu_wl=baidu_360_sougo_wl_sl.baidu_wl(url) #百度外部链接
                    data1+="baidus2='%s',"%(baidu_wl)
                    self.tableView_add(int_index,None,None,None,None,None,None,None,None,baidu_wl)  #添加数据
                if self.ui.checkBox_7.isChecked():  #360收录
                    s360_sl=baidu_360_sougo_wl_sl.s360_sl(url) #360收录数量
                    data1+="s360s1='%s',"%(s360_sl)
                    self.tableView_add(int_index,None,None,None,None,None,None,None,None,None,s360_sl)  #添加数据
                if self.ui.checkBox_8.isChecked():  #360外链
                    s360_wl=baidu_360_sougo_wl_sl.s360_wl(url) #360外部链接
                    data1+="s360s2='%s',"%(s360_wl)
                    self.tableView_add(int_index,None,None,None,None,None,None,None,None,None,None,s360_wl)  #添加数据
                if self.ui.checkBox_9.isChecked():  #搜狗收录
                    sogou_sl=baidu_360_sougo_wl_sl.sogou_sl(url) #sogou收录数量
                    data1+="sougos1='%s',"%(sogou_sl)
                    self.tableView_add(int_index,None,None,None,None,None,None,None,None,None,None,None,sogou_sl)  #添加数据
                if self.ui.checkBox_10.isChecked():  #搜狗外链
                    sogou_wl=baidu_360_sougo_wl_sl.sogou_wl(url) #sogou外部链接
                    data1+="sougos2='%s',"%(sogou_wl)
                    self.tableView_add(int_index,None,None,None,None,None,None,None,None,None,None,None,None,sogou_wl)  #添加数据
                if self.ui.checkBox_11.isChecked():  #bing收录
                    bing_sl=baidu_360_sougo_wl_sl.bing_sl(url) #bing收录数量
                    data1+="bings1='%s',"%(bing_sl)
                    self.tableView_add(int_index,None,None,None,None,None,None,None,None,None,None,None,None,None,bing_sl)  #添加数据
                if self.ui.checkBox_12.isChecked():  #bing外链
                    bing_wl=baidu_360_sougo_wl_sl.bing_wl(url) #bing外部链接
                    data1+="bings2='%s',"%(bing_wl)
                    self.tableView_add(int_index,None,None,None,None,None,None,None,None,None,None,None,None,None,None,bing_wl)  #添加数据
                if self.ui.checkBox_13.isChecked():  #百度来路ip
                    aizhan_ip=baidu_360_sougo_wl_sl.open_get_aizhan_ip(url) #获取爱站统计大概IP
                    aizhan_ip2=u"%s"%(aizhan_ip)
                    data1+="ip='%s',"%(aizhan_ip2)
                    self.tableView_add(int_index,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,aizhan_ip2)  #添加数据

                #sql_data="update url set %s where url='%s'"%(data1[0:len(data1)-1],urllib.quote(str(s0[0:len(s0)-2])))
                sql_data="update url set %s where url='%s'"%(data1[0:len(data1)-1],str(s0))
                #self.tableView_add(int_index,None,url_time2,None,None,None,baidu_sl,baidu_wl,s360_sl,s360_wl,sogou_sl,sogou_wl,bing_sl,bing_wl,aizhan_ip2)  #添加数据
                #sql_data="update url set urltime='%s',baidus1='%s',baidus2='%s',s360s1='%s',s360s2='%s',sougos1='%s',sougos2='%s',bings1='%s',bings2='%s',ip='%s' "\
                #         "where url='%s'"%(urllib.quote(str(url_time)),baidu_sl,baidu_wl,s360_sl,s360_wl,sogou_sl,sogou_wl,bing_sl,bing_wl,aizhan_ip2,urllib.quote(str(s0[0:len(s0)])))
                print sql_data
                self.sql3.mysqlite3_update(sql_data)
            except BaseException, e:
                #print(str(e))
                pass
                #self.ui.pushButton_5.setEnabled(1)
                #return 0
        self.ui.pushButton_5.setEnabled(1)

    def pushButton_6(self): #导出数据
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
                s4= model.data(model.index(int_index,4)).toString()
                s5= model.data(model.index(int_index,5)).toString()
                s6= model.data(model.index(int_index,6)).toString()
                s7= model.data(model.index(int_index,7)).toString()
                s8= model.data(model.index(int_index,8)).toString()
                s9= model.data(model.index(int_index,9)).toString()
                s10= model.data(model.index(int_index,10)).toString()
                s11= model.data(model.index(int_index,11)).toString()
                s12= model.data(model.index(int_index,12)).toString()
                s13= model.data(model.index(int_index,13)).toString()
                s14= model.data(model.index(int_index,14)).toString()
                s15= model.data(model.index(int_index,15)).toString()
                data+=s0+u"|"+s1+u"|"+s2+u"|"+\
                s3+u"|建站时间:"+s4+u"|br:"+s5+u"|pr:"+s6+u"|sr:"+s7+u"|百度收录:"+s8+u"|百度外链:"+s9+u"|360收录:"+s10+u"|360外链:"+\
                      s11+u"|搜狗收录:"+s12+u"|搜狗外链:"+s13+u"|bing收录:"+s14+u"|bing外链:"+s15
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

    def comboBox_Button(self): #查询
        #re_data=self.ui.spinBox.value() #获取内容
        re_data=str(self.ui.cx_textEdit.toPlainText()) #获取用户内容
        int_model = self.ui.tableView.selectionModel()  #获取选中编号
        if len(int_model.selectedRows())==0:
            user32.MessageBoxW(0,c_wchar_p(u"请选择有效内容xxxx"), c_wchar_p(u"提示"), 0)   # 调用MessageBoxA函数
            return
        thread.start_new_thread(self.tx_comboBox_Button,(str(re_data),))  #测试查询

    def tx_comboBox_Button(self,re_data):
        self.list=[]
        #txt_data=str(self.ui.comboBox_text.toPlainText()) #获取用户内容
#        model = self.ui.tableView.model()
#        for int_index in range(model.rowCount()):   获取全部数据
#            try:
        int_model = self.ui.tableView.selectionModel()  #获取选中编号
        model = self.ui.tableView.model()
        for index in int_model.selectedRows():       #// 对于被选中的每一行
            try:
                int_index=index.row()#获取行号
                xg_bool=False #True and False   设置个开关
                s0= model.data(model.index(int_index,0)).toString()
                s1= model.data(model.index(int_index,1)).toString()
                s2= model.data(model.index(int_index,2)).toString()
                s3= model.data(model.index(int_index,3)).toString()
                s4= model.data(model.index(int_index,4)).toString()
                s5= model.data(model.index(int_index,5)).toString()
                s6= model.data(model.index(int_index,6)).toString()
                s7= model.data(model.index(int_index,7)).toString()
                s8= model.data(model.index(int_index,8)).toString()
                s9= model.data(model.index(int_index,9)).toString()
                s10= model.data(model.index(int_index,10)).toString()
                s11= model.data(model.index(int_index,11)).toString()
                s12= model.data(model.index(int_index,12)).toString()
                s13= model.data(model.index(int_index,13)).toString()
                s14= model.data(model.index(int_index,14)).toString()
                s15= model.data(model.index(int_index,15)).toString()

                if self.comboBox_index_int==1:   #建站时间
                    ss3=str(s3)
                    if re_data=="!":
                        if str(ss3)=="!":
                            xg_bool=True
                    else:
                        if int(ss3[0:4])<=int(re_data):
                            xg_bool=True
                if self.comboBox_index_int==2:   #br
                    if int(re_data)==0:
                        if int(str(s4))==int(re_data):
                            xg_bool=True
                    else:
                        if int(str(s4))>=int(re_data):
                            xg_bool=True
                if self.comboBox_index_int==3:   #pr
#                    if re_data=="!":
#                        if str(s5)=="!":
#                            xg_bool=True
#                    else:
                    # if re_data=="!" or re_data=="?":
                    #     if str(s5)=="!" and re_data=="!":
                    #         xg_bool=True
                    #     if str(s5)=="?" and re_data=="?":
                    #         xg_bool=True
                    # else:
                    if int(str(s5))>=int(re_data):
                        xg_bool=True
                if self.comboBox_index_int==4:   #sr
                    if int(str(s6))>=int(re_data):
                        xg_bool=True
                if self.comboBox_index_int==5:   #百度收录
                    if re_data=="!":
                        if str(s7)=="!":
                            xg_bool=True
                    else:
                        if int(str(s7))>=int(re_data):
                            xg_bool=True
                if self.comboBox_index_int==6:   #百度外链
                    if re_data=="!":
                        if str(s8)=="!":
                            xg_bool=True
                    else:
                        if int(str(s8))>=int(re_data):
                            xg_bool=True
                if self.comboBox_index_int==7:   #360收录
                    if re_data=="!":
                        if str(s9)=="!":
                            xg_bool=True
                    else:
                        if int(str(s9))>=int(re_data):
                            xg_bool=True
                if self.comboBox_index_int==8:   #360外链
                    if re_data=="!":
                        if str(s10)=="!":
                            xg_bool=True
                    else:
                        if int(str(s10))>=int(re_data):
                            xg_bool=True
                if self.comboBox_index_int==9:   #搜狗收录
                    if re_data=="!":
                        if str(s11)=="!":
                            xg_bool=True
                    else:
                        if int(str(s11))>=int(re_data):
                            xg_bool=True
                if self.comboBox_index_int==10:   #搜狗外链
                    if re_data=="!":
                        if str(s12)=="!":
                            xg_bool=True
                    else:
                        if int(str(s12))>=int(re_data):
                            xg_bool=True
                if self.comboBox_index_int==11:   #bing收录
                    if re_data=="!":
                        if str(s13)=="!":
                            xg_bool=True
                    else:
                        if int(str(s13))>=int(re_data):
                            xg_bool=True
                if self.comboBox_index_int==12:   #bing外链
                    if re_data=="!":
                        if str(s14)=="!":
                            xg_bool=True
                    else:
                        if int(str(s14))>=int(re_data):
                            xg_bool=True
                if self.comboBox_index_int==13:   #百度来路ip
#                    if re_data=="!":
#                        if str(s15)=="!":
#                            xg_bool=True
#                    else:
                    if re_data=="!":
                        if str(s15)=="!":
                            xg_bool=True
                    else:
                        ss15=str(s15).split('~')
                        #print ss15
                        if int(ss15[0])>=int(re_data):
                            xg_bool=True

                s_data=","
                if xg_bool:
                    data=s0+s_data+s1+s_data+s2+s_data+s3+s_data+s4+s_data+s5+s_data+s6+s_data+s7+s_data+s8+s_data+s9+s_data+s10+s_data+\
                         s11+s_data+s12+s_data+s13+s_data+s14+s_data+s15
                    self.list.append(str(data))  #添加数据
            except BaseException, e:
                print(str(e))
        #print self.list
        #添加到表里
        idx=0
        try:
            self.del_tableView()  #清空数据
            for i in range(len(self.list)):
                data= str(self.list[i])
                line = data.split(",")
                s0=u"%s"%(line[0])
                s3=u"%s"%(line[3])
                s15=u"%s"%(line[15])
                self.tableView_add(i,s0,str(line[1]),str(line[2]),s3,str(line[4]),str(line[5]),str(line[6]),str(line[7]),str(line[8]),str(line[9]),str(line[10]),str(line[11]),str(line[12]),str(line[13]),str(line[14]),s15)  #添加数据
                idx+=1
        except BaseException, e:
            print(str(e))
            #return 0

    def pushButton_cx_xx(self): #全部选择
        self.ui.checkBox_1.setChecked( True )    #建站时间 设置复选框为选择状态
        self.ui.checkBox_2.setChecked( True )    #br
        self.ui.checkBox_3.setChecked( True )    #pr
        self.ui.checkBox_4.setChecked( True )    #sr
        self.ui.checkBox_5.setChecked( True )    #百度收录
        self.ui.checkBox_6.setChecked( True )    #百度外链
        self.ui.checkBox_7.setChecked( True )    #360收录
        self.ui.checkBox_8.setChecked( True )    #360外链
        self.ui.checkBox_9.setChecked( True )    #搜狗收录
        self.ui.checkBox_10.setChecked( True )    #搜狗外链
        self.ui.checkBox_11.setChecked( True )    #bing收录
        self.ui.checkBox_12.setChecked( True )    #bing外链
        self.ui.checkBox_13.setChecked( True )    #百度来路ip

    def pushButton_7(self): #显示成功webshell
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
            s3=u"%s"%(urllib.unquote(str(line[3])))
            s15=u"%s"%(str(line[15]))
            self.tableView_add(int_id,s0,str(line[1]),str(line[2]),s3,str(line[4]),str(line[5]),str(line[6]),str(line[7]),str(line[8]),str(line[9]),str(line[10]),str(line[11]),str(line[12]),str(line[13]),str(line[14]),s15)  #添加数据
            int_id+=1
        cur.close()  #关闭游标

    def pushButton_8(self): #显示失败webshell
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
            s3=u"%s"%(urllib.unquote(str(line[3])))
            s15=u"%s"%(str(line[15]))
            self.tableView_add(int_id,s0,str(line[1]),str(line[2]),s3,str(line[4]),str(line[5]),str(line[6]),str(line[7]),str(line[8]),str(line[9]),str(line[10]),str(line[11]),str(line[12]),str(line[13]),str(line[14]),s15)  #添加数据
            int_id+=1
        cur.close()  #关闭游标

if __name__ == "__main__":
    baidu_br=br_pr_sogo.baidu_br(br_pr_sogo.get_domain(str("http://www.baidu.com///upload/20150118182027.php|autoshell|ok|null|0|5|1|218.65.17.105/江西省上饶市横峰县-|2015-02-15 00:01:06|2015-02-01 00:30:27"),0))
    print baidu_br
