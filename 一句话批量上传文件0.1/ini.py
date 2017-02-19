#!/usr/local/bin/python
#-*- coding: UTF-8 -*-

A1=""  #延时/超时
A2=""   #上传文件名
A3=""  #设置URL路径
INITXT="Server.ini"  #INI文件名字

import ConfigParser
def ini_get():  #读取INI
    try:
        global INITXT,A1,A2,A3
        config = ConfigParser.ConfigParser()
        config.readfp(open(INITXT))
        A1 = config.get("DATA","A1")
        A2 = config.get("DATA","A2")
        A3 = config.get("DATA","A3")
    except:
        print "读取INI错误"
        ini_add("200","123.php","123.php?del=123456")  #写入INI

def ini_add(a,b,c):  #写入INI
    try:
        global INITXT
        config = ConfigParser.ConfigParser()
        config.add_section("DATA")# 设置section段及对应的值
        config.set("DATA","A1",a)
        config.set("DATA","A2",b)
        config.set("DATA","A3",c)
        config.write(open(INITXT, "w"))# 写入文件
    except:
        print "写入INI错误"

def ini_write(a,b,c):  #修改INI
    try:
        global INITXT
        config = ConfigParser.ConfigParser()
        config.read(INITXT)
        if not config.has_section("DATA"):#看是否存在该Section，不存在则创建
            temp = config.add_section("")
        config.set("DATA","A1",a)
        config.set("DATA","A2",b)
        config.set("DATA","A3",c)
        config.write(open(INITXT, "r+"))
    except:
        print "修改INI错误"
        ini_add("200","123.php","123.php?del=123456")  #写入INI







