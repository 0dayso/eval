// mac_key.cpp : Defines the entry point for the DLL application.
//

#include "stdafx.h"
#include "Nb30.h"
// BOOL APIENTRY DllMain( HANDLE hModule, 
//                        DWORD  ul_reason_for_call, 
//                        LPVOID lpReserved
// 					 )
// {
//     return TRUE;
// }

#include <windows.h>
#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#pragma comment(lib,"Netapi32.lib")
#include<iomanip.h>
#include<fstream.h>

extern "C" _declspec(dllexport) int mac_key();

/*
Dev C++ -> include libnetapi32.a
BCC 5.5 or VC++ -> #pragma comment(lib,"netapi32.lib")
*/
 
typedef struct _ASTAT_
{
    ADAPTER_STATUS adapt;
    NAME_BUFFER NameBuff [30];
} ASTAT, *PASTAT;
 
void getMac(char * mac)
{
    ASTAT Adapter;
    NCB Ncb;
    UCHAR uRetCode;
    LANA_ENUM lenum;
    int i = 0;
 
    memset(&Ncb, 0, sizeof(Ncb));
    Ncb.ncb_command = NCBENUM;
    Ncb.ncb_buffer = (UCHAR *)&lenum;
    Ncb.ncb_length = sizeof(lenum);
 
    uRetCode = Netbios( &Ncb );
    //printf( "The NCBENUM return adapter number is: %d \n ", lenum.length);
    for(i=0; i < lenum.length ; i++)
    {
        memset(&Ncb, 0, sizeof(Ncb));
        Ncb.ncb_command = NCBRESET;
        Ncb.ncb_lana_num = lenum.lana[i];
        uRetCode = Netbios( &Ncb );
 
        memset(&Ncb, 0, sizeof(Ncb));
        Ncb.ncb_command = NCBASTAT;
        Ncb.ncb_lana_num = lenum.lana[i];
        strcpy((char *)Ncb.ncb_callname, "* ");
        Ncb.ncb_buffer = (unsigned char *) &Adapter;
        Ncb.ncb_length = sizeof(Adapter);
        uRetCode = Netbios( &Ncb );
 
        if (uRetCode == 0)
        {
            //sprintf(mac, "%02x-%02x-%02x-%02x-%02x-%02x ",
            sprintf(mac, "%02X%02X%02X%02X%02X%02X ",
                    Adapter.adapt.adapter_address[0],
                    Adapter.adapt.adapter_address[1],
                    Adapter.adapt.adapter_address[2],
                    Adapter.adapt.adapter_address[3],
                    Adapter.adapt.adapter_address[4],
                    Adapter.adapt.adapter_address[5]
                   );
            //printf( "The Ethernet Number on LANA %d is: %s\n ", lenum.lana[i], mac);
        }
    }
}

