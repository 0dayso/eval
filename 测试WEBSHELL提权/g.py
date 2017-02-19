#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#BY: QQ292925842
#公用函数
import time
import socket
socket.setdefaulttimeout(10)  #设置了全局默认超时时间
from ctypes import *
# user32 = windll.LoadLibrary('user32.dll')               # 加载动态链接库

import re
import datetime
datetime.datetime.now()
#reload(sys)
#sys.setdefaultencoding('utf-8')

def re_data(data): #正则返回的结果
    try:
        #p = re.compile( r'->\|(.*?)\|<-')
        p = re.compile( r'->\|([\s\S]*?)\|<-')
        sarr = p.findall(data)
        #print sarr
        if len(sarr[0])>=1:
            #print "aaa"
            return sarr[0]
        return 0
    except Exception,e:
        #print e
        return 0

def asp_aspx_php_htm_html(s0): #查看文件格式
    try:
        if (".asp" in str(s0) or ".ASP" in str(s0) or ".Asp" in str(s0)):
            return "asp"
        if (".aspx" in str(s0) or ".ASPx" in str(s0) or ".Aspx" in str(s0)):
            return "aspx"
        if (".php" in str(s0) or ".PHP" in str(s0) or ".Php" in str(s0)):
            return "php"
        if (".htm" in str(s0) or ".HTM" in str(s0) or ".Htm" in str(s0)):
            return "htm"
        if (".html" in str(s0) or ".HTML" in str(s0) or ".Html" in str(s0)):
            return "html"
        return "null"
    except Exception,e:
        #print e
        return "null"

def bool_asp_php(s0): #查看一句话是语句的一句话
    try:
        if (".asp" in str(s0) or ".ASP" in str(s0) or ".Asp" in str(s0)):
            return "asp"
        if (".php" in str(s0) or ".PHP" in str(s0) or ".Php" in str(s0)):
            return "php"
        return "null"
    except Exception,e:
        #print e
        return "null"

#取消注释
def file_index(data, file_data):  #查找字符串是否存在
    if file_data in data:
        return True
    else:
        return False

def string_index(data,file_data):
    nPos = data.find(file_data) #查找字符        #print nPos
    #return data[0:nPos] #复制指定长度的字符
    return "%s\n"%(data[0:nPos])

def PHP_x1_zs(file_data): #清除注释/*   */
    data=""
    p = re.compile( r'.+?\n')
    sarr = p.findall(file_data)
    zs=0  #注释标记
    for every in sarr:
        if file_index(every,"/*"):
            zs=1
        if file_index(every,"*/"):
            zs=0
            continue#终止本次
        if zs==0:
            data+=every
    return data

def PHP_x2_zs(file_data): #清除//注释
    data=""
    p = re.compile( r'.+?\n')
    sarr = p.findall(file_data)
    for every in sarr:
        if file_index(every,"//"):
            every=string_index(every,"//") #截取字符串
        data+=every
    return data

def PHP_x0_zs(file_data): #清除注释<?php   ?>
    data=""
    p = re.compile( r'.+?\n')
    sarr = p.findall(file_data)
    zs=0  #注释标记
    for every in sarr:
        if not (file_index(every,"<?php") or file_index(every,"?>")):
            data+=every
            #        if not file_index(every,"?>"):
            #            data+=every
    return data

def open_file_null(file_data):  #清除空行
    data=""
    p = re.compile( r'.+?\n')
    sarr = p.findall(file_data)
    for every in sarr:
        if every.split():
            data+=every.lstrip().rstrip().strip().rstrip('\n')
    return data

def QC_PHP(PHP_data):  #清除PHP中没有用的数据
    PHP_data=PHP_x0_zs(PHP_data)  #清除注释<?php   ?>
    PHP_data=PHP_x1_zs(PHP_data)  #清除注释/*   */
    PHP_data=PHP_x2_zs(PHP_data)  #清除//注释
    PHP_data=open_file_null(PHP_data)     #清除空行
    return PHP_data

def get_domain(data,bool=0):
    # URL提取URL
    try:
        data += "/"      #data ="https://www.baidu.com/cache/sethelp/index.html"
        #bool=0   #0不带HTTP   1带HTTP
        if data.find("http://") == 0:
            data = data[7:] #字符串删除
            nPos1 = data.index('/') # 查找字符
            if bool==0:
                return data[0:nPos1]   # 复制指定长度的字符
            else:
                return "%s%s"%("http://",data[0:nPos1])   # 复制指定长度的字符
        if data.find("https://") == 0:
            data = data[8:]  # 字符串删除
            nPos2 = data.index('/') #查找字符
            #return data[0:nPos] #复制指定长度的字符
            if bool==0:
                return data[0:nPos2]   # 复制指定长度的字符
            else:
                return "%s%s"%("https://",data[0:nPos2])   # 复制指定长度的字符
    except:
        pass

def ww_path(www,path1,path2):
    path1=str(path1)
    path2=str(path2)
    url=www+path2[len(path1)-1:len(path2)]
    return url.replace('\\','/')

def www_http_z(data):  #返回是否是主目录
    try:
        data = data[8:] #字符串删除
        nPos1 = data.index('/') # 查找字符
        data = data[nPos1:]   # 复制指定长度的字符
        #return len(data)  #index.html   11
        if len(data)<=11:
            return 0
        else:
            return 1
    except:
        return 0

def utf_8_B(name,data):  #编码
    try:
        if name=="gbk":
            return "ok",data.encode('gbk',"ignore")
        if name=="utf-8":
            return "ok",data.encode('utf-8',"ignore")
        if name=="gb2312":
            return "ok",data.encode('gb2312',"ignore")
        return "no",""
#        if name=="gbk":
#            return "ok",data.encode('gbk')
#        if name=="utf-8":
#            return "ok",data.encode('utf-8')
#        if name=="gb2312":
#            return "ok",data.encode('gb2312')
#        return "no",""
    except Exception,e:
        print "utf_8_B",e
        return "no",""

def utf_8_G(data):  #解码
    try:
        try:
            return "gbk",data.decode('gbk')
        except Exception,e:
            #print e
            pass
        try:
            return "utf-8",data.decode('utf-8')
        except Exception,e:
            #print e
            pass
        try:
            return "gb2312",data.decode('gb2312')
        except Exception,e:
            #print e
            pass
    except Exception,e:
        print "utf_8_G",e
        pass


if __name__ == "__main__":
    print asp_aspx_php_htm_html("2121212nihao asp/asasa.h")
    #print ww_path(get_domain("http://www.dsolab.com/celive/uploadfiles/CELIVE-5GLFuOKKQF.php;.jpg",1),"D:/wamp/www/","D:/wamp/www/conn.php")
    #print get_domain("http://www.dsolab.com/celive/uploadfiles/CELIVE-5GLFuOKKQF.php;.jpg",1)
    #print bool_asp_php("http://www.dsolab.com/celive/uploadfiles/CELIVE-5GLFuOKKQF.php;.jpg")