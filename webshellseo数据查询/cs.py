

if __name__ == "__main__":
    data="http://www.0201.com.cn/plus/long.php"
    line = data.split("|")
    if len(line)>=2:
        print line[0]
        print line[1]
    else:
        print data


#    if line[0]==None:
#        line.append(data)
#
#    if line[1]==None:
#        line.append("")
#    print line[0]
#    print line[1]

