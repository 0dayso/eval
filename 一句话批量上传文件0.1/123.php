<?php
$fp=fopen("qq.txt","a"); 
$logMsg = "You are located at \r\n";
fputs($fp,$logMsg); 
fclose($fp); 
echo "-------qq.txt �Ѿ�����<br/>"; 

?>