#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
import urllib
import urllib2
import time

def Aurl_post(URL):  #提交内容
    try:
        req = urllib2.Request(URL)
        #req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
        urllib2.urlopen(req,timeout=20)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
        #urllib2.urlopen(URL,timeout=20)  # 后门POST提交   超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
        return 1
    except:
        return 0

def ping_seo(url):
    try:
        xxx = file("data/ping.txt", 'r')  #关键字
        for xxx_line in xxx.readlines():
            data=xxx_line.strip().lstrip()  #添加数据+"\r\n"
            data=data.replace('$url',urllib.quote(url))
            print data
            Aurl_post(data)  #提交内容
    except:
        return 0

if __name__=='__main__':
    ping_seo("http://19900521.com/book/Jeo/index.html")





