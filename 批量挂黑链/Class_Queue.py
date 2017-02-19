#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#神龙 QQ29295842
#blog http://hi.baidu.com/alalmn
#线程操作消息队列
import threading
import Queue
import time
import urllib2

webscan_url = Queue.Queue(0) #要采集的URL    #当有多个线程共享一个东西的时候就可以用它了
exp_url = Queue.Queue() #存在EXP漏洞的  ["网址","漏洞类型","漏洞详细信息","漏洞地址","密码","备注"]
exp_url_int = Queue.Queue(0)    #多线程下变量共享  不知道怎么回事
class C_Queue(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.exp_url_int=0
    def print_Queue(self):
        try:
            print "-----------------------------------------"
            print "WEBSEHLL--------%s"%(webscan_url.qsize())
            print "-----------------------------------------"
        except Exception,e:
            #print e
            return 0

    def run(self):
        while True:
            try:
                self.print_Queue()
                #self.add_txt_exp_url()  #对exp_url进行存储
                time.sleep(10)
            except Exception,e:
                pass

################################################
if __name__=='__main__':
    threads = []  #线程
    for i in range(1):  #nthreads=10  创建10个线程
        threads.append(C_Queue())
    for t in threads:   #不理解这是什么意思    是结束线程吗
        t.start()  #start就是开始线程