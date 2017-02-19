<?php

                 $phiz=array(
            'zhuakuang'=>'抓狂',
           );
             $phiz['user_id'] = 1;
         $phiz['user_type'] = 1;
         C($phiz,'name');
         //将数组写入文件之中
         F('Server_ini',$phiz,'Server_ini/');
         //phiz1是php文件名
         //调用文件 数据
         $phiz=F('Server_ini','','Server_ini/');
         $_config='Server_ini/Server_ini.php';
         p($phiz);

class data{
    /*public 表示全局，类内部外部子类都可以访问；
    private表示私有的，只有本类内部可以使用；
    protected表示受保护的，只有本类或子类或父类中可以访问；
    */
    xxxxxxxxxxx;//数据库路径
    protected $_filePath="./Server_ini/";
    //标记修改的数据项
    protected $_write=FALSE;

    function open_array($name=""){  //读取数组
        $filePath =$this->_filePath. $name.'.php';
        if(is_file($filePath)){
            return include($filePath);
        }
       echo $this->_filePath;
    }

    function open_array1($name=""){  //读取数组
        $filePath =$name;
        if(is_file($filePath)){
            return include($filePath);
        }
       echo $this->_filePath;
    }

}

?>



