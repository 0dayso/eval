#pragma once

//#ifndef DLLFUN_TYPE
#if defined(_DLL_MODULE_)
	#pragma message(_T("-------------�������������͡�-------"))
	#define DLLFUN_TYPE EXTERN_C _declspec(dllexport)
#else
	#pragma message(_T("-------------�����뺯�����͡�-------"))
	#define DLLFUN_TYPE EXTERN_C _declspec(dllimport)
#endif
//#endif


DLLFUN_TYPE LPSTR GetMacInfo() ;