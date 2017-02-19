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
#user32.MessageBoxW(0,c_wchar_p("1111111"), c_wchar_p("QQ:23456789"), 0)   # 调用MessageBoxA函数
import yijuhua
import thread
import Csqlite3  #数据库操作
import qqwry  #网址返回  IP和物理地址
import br_pr_sogo #获取网站权重  br
import g  #公用文件
import urllib #转换成网络格式
#共0条--OK0条--NO0条--等待测试0条
yu_1=0  #共多少数据
yu_2=0  #成功多少条
yu_3=0  #失败多少条

class   top_1(object):
    def __init__(self,ui,model):
        self.ui=ui
        self.model=model
        #数据库链接
        self.sql3=Csqlite3.C_sqlite3()
        self.sql3.mysqlite3_open()
        self.comboBox_index_int=0 #保存用户选择的ID

    def comboBox_index(self,data):
        self.comboBox_index_int=data

    def open_file(self,data): #格式化
        ss = data.split("|")
        #if len(ss)<=3:
        return ss[0],ss[1]
        #return 0

    #获取脚本文件的当前路径
    def cur_file_dir(self):
        #获取脚本路径
        path = sys.path[0]
        #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
        if os.path.isdir(path):
            return path
        elif os.path.isfile(path):
            return os.path.dirname(path)

#    def dr_yih_thread(self):
#        thread.start_new_thread(self.dr_yjh_Button,())

    def dr_yjh_Button(self): #导入一句话

        global yu_1
        dlg = QFileDialog(None)
        self.saveHistoryFilename = dlg.getOpenFileName()
        from os.path import isfile
        if isfile(self.saveHistoryFilename):
            #import codecs
            #text = codecs.open(self.saveHistoryFilename,'r','utf-8').read()
            #print self.saveHistoryFilename
            xxx = file(self.saveHistoryFilename, 'r')
            i=0
            self.ui.maim_pushButton_1.setEnabled(0)  #给改成禁用
            for xxx_line in xxx.readlines():
                try:
                    data=xxx_line.strip().lstrip().rstrip('\n')
                    s0,s1=self.open_file(data)
                    if len(s0)>7:
                        data_time2=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
                        data_time=time.mktime(time.strptime(data_time2,'%Y-%m-%d %H:%M:%S'))  #转化成时间戳
                        sql_data="insert into shell(urls1,passwods2,time1s6) VALUES('%s','%s','%s')"%(urllib.quote(str(s0.rstrip('\n'))),str(s1.strip().lstrip().rstrip('\n')),data_time)
                        self.sql3.mysqlite3_insert(sql_data)
                        #if self.sql3.mysqlite3_insert(sql_data): #添加数据
                        self.tableView_add(i,str(s0.rstrip('\n')),str(s1.strip().lstrip().rstrip('\n')),None,None,None,None,None,None,data_time2,None)  #添加数据
                        i+=1
                except BaseException, e:
                    print(str(e))
                yu_1=i  #共多少数据
            self.ui.messagebox.append(u"已经导入 %d 条 一句话"%(i))
            self.ui.maim_pushButton_1.setEnabled(1)

    #添加数据
    #u'1一句话地址',u'2密码',u'3状态',u'4操作系统',u'5上传URL路径',u'6访问URL路径',u'7IP/地址位置'
    def tableView_add(self,ints,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10):  #添加数据
        try:
            #红色：(255,0,0)
            #绿色：(0,255,0)
            global yu_1,yu_2,yu_3

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

#            data4=u"<html><head/><body><p align="+u"center"+u">共:%d条--OK:%d条--NO:%d条--等待测试:%d条</p></body></html>"%(yu_1,yu_2,yu_3,yu_1-(yu_2+yu_3))
#            self.ui.label_4.setText(data4)
        except BaseException, e:
            print(str(e))
            #        self.model.setSortRole(0) #排序
            #        self.model.sort(3,Qt.AscendingOrder) #排序  排序只针对INT型
        self.ui.SQLite_tableView.setModel(self.model)

    def Button_2(self):  #测试一句话\n(并存入数据库)
        int_model = self.ui.SQLite_tableView.selectionModel()  #获取选中编号
        if len(int_model.selectedRows())==0:
            self.ui.messagebox.append(u"=========================")
            self.ui.messagebox.append(u"提示:请选择要测的一句话")
            user32.MessageBoxW(0,c_wchar_p(u"请选择有效内容"), c_wchar_p(u"提示"), 0)   # 调用MessageBoxA函数
            return