///////////////////////////////////////
//加密解密
// 常量
static char base64[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
// 加密函数
int base64_encode(const void *data, int size, char **str)
{
	char *s, *p;
	int i;
	int c;
	const unsigned char *q;
	
	p = s = (char*)malloc(size*4/3+4);
	if (p == NULL)
		return -1;
	q = (const unsigned char*)data;
	i=0;
	for(i = 0; i < size;){
		c=q[i++];
		c*=256;
		if(i < size)
			c+=q[i];
		i++;
		c*=256;
		if(i < size)
			c+=q[i];
		i++;
		p[0]=base64[(c&0x00fc0000) >> 18];
		p[1]=base64[(c&0x0003f000) >> 12];
		p[2]=base64[(c&0x00000fc0) >> 6];
		p[3]=base64[(c&0x0000003f) >> 0];
		if(i > size)
			p[3]='=';
		if(i > size+1)
			p[2]='=';
		p+=4;
	}
	*p=0;
	*str = s;
	return strlen(s);
}

char* MyEncode(char *str)  //加密
{                          //bese64 加上两个异或
	int		i, len;  
	char	*p;
	char	*s, *data;
	len = strlen(str) + 1;
	//strlen求字符串长度 +1
	s = (char *)malloc(len);
	//malloc分配字节
	memcpy(s, str, len);
	//memcpy复制内容
	for (i = 0; i < len; i++)
	{
		s[i] ^= 0x19;
		s[i] += 0x86;  //^是异或
	}
	base64_encode(s, len, &data);  //64位编码
	free(s);
	return data;
}

// 解密函数
static int pos(char c)
{
	char *p;
	for(p = base64; *p; p++)
		if(*p == c)
			return p - base64;
		return -1;
}

int base64_decode(const char *str, char **data)
{
	const char *s, *p;
	unsigned char *q;
	int c;
	int x;
	int done = 0;
	int len;
	s = (const char *)malloc(strlen(str));
	q = (unsigned char *)s;
	for(p=str; *p && !done; p+=4){
		x = pos(p[0]);
		if(x >= 0)
			c = x;
		else{
			done = 3;
			break;
		}
		c*=64;
		
		x = pos(p[1]);
		if(x >= 0)
			c += x;
		else
			return -1;
		c*=64;
		
		if(p[2] == '=')
			done++;
		else{
			x = pos(p[2]);
			if(x >= 0)
				c += x;
			else
				return -1;
		}
		c*=64;
		
		if(p[3] == '=')
			done++;
		else{
			if(done)
				return -1;
			x = pos(p[3]);
			if(x >= 0)
				c += x;
			else
				return -1;
		}
		if(done < 3)
			*q++=(c&0x00ff0000)>>16;
		
		if(done < 2)
			*q++=(c&0x0000ff00)>>8;
		if(done < 1)
			*q++=(c&0x000000ff)>>0;
	}
	
	len = q - (unsigned char*)(s);
	
	*data = (char*)realloc((void *)s, len);
	
	return len;
}

char* MyDecode(char *str)  //解密
{
	int		i, len;
	char	*data = NULL;
	len = base64_decode(str, &data);
	
	for (i = 0; i < len; i++)
	{
		data[i] -= 0x86;
		data[i] ^= 0x19;
	}
	return data;
}

///////////////////////////////////////

#include <stdio.h>
#include <string>
#include <stdlib.h>
using namespace std;
#define FILENAME ("/home/snail/work_dir/linux_c_work/file.bin")
void add_txt(string name,char* data)
{
	char*name2=const_cast<char*>(name.c_str());
	FILE *file=fopen(name2,"w+");
	if(file==NULL) return;
	fputs(data,file);
	fclose(file);
}

char* open_txt(string name)
{
	char str[1024]={0};
	char*name2=const_cast<char*>(name.c_str());
	FILE *file=fopen(name2,"r");
	if(file==NULL) return 0;
	fgets(str,1024, file);
	fclose(file);
	//printf( "data--%s\n ",str);
	return str;
}

char* csTrim(char* cs)
{
    char* ret = cs;
    char* pc = new char[strlen(cs) + 1];
    int pos = strspn(cs , "\t \n");     // 查找非空白处pos
    strcpy(pc , cs + pos);
    char* end = pc;
    while (*end++)     // 找到字符串末位的'\0'，
        ;              // 因为上面 end++，实际指针在 '\0'的后一个
    end -= 2;          // 所以退2格，回到字符串最后一个字母
    while (*end == ' ' || *end == '\t' ||  *end == '\n') {
        *end-- = '\0';
    }
    strcpy(cs , pc);
    delete[] pc;
    return ret;
}


//----------------------------------------------------------

//----------------------------------------------------------

#include <string.h> 
#include "stdafx.h"
#include <iostream>
#include <assert.h>
int mac_key()
{

	char *mac=new char[NULL];
    getMac(mac);
    printf( "key2.txt:%s\n", mac);
	add_txt("key2.txt",mac);
	char *KEY1=MyEncode(mac);  //加密
	char *data_KEY1=open_txt("key1.txt");
	char *KEY2=MyDecode(data_KEY1);  //解密
// 	string s1(mac);
// 	string s2(KEY2);
//  	printf( "s11--%s\n",mac);
//  	printf( "s22--%s\n",KEY2);
 	if (strcmp(mac,KEY2))
	{//ok
		printf ("KEY OK");
 		return 1;
	} 
	else
	{//no
		return 0;
	}
	
	// 	printf( "KEY11--%s\n ", KEY1);
	// 	printf( "data_KEY11--%s\n ", data_KEY1);
	// 	printf( "KEY22--%s\n ", KEY2);
//  	add_txt("key2.txt",mac);
}