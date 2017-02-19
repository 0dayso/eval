#!/usr/local/bin/python
#-*- coding: UTF-8 -*-

import re,httplib
import gzip,StringIO
import socket
import urllib
socket.setdefaulttimeout(10)

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#def url_www(url_data): #提取主域名
#    try:
#
#    except Exception,e:
#        #print e
#        return "www null"

def URL_TQURL2(data): #URL提取URL
    try:  #127.0.0.1:8888
        data +="/"      #data ="https://www.baidu.com/cache/sethelp/index.html"
        if ~data.find("http://"):  #~取反
            data=data[7:] #字符串删除
            nPos = data.index('/') #查找字符        #print nPos
            sStr1 = data[0:nPos] #复制指定长度的字符
            return sStr1

        if ~data.find("https://"):  #~取反
            data=data[8:] #字符串删除
            nPos = data.index('/') #查找字符
            #print nPos
            sStr1 = data[0:nPos] #复制指定长度的字符
            return sStr1

    except:
        #print "Thread:%d-CS_openurl-Extract URL:%s URL error"%\
        #      (self.Ht,data)
        return "www null"

import urllib2
def open_url_read(url):  #返回页面内容
    try:
        req = urllib2.Request(url)
        req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
        s = urllib2.urlopen(req,timeout=10)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
        return s.read()
    except:
        return 0

def URL_DZ(data,re_data):  #遍历页里的地址
    try:
        p = re.compile(re_data)
        sarr = p.findall(data)
        if len(sarr)>=1:
            return 1
        return 0
    except:
        return 0

if __name__ == "__main__":
    url="http://127.0.0.1:8888/long.php"
    url_data=open_url_read("http://"+URL_TQURL2(url)+"/web.txt")
    if url_data:
        print URL_DZ(url_data,r'long')
#    yijuhua_cs("php","http://127.0.0.1:8888/long.php","long") #ASP还是PHP  ,URL地址 ，密码
#    print URL_TQURL2("http://127.0.0.1:8888/long.php") #URL提取URL
