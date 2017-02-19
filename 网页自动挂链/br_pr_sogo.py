#!/usr/local/bin/python
#-*- coding: UTF-8 -*-

import urllib2
import re

def url_post(url):
    try:
        req = urllib2.Request(url)
        req.add_header('User-Agent', "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.nml)")
        s = urllib2.urlopen(req, timeout=5)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
        return s.read()
    except:
        return ""

#获取百度权重
def baidu_br(url):
    try:
        baidu="http://mytool.chinaz.com/baidusort.aspx?host=%s"%(url)
        data=url_post(baidu)
        p = re.compile(r'<font color="blue">(.*?)</font>')
        # 找出一条一条的<a></a>标签
        sarr = p.findall(data)
        if len(sarr)>=1:
            return sarr[0]
        else:
            return 0
    except:
        return 0

def sogo(url):
    try:
        sogo="http://rank.ie.sogou.com/sogourank.php?url=%s"%(url)
        data=url_post(sogo)
        p = re.compile(r'sogourank=(.*?)$')
        # 找出一条一条的<a></a>标签
        sarr = p.findall(data)
        if len(sarr)>=1:
            return sarr[0]
        else:
            return "-"
    except:
        return "--"

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

def hash_url(url):
    try:
        SEED = "Mining PageRank is AGAINST GOOGLE'S TERMS OF SERVICE. Yes, I'm talking to you, scammer."
        Result = 0x01020345
        for i in range(len(url)) :
            Result ^= ord(SEED[i%len(SEED)]) ^ ord(url[i])
            Result = Result >> 23 | Result << 9
            Result &= 0xffffffff
        return '8%x' % Result
    except:
        pass

def google_pr(url):
    try:
        PR_CH=hash_url(get_domain(url,0))
        google="http://toolbarqueries.google.com/tbr?client=navclient-auto&features=Rank&q=info:%s&ch=%s"%(get_domain(url,0),PR_CH)
        #print google
        data=url_post(google)
        data=data.strip().lstrip().rstrip('')
        data=data[len(data)-1:len(data)]
        if int(data)>=1:
            return data
        else:
            return "-"
    except:
        return "--"

def aizhan_br(url): #从爱站获取权重
    try:
        aizhan="http://www.aizhan.com/getbr.php?url=%s&style=1"%(url)
        data=url_post(aizhan)
        p = re.compile(r'>(.*?)</a>')
        # 找出一条一条的<a></a>标签
        sarr = p.findall(data)
        if int(sarr[0])>=0:
            return sarr[0]
        else:
            return "-"
    except:
        return "--"

if __name__ == "__main__":
    www="http://www.baidu.com"
    #www=get_domain(str(www),0)
#    print google_pr(get_domain(str(www),0))
#    print baidu_br(get_domain(str(www),0))
#    print sogo(get_domain(str(www),1))
    print aizhan_br(get_domain(str(www),0))










