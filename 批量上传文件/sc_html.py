#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#BY: QQ292925842
#生成HTML
import threading
import sys
import g
import random
import time
import re
import ConfigParser
import base64
sys.path.append('..')
reload(sys)
sys.setdefaultencoding("utf-8")


class sc_html(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.content_lis=[]  #文章节段
        self.key_lis=[]  #关键字
        self.video_lis=[]  #视频地址
        self.index_int=1000  #生成文件篇数
        self.contentTpl_html=""  #内页模板
        self.listTpl_html=""  #主页模板
        self.ul_li_list=30 #主页每页多少条数据
        self.tmkeyword2=""  #整个网站模板随机抽取1个关键字
        self.name_id=1  #文件名规则
        self.ylinks_list=[]  #友情链接
        self.mb_path="data/mb/zhidao/"  #模板路径
        self.open_txt()   #读取
        self.open_mai_ini()   #读取配置信息

    def open_mai_ini(self):   #读取配置信息
        # 读取INI配置信息
        try:
            config = ConfigParser.ConfigParser()
            config.readfp(open("main.ini"))
            self.index_int = int(config.get("PLSH", "index_int"))  #生成文件篇数
            self.ul_li_list = int(config.get("PLSH", "ul_li_list"))  #主页每页多少条数据
            mb_path2 = str(config.get("PLSH", "mb_path"))  #模板路径
            ss = mb_path2.split("|")
            random.shuffle(ss)   #打算数组原有排序方式
            self.mb_path=ss[0]
            print u"当前模板 %s"%(str(self.mb_path))
            self.name_id = int(config.get("PLSH", "name_id"))  #文件名规则
            if self.name_id==0:
                self.name_id = random.randint(1,3)
        except Exception, e:
            print e
            pass

    def open_txt(self):   #读取
        try:
            try:
                tmkeyword2_lis=[]
                xxx = file("data/tmkeyword2.txt", 'r')  #整个网站模板随机抽取1个关键字
                for xxx_line in xxx.readlines():
                    tmkeyword2_lis.append(xxx_line.strip().lstrip())  #添加数据+"\r\n"
                random.shuffle(tmkeyword2_lis)   #打算数组原有排序方式
                self.tmkeyword2=tmkeyword2_lis[0]
                print u"当前网站 主关键字%s"%(self.tmkeyword2)
            except Exception, e:
                print u"读取文件 data/tmkeyword2.txt 异常"
                pass

            try:
                file_object = open("data/content.txt")  #内容
                try:
                    self.htm_html_text = file_object.read()
                    self.htm_html_text=g.open_file_null(self.htm_html_text).replace('。','.')  #清除空行
                    self.content_lis = self.htm_html_text.split(".")
                    random.shuffle(self.content_lis)   #打算数组原有排序方式
                finally:
                    file_object.close()
            except Exception, e:
                print u"读取文件 data/content.txt 异常"
                pass

            try:
                file_object = open("%slistTpl.html"%self.mb_path)  #主页
                try:
                    self.listTpl_html = file_object.read()
                finally:
                    file_object.close()
            except Exception, e:
                print u"读取文件 listTpl.html 异常"
                pass

            try:
                file_object = open("%scontentTpl.html"%self.mb_path)  #内页
                try:
                    self.contentTpl_html = file_object.read()
                finally:
                    file_object.close()
            except Exception, e:
                print u"读取文件 contentTpl.html 异常"
                pass

            try:
                xxx = file("data/key.txt", 'r')  #关键字
                for xxx_line in xxx.readlines():
                    self.key_lis.append(xxx_line.strip().lstrip())  #添加数据+"\r\n"
                random.shuffle(self.key_lis)   #打算数组原有排序方式
            except Exception, e:
                print u"读取文件 data/key.txt 异常"
                pass

            try:
                xxx = file("data/links.txt", 'r')  #友情链接
                for xxx_line in xxx.readlines():
                    self.ylinks_list.append(xxx_line.strip().lstrip())  #添加数据+"\r\n"
                random.shuffle(self.ylinks_list)   #打算数组原有排序方式
            except Exception, e:
                print u"读取文件 data/links.txt 异常"
                pass

            try:
                xxx = file("data/video.txt", 'r')  #视频地址
                for xxx_line in xxx.readlines():
                    self.video_lis.append(xxx_line.strip().lstrip())  #添加数据+"\r\n"
                random.shuffle(self.video_lis)   #打算数组原有排序方式
            except Exception, e:
                print u"读取文件 data/video.txt 异常"
                pass

        except Exception, e:
            pass

    def sj_lis(self,lis_data):  #获取随机内容
        try:
            return lis_data[random.randint(1,len(lis_data))]
        except Exception, e:
            return "pass"
        #return random.randint(zd0, zd1)

    def name_key(self,html):
        list=[]
        if self.name_id==1:
            name=time.strftime("%Y%m%d",time.localtime(time.time()))
            for i in range(self.index_int):
                name_index=int(name)+i
                name1="%s/index.%s|%s"%(str(name_index),html,str(self.sj_lis(self.key_lis)))
                list.append(name1)
        if self.name_id==2:
            for i in range(self.index_int):
                name_index=self.sj_HZ(random.randint(3,7))   #汉字拼音
                name1="%s/index.%s|%s"%(str(name_index),html,str(self.sj_lis(self.key_lis)))
                list.append(name1)
        if self.name_id==3:
            for i in range(self.index_int):
                name_index=self.sj_SZ(random.randint(3,7))   #数字3-7位拼音
                name1="%s/index.%s|%s"%(str(name_index),html,str(self.sj_lis(self.key_lis)))
                list.append(name1)
        return list

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

    def cx_re_sl(self,data,re_data):  #查询数量
        try:
            p = re.compile( r'%s'%(re_data))
            sarr = p.findall(data)
            return len(sarr)
        except Exception, e:
            #print e
            return 0

    def hq_ip(self):
        try:
            ip_data="%s.%s.%s.%s"%(random.randint(10,254),random.randint(10,254),random.randint(10,254),random.randint(10,254))
            return ip_data
        except Exception,e:
            return "120.0.0.1"

    def sj_SZ(self,x):   #汉字拼音
        try:
            data=""
            for i in range(x):
                data+=random.choice('1234567890')
            return data
        except Exception,e:
            return "876"

    def sj_HZ(self,x):   #汉字拼音
        try:
            data=""
            for i in range(x):
                data+=random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
            return data
        except Exception,e:
            return "XXX"

    def ny_html(self,html_data,title,url_path,name_html_list):  #模板内容 标题  url_path繁殖目录  内链地址
        if not self.cx_re_sl(html_data,'{tmkeyword2}')==0:
            html_data = html_data.replace('{tmkeyword2}',self.tmkeyword2)  #{tmkeyword2} 整个网站模板随机抽取1个关键字
        if not self.cx_re_sl(html_data,'{time}')==0:
            time_data = time.strftime("%Y-%m-%d",time.localtime(time.time()))
            html_data = html_data.replace('{time}',time_data)
        if not self.cx_re_sl(html_data,'{domain}')==0:
            html_data = html_data.replace('{domain}',url_path)  #SHELL目录地址(繁殖地址)
        if not self.cx_re_sl(html_data,'{tmkeyword}')==0:
            html_data = html_data.replace('{tmkeyword}',title)  #主关键词标签
        if not self.cx_re_sl(html_data,'{keyword2}')==0:
            keyword2 = str(self.sj_lis(self.key_lis))
            html_data = html_data.replace('{keyword2}',keyword2)  #固定关键词标签
        if not self.cx_re_sl(html_data,'{keyword3}')==0:
            keyword3 = str(self.sj_lis(self.key_lis))
            html_data = html_data.replace('{keyword3}',keyword3)  #固定关键词标签

        #{ip}  随机变异IP地址转换
        ip_int = self.cx_re_sl(html_data,'{ip}')  #查询数量
        if not ip_int==0:
            for i in range(ip_int):
                html_data = html_data.replace('{ip}',self.hq_ip())  #固定关键词标签

        #{pinyin}随机1~3个汉字拼音标签
        pinyin_int = self.cx_re_sl(html_data,'{pinyin}')  #查询数量
        if not pinyin_int==0:
            for i in range(pinyin_int):
                html_data = html_data.replace('{pinyin}',self.sj_HZ(random.randint(1,3)))  #固定关键词标签

        #{skeyword}  随机关键词标签
        skeyword_int = self.cx_re_sl(html_data,'{skeyword}')  #查询数量
        if not skeyword_int==0:
            for i in range(skeyword_int):
                th=str(self.sj_lis(self.key_lis))  #关键字
                html_data = html_data.replace('{skeyword}',th,1)
#                bool_no_ok,data=self.re_th_data(html_data,'{skeyword}',th) #替换内容   数据  标记  替换
#                if not bool_no_ok:  #正则失败
#                    continue  #跳过   这一次
#                html_data = data
        #{content}  随机句子标签
        content_int = self.cx_re_sl(html_data,'{content}')  #查询数量
        if not content_int==0:
            for i in range(content_int):
                th=str(self.sj_lis(self.content_lis)+"。")  #文章
                html_data = html_data.replace('{content}',th,1)
        #{number}  随机1~3个数字标签
        number_int = self.cx_re_sl(html_data,'{number}')  #查询数量
        if not number_int==0:
            for i in range(number_int):
                th = random.randint(9,999)
                html_data = html_data.replace('{number}',str(th),1)

        #{link}  随机链接标签(内链)
        link_int = self.cx_re_sl(html_data,'{link}')  #查询数量
        if not link_int==0:
            for i in range(link_int):
                th=str(self.sj_lis(name_html_list))
                #20150497/index.html|宁波交友QQ群
                ss = th.split("|")
                if not len(ss)==2:
                    html_data = html_data.replace('{link}',url_path,1)
                else:
                    html_data = html_data.replace('{link}',str(url_path+ss[0]),1)
        #{slink}  随机对应关键词超链标签(内链)
        slink_int = self.cx_re_sl(html_data,'{slink}')  #查询数量
        if not slink_int==0:
            for i in range(slink_int):
                th=str(self.sj_lis(name_html_list))
                #20150497/index.html|宁波交友QQ群
                ss = th.split("|")
                if not len(ss)==2:
                    #continue  #跳过   这一次
                    th=str(self.sj_lis(self.key_lis))  #关键字
                    data='<a href="http://www.36obuy.org/avcpa/1.php">%s</a>'%(th)
                    html_data = html_data.replace('{slink}',data,1)
                else:
                    data='<a href="%s">%s</a>'%(url_path+ss[0],ss[1])
                    html_data = html_data.replace('{slink}',data,1)
        #{video}  随机视频链接标签
        video_int = self.cx_re_sl(html_data,'{video}')  #查询数量
        if not video_int==0:
            for i in range(video_int):
                th=str(self.sj_lis(self.video_lis))  #
                html_data = html_data.replace('{video}',th,1)

        #################################
        #{newslist}  目录页目录链接
        newslist_int = self.cx_re_sl(html_data,'{newslist}')  #查询数量
        if not newslist_int==0:
            time_data = time.strftime("%Y-%m-%d",time.localtime(time.time()))
            for i in range(newslist_int):
                url_data=""
                for i in range(self.ul_li_list):
                    th=str(self.sj_lis(name_html_list))
                    #20150497/index.html|宁波交友QQ群
                    ss = th.split("|")
                    if not len(ss)==2:
                        #continue  #跳过   这一次
                        url_data+='<li><a href="%s">%s</a> <small>日期：</small>%s</li>\r\n'%(url_path,"狠狠撸",time_data)
                    else:
                        url_data+='<li><a href="%s">%s</a> <small>日期：</small>%s</li>\r\n'%(url_path+ss[0],ss[1],time_data)
                url_data="<ul>\r\n%s<ul>\r\n"%(url_data)
                html_data = html_data.replace('{newslist}',url_data,1)

        #{page}  目录页页数链接
        page_int = self.cx_re_sl(html_data,'{page}')  #查询数量
        if not page_int==0:
            url_data=""
            for i in range(len(name_html_list)/self.ul_li_list):
                i+=1
                if i==1:
                    url_data+='<a href="%sindex.html">[%s]</a>\r\n'%(url_path,int(i))
                else:
                    url_data+='<a href="%s">[%s]</a>\r\n'%(url_path+"index"+str(i)+".html",int(i))
            #print url_data
            html_data = html_data.replace('{page}',url_data,1)
        #print len(name_html_list)/self.ul_li_list

        #{title}  关键词+随机句子组合标签
        title_int = self.cx_re_sl(html_data,'{title}')  #查询数量
        if not title_int==0:
            for i in range(title_int):
                th=str(self.sj_lis(self.content_lis))  #文章
                th2=str(self.sj_lis(self.key_lis))  #关键字
                html_data = html_data.replace('{title}',th+"  "+th2,1)

        #{ylinks}  友链标签，调用外部链接
        ylinks_int = self.cx_re_sl(html_data,'{ylinks}')  #查询数量
        if not ylinks_int==0:
            for i in range(ylinks_int):
                th=str(self.sj_lis(self.ylinks_list))
                ss = th.split("|")
                if not len(ss)==2:
                    #continue  #跳过   这一次
                    url_data='<a href="%s">%s</a>'%(url_path,"小姐")
                else:
                    url_data='<a href="%s">%s</a>'%(ss[0],ss[1])
                html_data = html_data.replace('{ylinks}',url_data,1)

        return html_data
        #self.TXT_file_add("index.html",html_data)

    def TXT_file_add(self,file_nem,data):  #写入文本
        try:
            #file_nem=time.strftime('%Y.%m.%d')   #file_nem+".txt"
            file_object = open(file_nem,'w')
            #file_object.write(list_passwed[E])
            file_object.writelines(data)
            file_object.writelines("\n")
            file_object.close()
        except Exception,e:
            print u"写入TXT失败",file_nem,data,e
            return 0

    def sc_html(self,name_html,url_path):  #生成内容

        #生成文件地址和标题
        #url_path="http://127.0.0.1/path/"
        name_html_list=self.name_key(name_html)
        #20150497/index.html|宁波交友QQ群
        html_data = self.listTpl_html  #主页模板
        html_data2 = self.contentTpl_html  #内页模板
#        self.ny_html(html_data,"潞西市富婆",url_path,name_html_list)  #模板 标题  url_path繁殖目录  内链地址
        url_data=[]  #保存文件路径   内容
        for i in range(len(name_html_list)/self.ul_li_list):   #生成主页
            url_data2=[]
            gjz=str(self.sj_lis(self.key_lis))  #关键字
            th=self.ny_html(html_data,str(gjz),url_path,name_html_list)  #模板 标题  url_path繁殖目录  内链地址
            if i==1:
                url_data2.append("index.html")
                url_data2.append(base64.b64encode(th))
                url_data.append(url_data2)   #主页
            else:
                url_data2.append("%s"%"index"+str(i)+".html")
                url_data2.append(base64.b64encode(th))
                url_data.append(url_data2)   #主页

        for i in range(len(name_html_list)):   #生成主页
            ss = name_html_list[i]
            ss = ss.split("|")
            url_data2=[]
            gjz=str(self.sj_lis(self.key_lis))  #关键字
            th=self.ny_html(html_data2,str(gjz),url_path,name_html_list)  #模板 标题  url_path繁殖目录  内链地址
            if not len(ss)==2:
                continue  #跳过   这一次
            else:
                url_data2.append(ss[0])
                url_data2.append(base64.b64encode(th))
                url_data.append(url_data2)   #主页

#        for i in range(len(url_data)):
#            print url_data[i]

        return self.mb_path,url_data

    def file_path(self):  #写入文件
        mb,url_data = self.sc_html("html","http://127.0.0.1/path/")
        for i in range(len(url_data)):
            html_data=url_data[i]

            path="cs/%s"%(html_data[0])
            nPos1 = path.rindex("/")
            path2=path[0:nPos1]
            if not os.path.isdir(path2):
                os.makedirs(path2)
            #    os.path.isfile可以判断文件
            #    os.path.isdir可以判断目录
            #    os.path.exists不区分文件还是目录
            self.TXT_file_add(path,base64.b64decode(html_data[1]))

import os
import urllib


if __name__=='__main__':
    sc = sc_html()
    #sc.file_path()
    print sc.name_key("html")















