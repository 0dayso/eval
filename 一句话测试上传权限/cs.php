<?php

function file_add($file_name,$file_data)  
{
$fp=fopen($file_name,"w");
fputs($fp,$file_data);
fputs($fp,"\r\n");
fclose($fp);
echo "long";
}

define('BASE_PATH',str_replace('\\','/',realpath(dirname(__FILE__).'/'))."/");

file_add(BASE_PATH."web.txt","long");
?>
