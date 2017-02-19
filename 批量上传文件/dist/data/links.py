#!/usr/local/bin/python
#-*- coding: UTF-8 -*-

def TXT_file_add(file_nem,data):  #写入文本
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

import random
if __name__=='__main__':
    name="links.txt"
    name2="links_10.txt"
    url_data=[]  #保存繁殖的数组
    xxx = file(name, 'r')  #关键字
    for xxx_line in xxx.readlines():
        data=xxx_line.strip().lstrip()  #添加数据+"\r\n"
        ss = data.split("|")
        url_data.append(ss[0])

    random.shuffle(url_data)   #打算数组原有排序方式

    for xxx_line in url_data:
        TXT_file_add(name2,xxx_line)  #写入文本