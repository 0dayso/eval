// keydata.h : main header file for the keydata DLL
//

#pragma once

#ifndef __AFXWIN_H__
	#error "include 'stdafx.h' before including this file for PCH"
#endif

#include "resource.h"		// main symbols


// CkeydataApp
// See keydata.cpp for the implementation of this class
//

class CkeydataApp : public CWinApp
{
public:
	CkeydataApp();

// Overrides
public:
	virtual BOOL InitInstance();

	DECLARE_MESSAGE_MAP()
};