#        int_id=0
#        for index in int_model.selectedRows():       #// 对于被选中的每一行
#            int_id+=1
#        if int_id<1:
#            self.ui.messagebox.append(u"=========================")
#            self.ui.messagebox.append(u"提示:请选择要测的一句话")
#            return 0
        thread.start_new_thread(self.yjh_cs_2,())  #测试一句话是否连接成功

    def yjh_cs_2(self):  #测试一句话是否连接成功
        global yu_2,yu_3
        self.ui.main_pushButton_2.setEnabled(0)  #给改成禁用
        int_model = self.ui.SQLite_tableView.selectionModel()  #获取选中编号
        model = self.ui.SQLite_tableView.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
        h=qqwry.C_hoset()

        for index in int_model.selectedRows():       #// 对于被选中的每一行
            try:
                int_index=index.row()#获取行号
                s0= model.data(model.index(int_index,0)).toString()
                s1= model.data(model.index(int_index,1)).toString()
                data_time2=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
                data_time=time.mktime(time.strptime(data_time2,'%Y-%m-%d %H:%M:%S'))  #转化成时间戳
                if s0=="" or len(s0)<=7:
                    yu_3+=1  #失败多少条
                    self.tableView_add(int_index,None,None,u"null",None,None,None,None,None,None,data_time2)  #添加数据
                    sql_data="update shell set zts3='null',time2s7='%s' where urls1='%s' and passwods2='%s'"%(data_time,str(s0),str(s1))
                    self.sql3.mysqlite3_update(sql_data)
                    continue  #跳过

                #                url="http://www.sttc.cn/uploadfile/2013/0621/thumb_6_6_.Php.JPG%20%20%20%20%20%20%20Php"
                #                PASS="long"
                if yijuhua.yijuhua_cs(g.bool_asp_php(s0),str(s0),str(s1)):
                    yu_2+=1  #成功多少条
                    #self.tableView_add(int_index,None,None,u"ok",None,None,None,data_time)  #添加数据
                    #sql_data="update shell set zts3='ok',time2s7='%s' where urls1='%s' and passwods2='%s'"%(data_time,str(s0),str(s1))
                    #yijuhua_win_linux(url,PASS): #URL地址 ，密码   返回操作系统
                    win_linux=yijuhua.yijuhua_win_linux(str(s0),str(s1))  #URL地址 ，密码   返回操作系统
                    WLWZ=h.www_data(qqwry.url_www(str(s0)))
                    WLWZ=u"%s"%(WLWZ)
                    if g.bool_asp_php(str(s0))=="asp":
                        win_linux="WinNT"
                    self.tableView_add(int_index,None,None,u"ok",str(win_linux),None,None,None,WLWZ,None,data_time2)  #添加数据
                    sql_data="update shell set zts3='ok',oss4='%s',ips5='%s',time2s7='%s' where urls1='%s' and passwods2='%s'"%(str(win_linux),WLWZ,data_time,str(s0),str(s1))
                else:
                    yu_3+=1  #失败多少条
                    self.tableView_add(int_index,None,None,u"No",u"No",None,None,None,None,None,data_time2)  #添加数据
                    sql_data="update shell set zts3='No',oss4='No',time2s7='%s' where urls1='%s' and passwods2='%s'"%(data_time,str(s0),str(s1))
                self.sql3.mysqlite3_update(sql_data)

            except BaseException, e:
                print(str(e))
                self.ui.main_pushButton_2.setEnabled(1)
                return 0
        self.ui.messagebox.append(u"=========================")
        self.ui.messagebox.append(u"手动测试一句话 完成")
        self.ui.main_pushButton_2.setEnabled(1)

    def time_localtime(self,data):  #时间戳转换成日期
        try:
            #return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(line[8]))
            ltime=time.localtime(float(data))
            return time.strftime("%Y-%m-%d %H:%M:%S", ltime)
        except BaseException, e:
            #print(str(e))
            return "--"

    def SQLite_Button_1(self):  #显示全部数据
        self.del_tableView()  #清空数据
        sql_data = "select * from shell order by time1s6 DESC"   # asc 表示升序 , desc表示降序
        self.sql3.conn.commit()# 获取到游标对象
        cur = self.sql3.conn.cursor()# 用游标来查询就可以获取到结果
        cur.execute(sql_data)# 获取所有结果
        res = cur.fetchall()  #从结果中取出所有记录
        int_id=0
        for line in res:
            #self.url_data=line[0]
            ips5=u"%s"%(line[7])
            self.tableView_add(int_id,str(line[0]),str(line[1]),str(line[2]),str(line[3]),str(line[4]),str(line[5]),str(line[6]),ips5,self.time_localtime(line[8]),self.time_localtime(line[9]))  #添加数据
            int_id+=1
        cur.close()  #关闭游标
        self.ui.messagebox.append(u"=========================")
        self.ui.messagebox.append(u"显示全部数据  %d条一句话"%len(res))

    def re_cx_data(self,re_data,data):  #正则查询内容是否存在
        p = re.compile( r'%s'%re_data )
        sarr = p.findall(data)
        if len(sarr)>=1: #数据存在
            return True
        else:
            return False

    def comboBox_Button_sql(self):
        self.list=[]
        txt_data=str(self.ui.comboBox_text.toPlainText()) #获取用户内容
        model = self.ui.SQLite_tableView.model()
        for int_index in range(model.rowCount()):
            try:
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

                if self.comboBox_index_int==0:   #一句话地址
                    if self.re_cx_data(txt_data,str(s0)):
                        xg_bool=True
                if self.comboBox_index_int==1:   #密码
                    if self.re_cx_data(txt_data,str(s1)):
                        xg_bool=True
                if self.comboBox_index_int==2:   #状态
                    if self.re_cx_data(txt_data,str(s2)):
                        xg_bool=True
                if self.comboBox_index_int==3:   #操作系统
                    if self.re_cx_data(txt_data,str(s3)):
                        xg_bool=True
                if self.comboBox_index_int==4:   #br
                    if self.re_cx_data(txt_data,str(s4)):
                        xg_bool=True
                if self.comboBox_index_int==5:   #pr
                    if self.re_cx_data(txt_data,str(s5)):
                        xg_bool=True
                if self.comboBox_index_int==6:   #Sogou
                    if self.re_cx_data(txt_data,str(s6)):
                        xg_bool=True
                if self.comboBox_index_int==7:   #IP/地址位置
                    if self.re_cx_data(txt_data,str(s7)):
                        xg_bool=True
                if xg_bool:
                    data=s0+"|"+s1+"|"+s2+"|"+s3+"|"+s4+"|"+s5+"|"+s6+"|"+s7+"|"+s8+"|"+s9
                    self.list.append(str(data))  #添加数据
            except BaseException, e:
                print(str(e))

        #添加到表里
        idx=0
        try:
            self.del_tableView()  #清空数据
            for i in range(len(self.list)):
                data= str(self.list[i])
                line = data.split("|")
                ips5=u"%s"%(line[7])
                self.tableView_add(i,str(line[0]),str(line[1]),str(line[2]),str(line[3]),str(line[4]),str(line[5]),str(line[6]),ips5,str(line[8]),str(line[9]))  #添加数据
                idx+=1
        except BaseException, e:
            print(str(e))
            return 0
        self.ui.messagebox.append(u"筛选内容:%s  共筛选出%d条"%(txt_data,idx))



