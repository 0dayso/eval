# -*- coding: utf-8 -*-
#windows  #无控制台 
#console   #有控制台

from distutils.core import setup  

import py2exe


setup(version = "yijuhua_CS",description = "0.1",
    name = "postadmin",zipfile=None,
    console=[{"script": "yijuhua_CS.py", "icon_resources": [(1,"App.ico")]}],
    options={"py2exe":{"includes":["sip"]}},
    )

