#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#公用函数



def bool_asp_php(s0): #查看一句话是语句的一句话
    if (".asp" in str(s0) or ".ASP" in str(s0) or ".Asp" in str(s0)):
        return "asp"
    if (".php" in str(s0) or ".PHP" in str(s0) or ".Php" in str(s0)):
        return "php"


if __name__ == "__main__":
    print bool_asp_php("http://www.dsolab.com/celive/uploadfiles/CELIVE-5GLFuOKKQF.php;.jpg")