#        sql_data=""
#        txt_data=str(self.ui.comboBox_text.toPlainText()) #获取用户内容
#        if self.comboBox_index_int==0:   #一句话地址
#            sql_data="select * from shell where urls1 like '%%%s%%'"%(txt_data)
#        if self.comboBox_index_int==1:   #密码
#            sql_data="select * from shell where passwods2 like '%%%s%%'"%(txt_data)
#        if self.comboBox_index_int==2:   #状态
#            sql_data="select * from shell where zts3 like '%%%s%%'"%(txt_data)
#        if self.comboBox_index_int==3:   #操作系统
#            sql_data="select * from shell where oss4 like '%%%s%%'"%(txt_data)
#        if self.comboBox_index_int==4:   #br
#            sql_data="select * from shell where br like '%%%s%%'"%(txt_data)
#        if self.comboBox_index_int==5:   #pr
#            sql_data="select * from shell where pr like '%%%s%%'"%(txt_data)
#        if self.comboBox_index_int==6:   #Sogou
#            sql_data="select * from shell where sogo like '%%%s%%'"%(txt_data)
#        if self.comboBox_index_int==7:   #IP/地址位置
#            sql_data="select * from shell where name ips5 '%%%s%%'"%(txt_data)
#
#        #if not sql_data=="":
#        self.del_tableView()  #清空数据
#        #print "sql",sql_data
#        self.sql3.conn.commit()# 获取到游标对象
#        cur = self.sql3.conn.cursor()# 用游标来查询就可以获取到结果
#        cur.execute(sql_data)# 获取所有结果
#        res = cur.fetchall()  #从结果中取出所有记录
#        int_id=0
#        for line in res:
#            #self.url_data=line[0]
#            ips5=u"%s"%(line[7])
#            self.tableView_add(int_id,str(line[0]),str(line[1]),str(line[2]),str(line[3]),str(line[4]),str(line[5]),str(line[6]),ips5,self.time_localtime(line[9]),self.time_localtime
#                (line[8]))  #添加数据
#            int_id+=1
#        cur.close()  #关闭游标
#        self.ui.messagebox.append(u"=========================")
#        self.ui.messagebox.append(u"成功查询数据  %d条数据"%len(res))


    def del_tableView(self):  #清空数据
        model = self.ui.SQLite_tableView.model()
        int_id=self.ui.SQLite_tableView.model().rowCount()
        for i in range(int_id,-1,-1):
            model.removeRow(i)

    def SQLite_Button_2(self):  #显示一句话成功数据
        self.del_tableView()  #清空数据
        sql_data = "select * from shell where zts3='ok' order by time2s7 DESC"   # asc 表示升序 , desc表示降序
        self.sql3.conn.commit()# 获取到游标对象
        cur = self.sql3.conn.cursor()# 用游标来查询就可以获取到结果
        cur.execute(sql_data)# 获取所有结果
        res = cur.fetchall()  #从结果中取出所有记录
        int_id=0
        for line in res:
            #self.url_data=line[0]
            ips5=u"%s"%(line[7])
            self.tableView_add(int_id,str(line[0]),str(line[1]),str(line[2]),str(line[3]),str(line[4]),str(line[5]),str(line[6]),ips5,self.time_localtime(line[9]),self.time_localtime(line[8]))  #添加数据
            int_id+=1
        cur.close()  #关闭游标
        self.ui.messagebox.append(u"=========================")
        self.ui.messagebox.append(u"显示一句话成功数据  %d条一句话"%len(res))

    def Button_3(self):  #测试权重  PR
        int_model = self.ui.SQLite_tableView.selectionModel()  #获取选中编号
        if len(int_model.selectedRows())==0:
            self.ui.messagebox.append(u"=========================")
            self.ui.messagebox.append(u"提示:请选择要测的URL")
            user32.MessageBoxW(0,c_wchar_p(u"请选择有效内容"), c_wchar_p(u"提示"), 0)   # 调用MessageBoxA函数
            return
        thread.start_new_thread(self.br_pr_sogo_3,())  #测试一句话是否连接成功

    def br_pr_sogo_3(self):  #获取 百度 谷歌  搜狗  权重
        self.ui.main_pushButton_3.setEnabled(0)  #给改成禁用
        int_model = self.ui.SQLite_tableView.selectionModel()  #获取选中编号
        model = self.ui.SQLite_tableView.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
        for index in int_model.selectedRows():       #// 对于被选中的每一行
            try:
                int_index=index.row()#获取行号
                s0= model.data(model.index(int_index,0)).toString()
                s1= model.data(model.index(int_index,1)).toString()
                #s0=br_pr_sogo.get_domain(str(s0),0)
                baidu_br=br_pr_sogo.baidu_br(br_pr_sogo.get_domain(str(s0),0))
                if int(baidu_br)<=0:
                    #print "0000000000000000000000000"
                    baidu_br=br_pr_sogo.aizhan_br(br_pr_sogo.get_domain(str(s0),0))
                google_pr=br_pr_sogo.google_pr(s0)
                sogo=br_pr_sogo.sogo(br_pr_sogo.get_domain(str(s0),0))
                self.tableView_add(int_index,None,None,None,None,baidu_br,google_pr,sogo,None,None,None)  #添加数据
                sql_data="update shell set br='%s',pr='%s',sogo='%s' where urls1='%s' and passwods2='%s'"%(baidu_br,google_pr,sogo,urllib.quote(str(s0[0:len(s0)-2])),str(s1))
                #print sql_data
                self.sql3.mysqlite3_update(sql_data)
            except BaseException, e:
                print(str(e))
                self.ui.main_pushButton_3.setEnabled(1)
                return 0
        self.ui.messagebox.append(u"=========================")
        self.ui.messagebox.append(u"获取 百度 谷歌 搜狗 权重 完成")
        self.ui.main_pushButton_3.setEnabled(1)

    def SQLite_Button_3(self):  #显示一句话失败数据
        self.del_tableView()  #清空数据
        sql_data = "select * from shell where zts3 is null or zts3='No' order by time2s7 DESC"   # asc 表示升序 , desc表示降序  #select * from shell where zts3='no' or zts3='None'
        self.sql3.conn.commit()# 获取到游标对象
        cur = self.sql3.conn.cursor()# 用游标来查询就可以获取到结果
        cur.execute(sql_data)# 获取所有结果
        res = cur.fetchall()  #从结果中取出所有记录
        int_id=0
        for line in res:
            #self.url_data=line[0]
            ips5=u"%s"%(line[7])
            self.tableView_add(int_id,str(line[0]),str(line[1]),str(line[2]),str(line[3]),str(line[4]),str(line[5]),str(line[6]),ips5,self.time_localtime(line[9]),self.time_localtime(line[8]))  #添加数据
            int_id+=1
        cur.close()  #关闭游标
        self.ui.messagebox.append(u"=========================")
        self.ui.messagebox.append(u"显示一句话失败数据  %d条一句话"%len(res))


    def SQLite_Button_4(self):  #导出选择的一句话
        int_model = self.ui.SQLite_tableView.selectionModel()  #获取选中编号
        model = self.ui.SQLite_tableView.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
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
                data+=s0+"|"+s1+"|"+s2+"|"+s3+"|"+s4+"|"+s5+"|"+s6+"|"+s7+"|"+s8+"|"+s9
                data+="\n"
            except BaseException, e:
                print(str(e))
