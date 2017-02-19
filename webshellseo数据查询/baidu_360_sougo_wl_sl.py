#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#查询_外链收录\n(百度_360_搜狗)
import urllib2
import re

def url_post(url):
    try:
        req = urllib2.Request(url)
        #req.add_header('User-Agent', "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.nml)")
        req.add_header('User-Agent','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; BOIE9;ZHCN)')
        s = urllib2.urlopen(req, timeout=5)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
        return s.read()
    except:
        return ""

def url_data_re(url):
    try:
        ss=url_post(url)
        if ss==0:  #读取网页内容
            #print u"获取内容失败"
            #time.sleep(2)
            return "?"
            #print ss
        p = re.compile(r"该网站共有<b style=\"color:#333\">(.*?)</b>个")
        sarr = p.findall(ss)#找出一条百度
        if len(sarr) >0:  #None 也是假。
            return str(sarr[0]).strip().lstrip().replace(',','')

        p = re.compile(r"百度为您找到相关结果约(.*?)个")
        sarr = p.findall(ss)#找出一条百度
        if len(sarr) >0:  #None 也是假。
            return str(sarr[0]).strip().lstrip().replace(',','')

        p = re.compile(r"百度为您找到相关结果(.*?)个")
        sarr = p.findall(ss)#找出一条百度
        if len(sarr) >0:
            return str(sarr[0]).strip().lstrip().replace(',','')
            #=====goog.hk  获取不到数据

        p = re.compile(r'<span class="sb_count">(.*?)条结果</span>')
        sarr = p.findall(ss)#找出一条bing
        if len(sarr) >0:
            return str(sarr[0]).strip().lstrip().replace(',','')

        p = re.compile(r"找到相关结果约(.*?)个")
        sarr = p.findall(ss)#找出一条so360
        if len(sarr) >0:
            return str(sarr[0]).strip().lstrip().replace(',','')

        p = re.compile(r'找到约 <span id="scd_num">(.*?)</span>')
        sarr = p.findall(ss)#找出一条sogou
        if len(sarr) >0:
            return str(sarr[0]).strip().lstrip().replace(',','')

        p = re.compile(r'找到约 <em>(.*?)</em>')
        sarr = p.findall(ss)#找出一条sogou
        if len(sarr) >0:
            return str(sarr[0]).strip().lstrip().replace(',','')

        p = re.compile(r'找到约<resnum id="scd_num">(.*?)</resnum>')
        sarr = p.findall(ss)#找出一条sogou
        if len(sarr) >0:
            return str(sarr[0]).strip().lstrip().replace(',','')

        return "!"
    except:
        return "="

def baidu_sl(url): #百度收录数量
    try:
        url="http://www.baidu.com/s?wd=site:%s"%(url)
        return url_data_re(url)
    except:
        return 0

def baidu_wl(url): #百度外部链接
    try:
        url="http://www.baidu.com/s?wd=domain:%s"%(url)
        return url_data_re(url)
    except:
        return 0

def s360_sl(url): #360收录数量
    try:
        url="http://www.haosou.com/s?q=site:%s"%(url)
        return url_data_re(url)
    except:
        return 0

def s360_wl(url): #360外部链接
    try:
        url="http://www.haosou.com/s?q=\"%s\""%(url)
        return url_data_re(url)
    except:
        return 0

def sogou_sl(url): #sogou收录数量
    try:
        url="http://www.sogou.com/web?query=site:%s"%(url)
        return url_data_re(url)
    except:
        return 0

def sogou_wl(url): #sogou外部链接
    try:
        url="http://www.sogou.com/web?&query=\"%s\""%(url)
        return url_data_re(url)
    except:
        return 0

def bing_sl(url): #bing收录数量
    try:
        url="http://cn.bing.com/search?q=site:%s"%(url)
        return url_data_re(url)
    except:
        return 0

def bing_wl(url): #bing外部链接
    try:
        url="http://cn.bing.com/search?q=\"%s\""%(url)
        return url_data_re(url)
    except:
        return 0

#ahrefs反向链接
def ahrefs_fl(url):  #反链查询
    ss=url_post(url)
    if ss==0:  #读取网页内容
        #print u"获取内容失败"
        #time.sleep(2)
        return "?"
        #print ss
    p = re.compile(r"onClick=\"ClearInfoAndDataTable();\">(.*?)</a>")
    sarr = p.findall(ss)#找出一条百度
    if len(sarr) >0:  #None 也是假。
        return str(sarr[0]).strip().lstrip().replace(',','')

def url_time(url):  #查询域名注册时间
    try:
        url="http://whois.chinaz.com/%s"%(url)
        ss=url_post(url)
        if ss==0:  #读取网页内容
            #print u"获取内容失败"
            #time.sleep(2)
            return "?"
            #print ss
        p = re.compile(r"创建时间：(.*?)\" />")
        sarr = p.findall(ss)#找出一条百度
        if len(sarr) >0:  #None 也是假。
            return str(sarr[0]).strip().lstrip()
        return "!"
    except:
        return "="

def open_get_aizhan_ip(url):  #从爱站上获取这个网站大概IP
    try:
        url="http://baidurank.aizhan.com/baidu/%s/position/"%(url)
        ss=url_post(url)
        if ss==0:  #读取网页内容
            #print u"获取内容失败"
            #time.sleep(2)
            return "?"
            #print ss
        p = re.compile(r"预计来路:<span class=\"red\">(.*?)</span>")
        sarr = p.findall(ss)#找出一条百度
        if len(sarr) >0:  #None 也是假。
            return str(sarr[0]).strip().lstrip().replace(' ', '')
        return "!"
    except:
        return "="

if __name__ == "__main__":
#    url="https://cmn.ahrefs.com/site-explorer/overview/subdomains/?target=www.9945.com"
#    print ahrefs_fl(url)
    url="freebuf.com"
#    print url_time(url)
    print open_get_aizhan_ip(url)




