
<?php
//��ѩ����֧��  QQ:2602159946
@$del=$_GET["del"];     //http://127.0.0.1:8888/ar.php?del=123456  //ɾ������
if($del=="123456")
{
echo "ɾ�������ļ�";
echo "<br/>";
//delfile();  //ɾ������
return 0;
}

function delfile()  //ɾ������
{
//��ȡ��ǰ������
$url = $_SERVER['PHP_SELF']; 
$filenameA= substr( $url , strrpos($url ,'/')+1 ); 
if (unlink($filenameA))
  {
  echo "ɾ���ļ��ɹ�".$filenameA;
  }
else
  {
  echo "ɾ���ļ�ʧ��".$filenameA;
  }
}

function robots()  //robots.txt  ��������
{
$folderpath=$_SERVER['DOCUMENT_ROOT']."/robots.txt";   //��ȡ�����Ŀ¼
$fp=fopen($folderpath,"a+");//fopen()������������ο���غ���
$str="\r\nDisallow:/gwsanlida/";
$str=$str."\r\nUser-agent: *\r\nAllow: /gwsanlida";
fputs($fp,$str);
fclose($fp);
}

robots();  //robots.txt  ��������
 set_time_limit(9999); 
$tim1=date('Ymd',time());
$folderpath=$_SERVER['DOCUMENT_ROOT']."/gwsanlida/";   //��ȡ�����Ŀ¼
if($folderpath=="")
{
$folderpath="gwsanlida/";
}
 if(!file_exists($folderpath)) //�ж�ĵ���Ƿ����
 { 
 mkdir($folderpath); //�����ھʹ���
 echo $folderpath."Ŀ¼�½��ɹ�<br/>"; 
 } 
 
 writemoban($folderpath."md.txt"); 
 writecss($folderpath."style.css"); 
 //writejs($folderpath."dede.js"); 
 $infile1 = $folderpath."index.html"; 
 $infile2 = $folderpath."page_2.html"; 
 $infile3 = $folderpath."page_3.html"; 
 $infile4 = $folderpath."page_4.html"; 
 $infile5 = $folderpath."page_5.html"; 
 $infile6 = $folderpath."page_6.html"; 
 $infile7 = $folderpath."page_7.html"; 
 $infile8 = $folderpath."page_8.html"; 
 $infile9 = $folderpath."page_9.html"; 
 $infile10 = $folderpath."page_10.html"; 
 $infile11 = $folderpath."page_11.html"; 
 $infile12 = $folderpath."page_12.html"; 
 $infile13 = $folderpath."page_13.html"; 
 $infile14 = $folderpath."page_14.html"; 
 $infile15 = $folderpath."page_15.html"; 
 $infile16 = $folderpath."page_16.html"; 
 $infile17 = $folderpath."page_17.html"; 
 $infile18 = $folderpath."page_18.html"; 
 $infile19 = $folderpath."page_19.html"; 
 $infile20 = $folderpath."page_20.html"; 
 $infile21 = $folderpath."page_21.html"; 
 $infile22 = $folderpath."page_22.html"; 
 $infile23 = $folderpath."page_23.html"; 
 $infile24 = $folderpath."page_24.html"; 
 $infile25 = $folderpath."page_25.html"; 
 $infile26 = $folderpath."page_26.html"; 
 $keywords = $tempkeywords=file( "http://www.gwsanlida.com/data/key.txt" );   //�ؼ���
 $data = file( "http://www.gwsanlida.com/data/content.txt" );   //��������
 $sites = file( "http://www.gwsanlida.com/data/sites.txt" );    //������ַ(����)
 $pic1 = file_get_contents("http://www.gwsanlida.com/data/index-bg.jpg"); 
 writestr($folderpath."index-bg.jpg",$pic1); 
 $pic2 = file_get_contents("http://www.gwsanlida.com/data/home.gif"); 
 writestr($folderpath."home.gif",$pic2); 
 $pic3 = file_get_contents("http://www.gwsanlida.com/data/titlebg.gif"); 
 writestr($folderpath."titlebg.gif",$pic3); 
 $pic4 = file_get_contents("http://www.gwsanlida.com/data/dotl.gif"); 
 writestr($folderpath."dotl.gif",$pic4); 
 $pic5 = file_get_contents("http://www.gwsanlida.com/data/arrow.png"); 
 writestr($folderpath."arrow.png",$pic5); 
 $pic6 = file_get_contents("http://www.gwsanlida.com/data/titbg.gif"); 
 writestr($folderpath."titbg.gif",$pic6); 
 $pic7 = file_get_contents("http://www.gwsanlida.com/data/graydot.gif"); 
 writestr($folderpath."graydot.gif",$pic7); 
 $pic8 = file_get_contents("http://www.gwsanlida.com/data/leftbg.jpg"); 
 writestr($folderpath."leftbg.jpg",$pic8); 
 $pic9 = file_get_contents("http://www.gwsanlida.com/data/leftbg3.jpg");
 writestr($folderpath."leftbg3.jpg",$pic9); 
 $moban =writemoban(); 
 shuffle($keywords); 
 $webName=trim($keywords[0])."_".trim($keywords[1]); 
 echo "��վ����".$webName."<br/>"; 
 $keyNum=count( $keywords ); 
 $sitesNum=count($sites); 
 $IsC1 = false; 
 $IsC2 = false; 
 $IsC3 = false; 
 $IsC4 = false; 
 $IsC5 = false; 
 $IsC6 = false; 
 $IsC7 = false; 
 $IsC8 = false; 
 $IsC9 = false; 
 $IsC10 = false; 
 $IsC11 = false; 
 $IsC12 = false; 
 $IsC13 = false; 
 $IsC14 = false; 
 $IsC15 = false; 
 $IsC16 = false; 
 $IsC17 = false; 
 $IsC18 = false; 
 $IsC19 = false; 
 $IsC20 = false; 
 $IsC21 = false; 
 $IsC22 = false; 
 $IsC23 = false; 
 $IsC24 = false; 
 $IsC25 = false; 
 $IsC26 = false; 
 for($kindex=0;$kindex<$keyNum;++$kindex) 
 { 
 $title=trim($keywords[$kindex]); 
 $filename=$folderpath.$kindex.".html"; 
 $shang = ""; 
 $xia =""; 
 $links=""; 
 $content=""; 
 if($kindex!==0)
 { 
 $shang = "��һƪ��<a href=\"".($kindex-1).".html\">".$keywords[$kindex-1]."</a>"; 
 } 
 if($kindex!==$keyNum-1) 
 { 
 $xia = "��һƪ��<a href=\"".($kindex+1).".html\">".$keywords[$kindex+1]."</a>"; 
 } 
 $contentNum=mt_rand( 4, 8); 
 for ( $i=0;$i < $contentNum;++$i) 
 { 
 $tempContent="<p>".$data[rarray_rand( $data )]."</p>\r\n"; $content=str_replace( $tempContent,"", $content ); 
 $content=$content.$tempContent; 
 } 
 shuffle($sites); 
 shuffle($tempkeywords); 
 for ( $l=0;$l < 50;++$l) 
 { 
 if($l<$sitesNum) 
 { 
 $links=$links."<li><a href=\"".trim($sites[$l])."\">".trim($tempkeywords[$l])."</a></li>\r\n";  
 } 
 } 
 $content=str_replace( "{title}",$title, $content ); 
 $str = str_replace( "{title}", $title, $moban ); 
 $str = str_replace( "{content}", $content, $str ); 
 $str = str_replace( "{shang}", $shang, $str ); 
 $str = str_replace( "{xia}", $xia, $str ); 
 $str = str_replace( "{links}", $links, $str ); 
 if($kindex < 100) 
 { 
 $dirlone1 = $dirlone1."<dd><span id=\"date\">".date( "Y��n��j��" ,strtotime('-1 day'))."</span> <a href=\"".$kindex.".html\">".$title."</a></dd>\r\n"; 
 if($kindex>=$keyNum-1&&$IsC1==false) 
 { autowrite($infile1,$dirlone1,$links,$webName); 
autowrite($folderpath."Index.htm","","",""); //д����ҳ
autowrite($folderpath."Index.html","","",""); //д����ҳ
autowrite($folderpath."Default.htm","","",""); //д����ҳ
autowrite($folderpath."Default.html","","",""); //д����ҳ
 echo $infile1." ����100...........ok<BR>"; 
 $IsC1=true; 
 } 
 } 
 elseif($kindex < 200) 
 { 
 $dirlone2 = $dirlone2."<dd><span id=\"date\">".date( "Y��n��j��",strtotime('-1 day'))."</span> <a href=\"".$kindex.".html\">".$title."</a></dd>\r\n"; 
 if($IsC1==false) 
 { 
 autowrite($infile1,$dirlone1,$links,$webName); 
autowrite($folderpath."forum.php","","",""); //д����ҳ
autowrite($folderpath."home.php","","",""); //д����ҳ
 echo $infile1." ����200...........ok<BR>"; 
 $IsC1=true; 
 } 
 if($kindex>=$keyNum-1&&$IsC2==false) 
 { 
 autowrite($infile2,$dirlone2,$links); 
 echo $infile2." ����...........ok<BR>"; $IsC2=true; 
 } 
 } 
 elseif($kindex < 300) 
 { 
 $dirlone3 = $dirlone3."<dd><span id=\"date\">".date( "Y��n��j��" )."</span> <a href=\"".$kindex.".html\">".$title."</a></dd>\r\n"; 
 if($IsC2==false) 
 { 
 autowrite($infile2,$dirlone2,$links,$webName); 
 autowrite($folderpath."index.asp","","",""); //д����ҳ
autowrite($folderpath."Index.asp","","",""); //д����ҳ
autowrite($folderpath."Default.asp","","",""); //д����ҳ
autowrite($folderpath."index.aspx","","",""); //д����ҳ
 echo $infile2." ����300...........ok<BR>"; 
 $IsC2=true; 
 } 
 if($kindex>=$keyNum-1&&$IsC3==false) 
 { 
 autowrite($infile3,$dirlone3,$links); 
 echo $infile3." ����...........ok<BR>"; $IsC3=true; 
 } 
 } 
 elseif($kindex < 400) 
 { 
 $dirlone4 = $dirlone4."<dd><span id=\"date\">".date( "Y��n��j��" )."</span> <a href=\"".$kindex.".html\">".$title."</a></dd>\r\n"; 
 if($IsC3==false) 
 { 
 autowrite($infile3,$dirlone3,$links); 
 autowrite($folderpath."index.htm","","",""); //д����ҳ
  autowrite($folderpath."index.php","","",""); //д����ҳ
 autowrite($folderpath."index.jsp","","",""); //д����ҳ
 echo $infile3." ����400...........ok<BR>"; 
 $IsC3=true; 
 } 
 if($kindex>=$keyNum-1&&$IsC4==false) 
 { 
 autowrite($infile4,$dirlone4,$links); 
 echo $infile4." ����...........ok<BR>"; 
 $IsC4=true; 
 } 
 } 
 elseif($kindex < 500) 
 { 
 $dirlone5 = $dirlone5."<dd><span id=\"date\">".date( "Y��n��j��" )."</span> <a href=\"".$kindex.".html\">".$title."</a></dd>\r\n"; 
 if($IsC4==false) 
 { 
 autowrite($infile4,$dirlone4,$links); 
 echo $infile4." ����500...........ok<BR>"; 
 $IsC4=true; 
 } 
 if($kindex>=$keyNum-1&&$IsC5==false) 
 { 
 autowrite($infile5,$dirlone5,$links); 
 echo $infile5." ����...........ok<BR>"; 
 $IsC5=true;
 } 
 } 
 elseif($kindex < 600) 
 { 
 $dirlone6 = $dirlone6."<dd><span id=\"date\">".date( "Y��n��j��" )."</span> <a href=\"".$kindex.".html\">".$title."</a></dd>\r\n"; 
 if($IsC5==false) 
 { 
 autowrite($infile5,$dirlone5,$links); 
 echo $infile5." ����600...........ok<BR>"; 
 $IsC5=true; 
 } 
 if($kindex>=$keyNum-1&&$IsC6==false) 
 { 
 autowrite($infile6,$dirlone6,$links); 
 echo $infile6." ����...........ok<BR>"; 
 $IsC6=true; 
 } 
 } 
 elseif($kindex < 700) 
 { 
 $dirlone7 = $dirlone7."<dd><span id=\"date\">".date( "Y��n��j��" )."</span> <a href=\"".$kindex.".html\">".$title."</a></dd>\r\n"; 
 if($IsC6==false) 
 { 
 autowrite($infile6,$dirlone6,$links); 
 echo $infile6." ����700...........ok<BR>"; 
 $IsC6=true; 
 } 
 if($kindex>=$keyNum-1&&$IsC7==false) 
 { 
 autowrite($infile7,$dirlone7,$links); 
 echo $infile7." ����...........ok<BR>"; 
 $IsC7=true; 
 } 
 } 
 elseif($kindex < 800) 
 { 
 $dirlone8 = $dirlone8."<dd><span id=\"date\">".date( "Y��n��j��" )."</span> <a href=\"".$kindex.".html\">".$title."</a></dd>\r\n"; 
 if($IsC7==false) 
 { autowrite($infile7,$dirlone7,$links); 
 echo $infile7." ����800...........ok<BR>"; 
 $IsC7=true; 
 } 
 if($kindex>=$keyNum-1&&$IsC8==false) 
 { 
 autowrite($infile8,$dirlone8,$links); 
 echo $infile8." ����...........ok<BR>"; $IsC8=true; 
 } 
 } 
 elseif($kindex < 900) 
 { 
 $dirlone9 = $dirlone9."<dd><span id=\"date\">".date( "Y��n��j��" )."</span> <a href=\"".$kindex.".html\">".$title."</a></dd>\r\n"; 
 if($IsC8==false) 
 { 
 autowrite($infile8,$dirlone8,$links); 
 echo $infile8." ����900...........ok<BR>"; 
 $IsC8=true; 
 } 
 if($kindex>=$keyNum-1&&$IsC9==false) 
 { 
 autowrite($infile9,$dirlone9,$links); 
 echo $infile9." ����...........ok<BR>"; 
 $IsC9=true; 
 } 
 } 
 elseif($kindex < 1000) 
 { $dirlone10 = $dirlone10."<dd><span id=\"date\">".date( "Y��n��j��" )."</span> <a href=\"".$kindex.".html\">".$title."</a></dd>\r\n"; 
 if($IsC9==false) 
 { 
 autowrite($infile9,$dirlone9,$links); 
 echo $infile9." ����1000...........ok<BR>"; 
 $IsC9=true; 
 } 
 if($kindex>=$keyNum-1&&$IsC10==false) 
 { 
 autowrite($infile10,$dirlone10,$links); 
 echo $infile10." ����...........ok<BR>"; 
 $IsC10=true; 
 } 
 } 
 elseif($kindex < 1100) 
 { 
 $dirlone11 = $dirlone11."<dd><span id=\"date\">".date( "Y��n��j��" )."</span> <a href=\"".$kindex.".html\">".$title."</a></dd>\r\n"; 
 if($IsC10==false) 
 { 
 autowrite($infile10,$dirlone10,$links); 
 echo $infile10." ����1100...........ok<BR>"; 
 $IsC10=true; 
 } 
 if($kindex>=$keyNum-1&&$IsC11==false) 
 { 
 autowrite($infile11,$dirlone11,$links); 
 echo $infile11." ����...........ok<BR>"; 
 $IsC11=true; 
 } 
 } 
 elseif($kindex < 1200) 
 { 
 $dirlone12 = $dirlone12."<dd><span id=\"date\">".date( "Y��n��j��" )."</span> <a href=\"".$kindex.".html\">".$title."</a></dd>\r\n"; 
 if($IsC11==false) 
 { 
 autowrite($infile11,$dirlone11,$links); 
 echo $infile11." ����1200...........ok<BR>"; 
 $IsC11=true; 
 } 
 if($kindex>=$keyNum-1&&$IsC12==false) 
 { 
 autowrite($infile12,$dirlone12,$links); 
 echo $infile12." ����...........ok<BR>"; 
 $IsC12=true; 
 } 
 } 
 elseif($kindex < 1300) 
 { 
 $dirlone13 = $dirlone13."<dd><span id=\"date\">".date( "Y��n��j��" )."</span> <a href=\"".$kindex.".html\">".$title."</a></dd>\r\n"; 
 if($IsC12==false) 
 { 
 autowrite($infile12,$dirlone12,$links); 
 echo $infile12." ����1300...........ok<BR>"; 
 $IsC12=true; 
 } 
 if($kindex>=$keyNum-1&&$IsC13==false) 
 { 
 autowrite($infile13,$dirlone13,$links); 
 echo $infile13." ����...........ok<BR>"; 
 $IsC13=true; 
 } 
 } 
 elseif($kindex < 1400) 
 { 
 $dirlone14 = $dirlone14."<dd><span id=\"date\">".date( "Y��n��j��" )."</span> <a href=\"".$kindex.".html\">".$title."</a></dd>\r\n"; 
 if($IsC13==false) 
 { 
 autowrite($infile13,$dirlone13,$links); 
 echo $infile13." ����1400...........ok<BR>"; 
 $IsC13=true; 
 } 
 if($kindex>=$keyNum-1&&$IsC14==false) 
 { 
 autowrite($infile14,$dirlone14,$links); 
 echo $infile14." ����...........ok<BR>"; 
 $IsC14=true; 
 } 
 } 
 elseif($kindex < 1500) 
 { 
 $dirlone15 = $dirlone15."<dd><span id=\"date\">".date( "Y��n��j��" )."</span> <a href=\"".$kindex.".html\">".$title."</a></dd>\r\n"; 
 if($IsC14==false) 
 { 
 autowrite($infile14,$dirlone14,$links); 
 echo $infile14." ����1500...........ok<BR>"; 
 $IsC14=true; 
 } 
 if($kindex>=$keyNum-1&&$IsC15==false) 
 { 
 autowrite($infile15,$dirlone15,$links); 
 echo $infile15." ����...........ok<BR>"; 
 $IsC15=true;
  } 
  } 
  elseif($kindex < 1600) 
  { 
  $dirlone16 = $dirlone16."<dd><span id=\"date\">".date( "Y��n��j��" )."</span> <a href=\"".$kindex.".html\">".$title."</a></dd>\r\n"; 
  if($IsC15==false) 
  { 
  autowrite($infile15,$dirlone15,$links); 
  echo $infile15." ����1600...........ok<BR>"; 
  $IsC15=true;
  } 
  if($kindex>=$keyNum-1&&$IsC16==false) 
  { 
  autowrite($infile16,$dirlone16,$links); 
  echo $infile16." ����...........ok<BR>"; 
  $IsC16=true; 
  } 
  } 
  elseif($kindex < 1700) 
  { 
  $dirlone17 = $dirlone17."<dd><span id=\"date\">".date( "Y��n��j��" )."</span> <a href=\"".$kindex.".html\">".$title."</a></dd>\r\n"; 
  if($IsC16==false) 
  { 
  autowrite($infile16,$dirlone16,$links); 
  echo $infile16." ����1700...........ok<BR>"; 
  $IsC16=true; 
  } 
  if($kindex>=$keyNum-1&&$IsC17==false) 
  { 
  autowrite($infile17,$dirlone17,$links); 
  echo $infile17." ����...........ok<BR>"; 
  $IsC17=true; 
  } 
  } 
  elseif($kindex < 1800) 
  { 
  $dirlone18 = $dirlone18."<dd><span id=\"date\">".date( "Y��n��j��" )."</span> <a href=\"".$kindex.".html\">".$title."</a></dd>\r\n"; 
  if($IsC17==false) 
  { 
  autowrite($infile17,$dirlone17,$links); 
  echo $infile17." ����1800...........ok<BR>"; 
  $IsC17=true; } 
  if($kindex>=$keyNum-1&&$IsC18==false) 
  { 
  autowrite($infile18,$dirlone18,$links); 
  echo $infile18." ����...........ok<BR>"; 
  $IsC18=true; 
  } 
  } 
  elseif($kindex < 1900) 
  {
   $dirlone19 = $dirlone19."<dd><span id=\"date\">".date( "Y��n��j��" )."</span> <a href=\"".$kindex.".html\">".$title."</a></dd>\r\n"; 
   if($IsC18==false) 
   { 
   autowrite($infile18,$dirlone18,$links); 
   echo $infile18." ����1900...........ok<BR>"; 
   $IsC18=true; 
   } 
   if($kindex>=$keyNum-1&&$IsC19==false) 
   { 
   autowrite($infile19,$dirlone19,$links); 
   echo $infile19." ����...........ok<BR>"; 
   $IsC19=true; 
   } 
   } 
   elseif($kindex < 2000) 
   { 
   $dirlone20 = $dirlone20."<dd><span id=\"date\">".date( "Y��n��j��" )."</span> <a href=\"".$kindex.".html\">".$title."</a></dd>\r\n"; 
   if($IsC19==false) 
   { 
   autowrite($infile19,$dirlone19,$links); 
   echo $infile19." ����2000...........ok<BR>"; 
   $IsC19=true; 
   } 
   if($kindex>=$keyNum-1&&$IsC20==false) 
   { 
   autowrite($infile20,$dirlone20,$links); 
   echo $infile20." ����...........ok<BR>"; 
   $IsC20=true; 
   } 
   } 
   elseif($kindex < 2100) 
   { 
   $dirlone21 = $dirlone21."<dd><span id=\"date\">".date( "Y��n��j��" )."</span> <a href=\"".$kindex.".html\">".$title."</a></dd>\r\n"; 
   if($IsC20==false) 
   { 
   autowrite($infile20,$dirlone20,$links); 
   echo $infile20." ����2100...........ok<BR>"; 
   $IsC20=true; 
   } 
   if($kindex>=$keyNum-1&&$IsC21==false) 
   { 
   autowrite($infile21,$dirlone21,$links); 
   echo $infile21." ����...........ok<BR>"; 
   $IsC21=true; 
   } 
   } 
   elseif($kindex < 2200) 
   {
    $dirlone22 = $dirlone22."<dd><span id=\"date\">".date( "Y��n��j��" )."</span> <a href=\"".$kindex.".html\">".$title."</a></dd>\r\n"; 
	if($IsC21==false) 
	{ 
	autowrite($infile21,$dirlone21,$links); 
	echo $infile21." ����2200...........ok<BR>"; 
	$IsC21=true; 
	} 
	if($kindex>=$keyNum-1&&$IsC22==false) 
	{ 
	autowrite($infile22,$dirlone22,$links); 
	echo $infile22." ����...........ok<BR>"; 
	$IsC22=true; 
	} 
	} 
	elseif($kindex < 2300) 
	{ 
	$dirlone23 = $dirlone23."<dd><span id=\"date\">".date( "Y��n��j��" )."</span> <a href=\"".$kindex.".html\">".$title."</a></dd>\r\n"; 
	if($IsC22==false) 
	{ 
	autowrite($infile22,$dirlone22,$links); 
	echo $infile22." ����2300...........ok<BR>"; 
	$IsC22=true; 
	} 
	if($kindex>=$keyNum-1&&$IsC23==false) 
	{ 
	autowrite($infile23,$dirlone23,$links); 
	echo $infile23." ����...........ok<BR>"; 
	$IsC23=true; 
	} 
	} 
	elseif($kindex < 2400) 
	{ 
	$dirlone24 = $dirlone24."<dd><span id=\"date\">".date( "Y��n��j��" )."</span> <a href=\"".$kindex.".html\">".$title."</a></dd>\r\n"; 
	if($IsC23==false) 
	{ 
	autowrite($infile23,$dirlone23,$links); 
	echo $infile23." ����2400...........ok<BR>"; 
	$IsC23=true; 
	} 
	if($kindex>=$keyNum-1&&$IsC24==false) 
	{ 
	autowrite($infile24,$dirlone24,$links); 
	echo $infile24." ����...........ok<BR>";
	$IsC24=true;
	 } 
	 } 
	 elseif($kindex < 2500) 
	 {
	 $dirlone25 = $dirlone25."<dd><span id=\"date\">".date( "Y��n��j��" )."</span> <a href=\"".$kindex.".html\">".$title."</a></dd>\r\n"; 
	 if($IsC24==false) 
	 { 
	 autowrite($infile24,$dirlone24,$links); 
	 echo $infile24." ����2500...........ok<BR>"; 
	 $IsC24=true; 
	 } 
	 if($kindex>=$keyNum-1&&$IsC25==false) 
	 { 
	 autowrite($infile25,$dirlone25,$links); 
	 echo $infile25." ����...........ok<BR>"; 
	 $IsC25=true; 
	 } 
	 } 
	 elseif($kindex > 2601) 
	 { 
	 $dirlone26 = $dirlone26."<dd><span id=\"date\">".date( "Y��n��j��" )."</span> <a href=\"".$kindex.".html\">".$title."</a></dd>\r\n"; 
	 if($IsC25==false) 
	 { 
	 autowrite($infile25,$dirlone25,$links); 
	 echo $infile25." ����2600...........ok<BR>"; 
	 $IsC25=true; 
	 } 
	 if($kindex>=$keyNum-1&&$IsC26==false) 
	 { 
	 autowrite($infile26,$dirlone26,$links); 
	 echo $infile26." ����...........ok<BR>"; $IsC26=true; 
	 } 
	 } 
	 writestr($filename,$str); 
	 echo $filename." ����ok<BR>"; 
	 unset( $content ); 
	 } 
	 if($IsC26==false) 
	 { 
	 autowrite($infile26,$dirlone26,$links); 
	 echo $infile26." ����...........ok<BR>"; 
	 $IsC26=true; 
	 } 
	 function rarray_rand( $arr ) 
	 { 
	 return mt_rand( 0, count( $arr ) - 1 ); 
	 } 
	 function writestr($fname,$str) 
	 { 
	 $fp=fopen($fname,"w"); 
	 fputs($fp,$str); 
	 fclose($fp); 
	 } 
	 function autowrite($fname,$filedata,$linkdata,$strtitle) ////0�ļ�����  1ʱ�����������  2����   3����
	 { 
	 $dirdata1 = "<!DOCTYPE html PUBLIC \"-//W3C//liD XHTML 1.0 Transitional//EN\" \"http://www.w3.org/TR/xhtml1/liD/xhtml1-transitional.lid\">\r\n"; 	 $dirdata1=$dirdata1."<html xmlns=\"http://www.w3.org/1999/xhtml\">\r\n"; 
	 $dirdata1=$dirdata1."<head>\r\n"; 
	 $dirdata1=$dirdata1."<title>www.gwsanlida.com-".$strtitle."�������ȫ��</title>\r\n"; 
	 $dirdata1=$dirdata1."<meta name=\"keywords\" content=\"ȫ����������!     ������ٷ���վ������,���ӥ,���ӥ,34D,ɭ��֮��,ɭ��֮��,ɭ��֮��,ɭ��֮ӥ,ɭ��֮��,ɭ��֮��,ɭ��֮��,��������,����׼��,��ѧ��׼��,׷��225A,׷��150A,׷��,����,���Ӽ�\"/><meta name=\"description\" content=\"������-�����������Ϸ����գ���Ʒ����������˫���ϣ�|������|����|���Ϲ�|���ӥ|���������\"/>\r\n"; 
	 $dirdata1=$dirdata1."<MEtA http-equiv=Content-type content=\"text/html; charset=gb2312\">\r\n"; 
	 $dirdata1=$dirdata1."<meta http-equiv=\"X-UA-Compatible\" content=\"IE=EmulateIE7\" />\r\n"; 
	 $dirdata1=$dirdata1."<link href=\"style.css\" rel=\"stylesheet\" type=\"text/css\" />\r\n"; 
	 $dirdata1=$dirdata1."</head>\r\n"; 
	 $dirdata1=$dirdata1."<body>\r\n"; 
	 $dirdata1=$dirdata1."�����ڵ�λ�� <a  href=\"http://www.gwsanlida.com/\">�����﹭��-���ӥ</a> > <a  href=\"/gwsanlida/\">������Ѷ</a> > Ƶ����ҳ </div>\r\n"; 
	 $dirdata1=$dirdata1."<script language=\"javascript\" src=\"http://www.gwsanlida.com/data/a.js\"></script>\r\n"; 
	 $dirdata1=$dirdata1."<script language=\"javascript\" src=\"http://www.gwsanlida.com/data/b.js\"></script>\r\n"; 
	 $dirdata1=$dirdata1."<div class=\"wrap\">\r\n"; 
	 $dirdata1=$dirdata1."<div class=\"clear blank10\"></div>\r\n"; 
	 $dirdata1=$dirdata1."  <div class=\"clear blank10\"></div>\r\n"; 
	 $dirdata1=$dirdata1."  <div class=\"newsmain\">\r\n"; 
	 $dirdata1=$dirdata1."      <div id=\"side\">\r\n"; 
	 $dirdata1=$dirdata1."	      <div class=\"sideNav\">\r\n"; 
	 $dirdata1=$dirdata1."		     <h2>��������</h2>\r\n"; 
	 $dirdata1=$dirdata1."		        <ul>{links}</ul>\r\n"; 
	 $dirdata1=$dirdata1."		   <div class=\"sidebottom\"></div>\r\n"; 
	 $dirdata1=$dirdata1."	       </div>\r\n"; 
	 $dirdata1=$dirdata1."       </div>\r\n"; 
	 $dirdata1=$dirdata1."    <div class=\"rightPart\" id=\"about\">\r\n"; 
	 $dirdata1=$dirdata1."      <div class=\"aboutTitle\">\r\n"; 
	 $dirdata1=$dirdata1."        <h3>���Ź���</h3>\r\n"; 
	 $dirdata1=$dirdata1."      </div>\r\n"; 
	 $dirdata1=$dirdata1."      <div class=\"newslist\">\r\n"; 
	 $dirdata1=$dirdata1."        <dl>\r\n"; 
	 $dirdata2="        </dl>\r\n"; 
	 $dirdata2=$dirdata2."        <div id=\"fenye\" class=\"plist\" style=\"margin-top:6px;text-align:right;\">\r\n"; 
	 $dirdata2=$dirdata2."          <table border=\"0\" align=\"right\">\r\n"; 
	 $dirdata2=$dirdata2."            <tr>\r\n"; 
	 $dirdata2=$dirdata2."              <td id=\"pagelist\">\r\n";
	  $dirdata2=$dirdata2."<a href=\"index.html\" class=\"next\">��1ҳ</a>\r\n"; 
	  $dirdata2=$dirdata2."<a href=\"page_2.html\" class=\"next\">��2ҳ</a>\r\n"; 
	  $dirdata2=$dirdata2."<a href=\"page_3.html\" class=\"next\">��3ҳ</a>\r\n"; 
	  $dirdata2=$dirdata2."<a href=\"page_4.html\" class=\"next\">��4ҳ</a>\r\n"; 
	  $dirdata2=$dirdata2."<a href=\"page_5.html\" class=\"next\">��5ҳ</a>\r\n"; 
	  $dirdata2=$dirdata2."<a href=\"page_6.html\" class=\"next\">��6ҳ</a>\r\n"; 
	  $dirdata2=$dirdata2."<a href=\"page_7.html\" class=\"next\">��7ҳ</a>\r\n"; 
	  $dirdata2=$dirdata2."<a href=\"page_8.html\" class=\"next\">��8ҳ</a>\r\n"; 
	  $dirdata2=$dirdata2."<a href=\"page_9.html\" class=\"next\">��9ҳ</a>\r\n"; 
	  $dirdata2=$dirdata2."<a href=\"page_10.html\" class=\"next\">��10ҳ</a>\r\n"; 
	  $dirdata2=$dirdata2."<a href=\"page_11.html\" class=\"next\">��11ҳ</a>\r\n"; 
	  $dirdata2=$dirdata2."<a href=\"page_12.html\" class=\"next\">��12ҳ</a>\r\n"; 
	  $dirdata2=$dirdata2."<a href=\"page_13.html\" class=\"next\">��13ҳ</a>\r\n"; 
	  $dirdata2=$dirdata2."<a href=\"page_14.html\" class=\"next\">��14ҳ</a>\r\n"; 
	  $dirdata2=$dirdata2."<a href=\"page_15.html\" class=\"next\">��15ҳ</a>\r\n"; 
	  $dirdata2=$dirdata2."<a href=\"page_16.html\" class=\"next\">��16ҳ</a>\r\n"; 
	  $dirdata2=$dirdata2."<a href=\"page_17.html\" class=\"next\">��17ҳ</a>\r\n"; 
	  $dirdata2=$dirdata2."<a href=\"page_18.html\" class=\"next\">��18ҳ</a>\r\n"; 
	  $dirdata2=$dirdata2."<a href=\"page_19.html\" class=\"next\">��19ҳ</a>\r\n"; 
	  $dirdata2=$dirdata2."<a href=\"page_20.html\" class=\"next\">��20ҳ</a>\r\n"; 
	  $dirdata2=$dirdata2."<a href=\"page_21.html\" class=\"next\">��21ҳ</a>\r\n"; 
	  $dirdata2=$dirdata2."<a href=\"page_22.html\" class=\"next\">��22ҳ</a>\r\n"; 
	  $dirdata2=$dirdata2."<a href=\"page_23.html\" class=\"next\">��23ҳ</a>\r\n"; 
	  $dirdata2=$dirdata2."<a href=\"page_24.html\" class=\"next\">��24ҳ</a>\r\n"; 
	  $dirdata2=$dirdata2."<a href=\"page_25.html\" class=\"next\">��25ҳ</a>\r\n"; 
	  $dirdata2=$dirdata2."<a href=\"page_26.html\" class=\"next\">��26ҳ</a>\r\n"; 
	  $dirdata2=$dirdata2."</td>\r\n"; 
	  $dirdata2=$dirdata2."            </tr>\r\n"; 
	  $dirdata2=$dirdata2."          </table>\r\n"; 
	  $dirdata2=$dirdata2."        </div>\r\n"; 
	  $dirdata2=$dirdata2."      </div>\r\n"; 
	  $dirdata2=$dirdata2."    </div>\r\n"; 
	  $dirdata2=$dirdata2."  </div>\r\n"; 
	  $dirdata2=$dirdata2." </div>\r\n"; 
	  $dirdata2=$dirdata2."</div>\r\n"; 
	  $dirdata2=$dirdata2."<div class=\"clear blank10\"></div>\r\n"; 
	  $dirdata2=$dirdata2."<div class=\"copyright\">  make by mkCoS<sup>TM</sup>S0���� �й���������ٷ���վwww.gwsanlida.com������Ʒ�������޹�˾�� ��Ȩ����  1998-2013  <br>\r\n"; 
	  $dirdata2=$dirdata2."  <div class=\"copyright\"><p><b><font size=\"4\" color=\"#FF0000\">������ٷ���վ</font></a></b>���������������󹭲�Ʒ������ʹ�ã����������й����ɣ����������﹭�����޹ء�<b><font size=\"4\" color=\"#FF0000\">������</font></a></b>��������| About Crossbow |������|����|���Ϲ�|���ӥ|��Ȩ���� �������й�<b><font size=\"4\" color=\"#FF0000\">������ٷ���վ</font></a></b>����Э�ᡢ�й�<b><font size=\"4\" color=\"#FF0000\">�����ﱼ�ۻ�</font></a></b>�������̻�<b><font size=\"4\" color=\"#FF0000\">���ӥ</font></a></b>���ӥ�ٷ���վ<b><font size=\"4\" color=\"#FF0000\">�����ﱦ���</font></a></b>Э�������������˻�.Copyright &copy; 2002-2013 TT&TG GROUP. ������ٷ���վ���޹�˾ ��Ȩ����  </div></p><script language=\"javascript\" type=\"text/javascript\" src=\"http://www.gwsanlida.com/data/tj.js\"></script>\r\n"; 
	  $dirdata2=$dirdata2."</body>\r\n"; 
	  $dirdata2=$dirdata2."</html>\r\n"; 
	  $lastdata = $dirdata1.$filedata.$dirdata2; 
	  $newlastdata=str_replace( "{links}",$linkdata, $lastdata ); 
	  $fp=fopen($fname,"w"); 
	  fputs($fp,$newlastdata); fclose($fp); 
	  } 
	  function writecss($fname) 
	  { 
	  $cssdata=$cssdata."*{margin:0;padding:0;word-wrap:break-word;}\r\n"; 
	  $cssdata=$cssdata."body{font:12px/1.75 \"����\", arial, sans-serif,'DejaVu Sans','Lucida Grande',Tahoma,'Hiragino Sans GB',STHeiti,SimSun,sans-serif;color:#444;}\r\n"; 
	  $cssdata=$cssdata."body{ background:#FBFCFF url(index-bg.jpg) repeat-x;}\r\n"; 
	  $cssdata=$cssdata."a{text-decoration:none;color:#2C2C2C}\r\n"; 
	  $cssdata=$cssdata."a:hover{text-decoration:underline;color:#F60;}\r\n"; 
	  $cssdata=$cssdata."h1,h3,h4,h5,h6{font-size:12px; margin:0; padding:0; font-weight:100;}\r\n"; 
	  $cssdata=$cssdata."h2{font-size:20px; color:#000; text-align:center;}\r\n"; 
	  $cssdata=$cssdata."h3{font-size:14px; font-weight:600; padding-left:15px;}\r\n"; 
	  $cssdata=$cssdata."a img{border:none;}\r\n"; 
	  $cssdata=$cssdata."div,ul,li,p,form{padding: 0px; margin: 0px;list-style-type: none;}\r\n"; 
	  $cssdata=$cssdata."em{font-style: normal;font-weight: normal;}\r\n"; 
	  $cssdata=$cssdata."table {padding: 0px; margin: 0px;list-style-type: none;}\r\n"; 
	  $cssdata=$cssdata."dt,dl,dd {padding: 0px; margin: 0px;list-style-type: none;}\r\n"; 
	  $cssdata=$cssdata."form{margin:0px;padding:0px;}\r\n"; 
	  $cssdata=$cssdata."tr {padding: 0px; margin: 0px;list-style-type: none;}\r\n"; 
	  $cssdata=$cssdata.".clear {clear:both;height:0px; overflow:hidden;}\r\n"; 
	  $cssdata=$cssdata.".blank10{height:10px;overflow:hidden;}\r\n"; 
	  $cssdata=$cssdata.".blank20{height:20px;overflow:hidden;}\r\n"; 
	  $cssdata=$cssdata."sup{ font-size:9px; color:#555;}\r\n"; 
	  $cssdata=$cssdata.".wrap{width:960px; margin:0px auto;background:#fff; height:100%; overflow:hidden;}\r\n"; 
	  $cssdata=$cssdata.".clear {clear:both;height:0px; overflow:hidden;}\r\n"; 
	  $cssdata=$cssdata.".blank10{height:10px;overflow:hidden;}\r\n"; 
	  $cssdata=$cssdata.".navi{width:940px;margin:0px auto;height:28px;line-height:28px;color:#ccc;background:url(home.gif) no-repeat 5px 8px; padding-left:20px;}\r\n"; 
	  $cssdata=$cssdata.".navi a{color:#ccc}\r\n"; 
	  $cssdata=$cssdata.".navi a:hover{color:#069;text-decoration:none;}\r\n"; 
	  $cssdata=$cssdata.".newsmain{width:960px;margin:0px auto;background:#fff;}\r\n"; 
	  $cssdata=$cssdata.".newsmain .left{width:266px;float:left;}\r\n"; 
	  $cssdata=$cssdata.".newsmain .left .left01{}\r\n"; 
	  $cssdata=$cssdata.".newsmain .left .left01 .tit{background:url(titlebg.gif) no-repeat; font-size:14px; padding-left:12px; font-weight:bold; color:#069; height:40px; line-height:40px;}\r\n"; 
	  $cssdata=$cssdata.".newsmain .left .left01 .left01box{}\r\n"; 
	  $cssdata=$cssdata.".newsmain .left .left01 .left01box ul{}\r\n"; 
	  $cssdata=$cssdata.".newsmain .left .left01 .left01box li{height:37px;line-height:37px;border-bottom:#f1f1f1 1px dashed; padding-left:15px;}\r\n"; 
	  $cssdata=$cssdata.".newsmain .left .left01 .left01box a{font-size:14px;height:37px;line-height:37px;display:block;padding-left:25px;background:url(dotl.gif) no-repeat 0px 14px;padding-left:12px;}\r\n"; 
	  $cssdata=$cssdata.".newsmain .left .left01 .left01box a:hover{color:#069;text-decoration:none;}\r\n"; 
	  $cssdata=$cssdata.".rightPart { border:1px solid #ddd; color:#646363; line-height:25px; float:left; display:inline; margin:0 0 0 8px; padding:0px; width:775px; _width:772px; position:relative; padding-bottom:10px;}\r\n"; 
	  $cssdata=$cssdata.".rightPart #MyContent{padding:10px;font-size:14px;line-height:25px; text-align:left;}\r\n"; 
	  $cssdata=$cssdata.".rightPart #MyContent h2{ height:50px; line-height:50px; text-align:center; border-bottom:#E8E8E8 1px solid; margin-bottom:10px; display:none;}\r\n"; 
	  $cssdata=$cssdata.".rightPart #MyContent dd{ background:url(arrow.png) no-repeat 0px 10px; padding-left:10px;}\r\n"; 
	  $cssdata=$cssdata.".rightPart #MyContent dd span#date{ float:right; color:#999;}\r\n"; 
	  $cssdata=$cssdata.".aboutTitle h3 { display:block; padding:0px 0 0px 40px; font-size:14px; font-weight:bold; color:#4a628d; text-align:left;background:url(titbg.gif) no-repeat;height:38px;line-height:38px;  position:relative;}\r\n"; 
	  $cssdata=$cssdata.".aboutTitle h3 span{ position:absolute; right:10px; top:0px; font-weight:normal; font-size:12px; color:#999;}\r\n"; 
	  $cssdata=$cssdata.".copyright{width:960px; margin:0px auto;line-height:24px; text-align:center; color:#555 ;font-family:\"΢���ź�\";}\r\n"; 
	  $cssdata=$cssdata.".copyright sup{ font-size:8px; font-family:\"΢���ź�\";}\r\n";
	  $cssdata=$cssdata."#about { background:none; height:100%;overflow:hidden;}\r\n"; 
	  $cssdata=$cssdata."#about p { text-align:left; padding:0 40px;}\r\n"; 
	  $cssdata=$cssdata.".newslist{}\r\n"; 
	  $cssdata=$cssdata.".newslist dl{padding:20px;}\r\n"; 
	  $cssdata=$cssdata.".newslist div.first{border-bottom:#ccc 1px dashed; line-height:28px; margin-bottom:10px;padding-bottom:10px; }\r\n"; 
	  $cssdata=$cssdata.".newslist div.first a{font-size:16px;font-weight:bold;color:#CC0000; font-family:\"Times New Roman\", Times, serif}\r\n"; 
	  $cssdata=$cssdata.".newslist div.first a:hover{color:#069;}\r\n"; 
	  $cssdata=$cssdata.".newslist div.first span#date{ float:right; color:#999;}\r\n"; 
	  $cssdata=$cssdata.".newslist dd{height:30px;line-height:30px;background:url(graydot.gif) no-repeat 0px 13px;padding-left:10px; border-bottom:#e8e8e8 1px dotted;}\r\n"; 
	  $cssdata=$cssdata.".newslist span#date{float:right;color:#999;}\r\n"; 
	  $cssdata=$cssdata.".newslist a{font-size:14px;}\r\n"; 
	  $cssdata=$cssdata.".newslist a:hover{color:#069;text-decoration:none;}\r\n"; 
	  $cssdata=$cssdata."#fenye{clear:both;margin:10px;}\r\n"; 
	  $cssdata=$cssdata."#fenye a{text-decoration:non;}\r\n"; 
	  $cssdata=$cssdata."#fenye .prev,#fenye .next{width:52px; text-align:center;}\r\n"; 
	  $cssdata=$cssdata."#fenye a.curr{width:22px;background:#3B85B4; border:1px solid #3185C3; color:#fff; font-weight:bold; text-align:center;}\r\n"; 
	  $cssdata=$cssdata."#fenye a.curr:visited {color:#fff;}\r\n"; 
	  $cssdata=$cssdata."#fenye a{margin:5px 4px 0 0; color:#3B85B4;background:#fff; display:inline-table; border:1px solid #3185C3; float:left; font-size:12px; text-align:center;height:22px;line-height:22px}\r\n"; 
	  $cssdata=$cssdata."#fenye a.num{width:22px;}\r\n"; 
	  $cssdata=$cssdata."#fenye a:visited{color:#3B85B4;}\r\n"; 
	  $cssdata=$cssdata."#fenye a:hover{color:#fff; background:#3B85B4; border:1px solid #3B85B4;float:left;}\r\n"; 
	  $cssdata=$cssdata."#fenye span{line-height:30px;}\r\n"; 
	  $cssdata=$cssdata."#ranks_change_bar #next { background-position:-27px 0; }\r\n"; 
	  $cssdata=$cssdata."#side {float:left; text-align:left; width:174px; }\r\n"; 
	  $cssdata=$cssdata.".sideNav {text-align:left; margin:0 auto 14px auto; width:174px; z-index:2;}\r\n"; 
	  $cssdata=$cssdata.".sideNav ul { border-left:1px solid #ddd; border-right:1px solid #ddd; padding:0px; width:166px;}\r\n"; 
	  $cssdata=$cssdata.".sideNav h2, .sideNav h3 { display:block; text-align:left; padding:0 0 0 20px;}\r\n"; 
	  $cssdata=$cssdata.".sideNav h2 {background:url(leftbg.jpg) no-repeat; height:37px; line-height:37px; font-size:14px; color:#069;}\r\n"; 
	  $cssdata=$cssdata.".sideNav li { cursor:pointer; display:inline; }\r\n"; 
	  $cssdata=$cssdata.".sideNav li a { background:url(arrow.png) 20px 13px no-repeat; text-decoration:none; color:#4a628d; line-height:33px; display:block; width:128px; height:33px; padding:0 0 0 32px; margin:0; overflow:hidden;}\r\n"; 
	  $cssdata=$cssdata.".sideNav .currclass a{ background:url(arrow.png) 20px 13px no-repeat #fff; border-top:1px solid #ddd; border-bottom:1px solid #ddd; text-decoration:none; color:#4a628d; display:block; height:32px; line-height:32px; width:150px; overflow:hidden; position:absolute; z-index:8; top:-1px;}\r\n"; 
	  $cssdata=$cssdata.".sideNav li{ display:block; background:url(leftbg3.jpg) no-repeat; margin:0; padding:0; height:33px; position:relative; z-index:8;}\r\n"; 
	  $fp=fopen($fname,"w"); 
	  fputs($fp,$cssdata); 
	  fclose($fp); 
	  } 

	  function writemoban() 
	  { 
	  $mobandata=$mobandata."<!DOCTYPE html PUBLIC \"-//W3C//liD XHTML 1.0 Transitional//EN\" \"http://www.w3.org/TR/xhtml1/liD/xhtml1-transitional.lid\">\r\n"; 
	  $mobandata=$mobandata."<html xmlns=\"http://www.w3.org/1999/xhtml\">\r\n"; 
	  $mobandata=$mobandata."<head>\r\n"; 
	  $mobandata=$mobandata."<meta http-equiv=\"Content-Type\" content=\"text/html; charset=gb2312\" />\r\n"; 
	  $mobandata=$mobandata."<title>www.gwsanlida.com-{title}�������ȫ��</title>\r\n"; 
	  $mobandata=$mobandata."<meta name=\"keywords\" content=\"{title}ȫ����������! ������ٷ���վ������,���ӥ,���ӥ,34D,ɭ��֮��,ɭ��֮��,ɭ��֮��,ɭ��֮ӥ,ɭ��֮��,ɭ��֮��,ɭ��֮��,��������,����׼��,��ѧ��׼��,׷��225A,׷��150A,׷��,����,���Ӽ�\"/><meta name=\"description\" content=\"{title}������-�����������Ϸ����գ���Ʒ����������˫���ϣ�|������|����|���Ϲ�|���ӥ|���������\"/>\r\n"; 
	  $mobandata=$mobandata."<meta content=\"all\" name=\"robots\" />\r\n"; 
	  $mobandata=$mobandata."<meta http-equiv=\"X-UA-Compatible\" content=\"IE=EmulateIE7\" />\r\n"; 
	  $mobandata=$mobandata."<link href=\"style.css\" rel=\"stylesheet\" type=\"text/css\" />\r\n"; 
	  $mobandata=$mobandata."</head>\r\n"; 
	  $mobandata=$mobandata."<body>\r\n"; 
	  $mobandata=$mobandata."�����ڵ�λ��   <a  href=\"http://www.gwsanlida.com/\">�����﹭��-���ӥ</a> > <a  href=\"/gwsanlida/\">������Ѷ</a> > �������</div>\r\n"; 
	  $mobandata=$mobandata."<script language=\"javascript\" src=\"http://www.gwsanlida.com/data/a.js\"></script>\r\n"; 
	  $mobandata=$mobandata."<script language=\"javascript\" src=\"http://www.gwsanlida.com/data/b.js\"></script>\r\n"; 
	  $mobandata=$mobandata."<div class=\"wrap\">\r\n"; 
	  $mobandata=$mobandata."   <div class=\"clear blank10\"></div>\r\n"; 
	  $mobandata=$mobandata."   <div class=\"clear blank10\"></div>\r\n"; 
	  $mobandata=$mobandata."   <div class=\"newsmain\">\r\n"; 
	  $mobandata=$mobandata."      <div id=\"side\">\r\n"; 
	  $mobandata=$mobandata."	      <div class=\"sideNav\">\r\n"; 
	  $mobandata=$mobandata."		     <h2>��������</h2>\r\n"; 
	  $mobandata=$mobandata."		        <ul>{links}</ul>\r\n"; 
	  $mobandata=$mobandata."		   <div class=\"sidebottom\"></div>\r\n"; 
	  $mobandata=$mobandata."	       </div>\r\n"; 
	  $mobandata=$mobandata."       </div>\r\n"; 
	  $mobandata=$mobandata."       <div class=\"rightPar\" id=\"about\">\r\n"; 
	  $mobandata=$mobandata."            <div class=\"aboutTitle\">\r\n"; 
	  $mobandata=$mobandata."                <h3><span>���ߣ�admin </span> {title}</h3>\r\n"; 
	  $mobandata=$mobandata."            </div>\r\n"; 
	  $mobandata=$mobandata."              <div id=\"MyContent\">\r\n"; 
	  $mobandata=$mobandata."					<div id=\"MyContent\">{content}\r\n"; 
	  $mobandata=$mobandata."					<br/>\r\n"; 
	  $mobandata=$mobandata."					<p align=left >{shang}|{xia}</P>\r\n"; 
	  $mobandata=$mobandata."					</div>\r\n"; 
	  $mobandata=$mobandata."		  </div>\r\n"; 
	  $mobandata=$mobandata."     </div>\r\n"; 
	  $mobandata=$mobandata."  </div>\r\n"; 
	  $mobandata=$mobandata."</div>\r\n"; 
	  $mobandata=$mobandata."<div class=\"clear blank10\"></div>\r\n"; 
	  $mobandata=$mobandata."<div class=\"copyright\">  make by mkCoS<sup>TM</sup>S0���� �й���������ٷ���վwww.gwsanlida.com������Ʒ�������޹�˾�� ��Ȩ����  1998-2013  <br>\r\n"; 
	  $mobandata=$mobandata."  <div class=\"copyright\"><p><b><font size=\"4\" color=\"#FF0000\">������ٷ���վ</font></a></b>���������������󹭲�Ʒ������ʹ�ã����������й����ɣ����������﹭�����޹ء�<b><font size=\"4\" color=\"#FF0000\">������</font></a></b>��������| About Crossbow |������|����|���Ϲ�|���ӥ|��Ȩ���� �������й�<b><font size=\"4\" color=\"#FF0000\">������ٷ���վ</font></a></b>����Э�ᡢ�й�<b><font size=\"4\" color=\"#FF0000\">�����ﱼ�ۻ�</font></a></b>�������̻�<b><font size=\"4\" color=\"#FF0000\">���ӥ</font></a></b>���ӥ�ٷ���վ<b><font size=\"4\" color=\"#FF0000\">�����ﱦ���</font></a></b>Э�������������˻�.Copyright &copy; 2002-2013 TT&TG GROUP. ������ٷ���վ���޹�˾ ��Ȩ����  </div></p><script language=\"javascript\" type=\"text/javascript\" src=\"http://www.gwsanlida.com/data/tj.js\"></script>\r\n"; 
	  $mobandata=$mobandata."</body>\r\n"; 
	  $mobandata=$mobandata."</html>\r\n"; 
	  return $mobandata; 
	  } 
	  
delfile();  //ɾ������
	  ?>