#        print data
        data_time=time.strftime('%Y-%m-%d',time.localtime(time.time()))
        dlg = QFileDialog(None)
        self.filename = dlg.getSaveFileName(None,u"保存WEBSHELL", u"./"+data_time+u"WEBSHELL.txt",u"txt (*.txt)")
        #print self.filename
        file_object = open(self.filename, 'w')
        file_object.writelines(data)
        file_object.close()

    def SQLite_Button_5(self):  #删除选择的一句话
        int_model = self.ui.SQLite_tableView.selectionModel()  #获取选中编号
        model = self.ui.SQLite_tableView.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
        if len(int_model.selectedRows())==0:
            user32.MessageBoxW(0,c_wchar_p(u"请选择有效内容"), c_wchar_p(u"提示"), 0)   # 调用MessageBoxA函数
            return
        for index in int_model.selectedRows():       #// 对于被选中的每一行
            try:
                int_index=index.row()#获取行号
                s0= model.data(model.index(int_index,0)).toString()
                s1= model.data(model.index(int_index,1)).toString()
                sql_data="delete from shell where urls1='%s' and passwods2='%s'"%(str(s0),str(s1))
                self.sql3.mysqlite3_delete(sql_data)
            except BaseException, e:
                print(str(e))
        self.SQLite_Button_1()  #显示一句话成功数据