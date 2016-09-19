
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

class pyColor:
	CLRLST = {'RED':'\033[91m',
			'GREEN':'\033[92m',
			'YELLOW':'\033[93m',
			'BLUE':'\033[94m',
			'LIGHTBLUE':'\033[96m',
			'GREY':'\033[90m',	
			'PURPLE':'\033[95m',
			'BG_RED':'\033[6;30;41m',\
			'BG_GREY':'\033[6;37;40m',\
			'BG_YELLOW':'\033[43m',\
			'BG_WHITE':'\033[47m'}
	STYLE = {'UL':'\033[4m',
			'NORMAL':'\033[0m'}	

	def Fore(self, color):
		return self.CLRLST[color.upper()]
	
	def Style(self, style):
		return self.STYLE[style.upper()]

	def Succ(self, string):
		return(self.CLRLST['GREEN'] + "[+] " + self.STYLE["NORMAL"] + string)

	def Err(self, string):
		return(self.CLRLST['RED'] + "[-] " + self.STYLE["NORMAL"] + string)

	def Info(self, string):
		return(self.CLRLST['BLUE'] + "[*] " + self.STYLE["NORMAL"] + string)

	def Warn(self, string):
		return(self.CLRLST['YELLOW'] + "[!] " + self.STYLE["NORMAL"] + string)

	def Imp(self, string):
		return(self.STYLE["UL"] + string + self.STYLE["NORMAL"])

	def cLine(self, color, string):
		return(self.CLRLST[color] + string + self.STYLE["NORMAL"])
		




