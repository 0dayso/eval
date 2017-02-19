#!/usr/local/bin/python
#-*- coding: UTF-8 -*-

import re,httplib
import gzip,StringIO
import socket
import urllib
import time
socket.setdefaulttimeout(10)

import sys
reload(sys)
sys.setdefaultencoding('utf-8')



if __name__ == "__main__":
    xxx = file("cs.php", 'r')
    file_data=xxx.read()
    print file_data