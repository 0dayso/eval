#include "StdAfx.h"
#include "functions.h"

#include <IPHlpApi.h>
#pragma comment(lib,"Iphlpapi.lib")

LPSTR GetMacInfo()
{
	// 虚拟机加密技术，防破解
	// 软件加密起始标记
	VMProtectBegin ;
	static TCHAR buffer[100] ;
	memset(buffer, 0, sizeof(buffer)) ;

	CString strMac = "" ;
	PIP_ADAPTER_INFO pAdapterInfo;
	PIP_ADAPTER_INFO pAdapter = NULL,pAdapterUse = NULL;
	DWORD dwRetVal = 0;

	pAdapterInfo = (IP_ADAPTER_INFO *) malloc( sizeof(IP_ADAPTER_INFO) );
	ULONG ulOutBufLen = sizeof(IP_ADAPTER_INFO);

	// Make an initial call to GetAdaptersInfo to get
	// the necessary size into the ulOutBufLen variable
	if (GetAdaptersInfo( pAdapterInfo, &ulOutBufLen) == ERROR_BUFFER_OVERFLOW) 
	{
		free(pAdapterInfo);
		pAdapterInfo = (IP_ADAPTER_INFO *) malloc (ulOutBufLen); 
		if (pAdapterInfo == NULL) 
		{
			//printf("Error allocating memory needed to call GetAdaptersinfo\n");
			return buffer;
		}
	}
	CString strDesUse = _T("");
	if ((dwRetVal = GetAdaptersInfo( pAdapterInfo, &ulOutBufLen)) == NO_ERROR) 
	{
		pAdapter = pAdapterInfo;
		while( NULL != pAdapter) 
		{
			if( pAdapter->Type == MIB_IF_TYPE_ETHERNET)
			{
				// 以太网卡
				CString strdes = pAdapter->Description ;
				strdes = strdes.MakeLower() ;
				if( strdes.Find(_T("usb")) < 0)
				{
					if( strDesUse.GetLength() <= 0 || 
						strDesUse.Compare(strdes) < 0)
					{
						pAdapterUse = pAdapter;
						strDesUse = strdes ;
					}
				}
			}

			pAdapter = pAdapter->Next ;
		}
	}
	if( pAdapterUse != NULL )
	{
		sprintf_s(buffer,100,_T("[%02x-%02x-%02x-%02x-%02x-%02x]"),
			pAdapterUse->Address[0],
			pAdapterUse->Address[1],
			pAdapterUse->Address[2],
			pAdapterUse->Address[3],
			pAdapterUse->Address[4],
			pAdapterUse->Address[5]);

	}
	if (pAdapterInfo)
		free(pAdapterInfo);

	return buffer ;
    // 软件加密结束位置
	VMProtectEnd ;
}
