#!/usr/local/bin/python
#-*- coding: UTF-8 -*-

import time
import random
def sitemap_xml(data):
    name=time.strftime("%Y-%m-%d",time.localtime(time.time()))
    x=["always","hourly","daily","weekly","monthly","yearly","never"]
    url=""
    for i in data:
        data="<url>\r\n"
        i=i.split("|")
        if len(i)<=1:
            continue  #跳过   这一次
        data+="  <loc>%s</loc>\r\n"%(i[0])
        data+="  <lastmod>%s</lastmod>\r\n"%(name)
        random.shuffle(x)
        data+="  <changefreq>%s</changefreq>\r\n"%(str(x[0]))
        data+="  <priority>0.%s</priority>\r\n"%(str(random.randint(4,9)))
        data+="</url>\r\n"
        url+=data

    data2="""<?xml version="1.0" encoding="UTF-8"?>
<urlset
   xmlns="http://www.google.com/schemas/sitemap/0.9"
   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    $data
</urlset>
    """
    url=data2.replace('$data',url)
    #print url
    return url
if __name__=='__main__':
    data=["http://www.123.com|312312","http://hao.com|123123123"]
    sitemap_xml(data)
        #windows下为：d:\data\query_text\EL_00154


