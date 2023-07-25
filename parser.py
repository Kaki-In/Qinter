#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  __init__.py
#
#  Copyright 2023 Kaki In <kaki@mifamofi.net>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

"""
XML parser (by hand)
"""

from . import *

def isValidName(name):
	"""
	Returns True if the given name can be used as a tagname or attribute
	name.
	"""
	for i in name:
		if not (i.isalpha() or i.isdigit() or i in ".:_"):
			return False
	return True

def split(data):
	"""
	Returns a list containing the different elements openures and
	closures
	"""
	lines = data.split("\n")
	for i in range(len(lines)):
		while lines[i] and lines[i][0] in " \t":
			lines[i] = lines[i][1:]
		while lines[i] and lines[i][-1] in " \t":
			lines[i] = lines[i][:-1]
	while "" in lines:
		lines.remove("")
	data = ""
	for i in lines:
		if not i[0] in "</":data += " "
		data += i
	data = data.replace("><", ">\n<").split("\n")
	return data

def parse(data):
	"""
	Returns a parsed object containing the elements in the parsed string
	"""
	datalist = split(data)
	elembase = CustomView("LinearLayout", layout_width=View.FILL_PARENT, layout_height=View.FILL_PARENT)
	elemused = elembase
	arb = []
	for i in datalist:
		if   i[0] != "<" or i[-1] != ">":
			raise SyntaxError(i)
		elif i[1] == "/":
			elemname = i[2:-1]
			if not isValidName(elemname) or elemused is None or elemused.getTagName() != elemname:
				print(elemused.getTagName(), elemname)
				raise SyntaxError(i)
			elemused = arb.pop( -1 )
		else:
			elemdivision = [""]
			actQuote = None
			lastIsSlash = False
			parenthesis = ""
			for k in i[1:-1]:
				if str(actQuote) in "\"'":
					if lastIsSlash:
						elemdivision[-1] += "\\" + k
						lastIsSlash = False
					elif k is actQuote:
						actQuote = None
						elemdivision[-1] += k
					else:
						elemdivision[-1] += k
				elif parenthesis:
					if k in "[{(":
						parenthesis += k
					elif k in "]})":
						i = "]})".index(k)
						if "[{(" [ i ] != parenthesis[ -1 ]:
							raise SyntaxError("Unmatched parenthesis", repr(parenthesis[ -1 ]))
						parenthesis = parenthesis[ :-1 ]
					elemdivision[ -1 ] += k
				else:
					if k == " ":
						if elemdivision[ -1 ]:
							elemdivision.append("")
					elif k in "\"'":
						actQuote = k
						elemdivision[-1] += k
					elif k in "[{(":
						parenthesis += k
						elemdivision[ -1 ] += k
					elif k in "]})":
						raise SyntaxError("Unmatched parenthesis", k)
					else:
						elemdivision[-1] += k
			name = elemdivision[0]
			if not isValidName(name):
				raise SyntaxError(i)
			elem = CustomView(name, layout_width=View.FILL_PARENT, layout_height=View.FILL_PARENT)
			elemused.addView(elem)
			arb.append(elemused)
			elemused = elem
			keepelem = True
			if elemdivision[-1][-1] == "/":
				elemdivision[-1] = elemdivision[-1][:-1]
				keepelem = False
			for d in elemdivision[1:]:
				if "=" in d:
					attrname = d[:d.index("=")]
					attrval = d[d.index("=") + 1:]
					if attrname.startswith('android:'):
						attrname = attrname[ 8 : ]
					if attrname.startswith('qinter:'):
						attrname = attrname[ 7 : ]
					if not isValidName(attrname):
						raise SyntaxError(str(d), str(i))
					try:
						elemused.set(attrname, eval(attrval))
					except :
						raise SyntaxError(i)
				else:
					raise SyntaxError(i)
			if not keepelem:
				elemused = arb.pop( -1 )
	if elemused is not elembase:
		raise SyntaxError("")
	return elembase
