# encoding: utf-8
from __future__ import division, print_function, unicode_literals


###########################################################################################################
#
#
#	General Plugin
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/General%20Plugin
#
#
###########################################################################################################

import re
import os
import codecs


import objc
from GlyphsApp import *
from GlyphsApp.plugins import *
from GlyphsApp.UI import *
from vanilla import*

import AppKit
from vanilla import FloatingWindow, Button, TextBox, Box
from AppKit import NSColor, NSMakeRect, NSColor, NSBezierPath







class FontDash(GeneralPlugin):

	@objc.python_method
	def settings(self):
		self.name = "Font Dashboard"
		self.meaning = self.mapKeys(self.getKeyFile())

	@objc.python_method
	def start(self):
		newMenuItem = NSMenuItem(self.name, self.showWindow_)
		Glyphs.menu[WINDOW_MENU].append(newMenuItem)

	@objc.python_method
	def showWindow_(self, sender):
		
		self.font = Glyphs.font
		self.barWidth = 800
		self.height = 46*len(self.font.masters)+90
		self.barHeight = 18
		self.barWidthDic = {}
		self.colorKeys = {
						"0":(0.85, 0.26, 0.06, 0.5),
						"1":(0.99, 0.62, 0.11, 0.5),
						"2":(0.65, 0.48, 0.20, 0.5),
						"3":(0.97, 0.90, 0.00, 0.5),
						"4":(0.67, 0.95, 0.38, 0.5),
						"5":(0.04, 0.57, 0.04, 0.5),
						"6":(0.06, 0.60, 0.98, 0.5),
						"7":(0.00, 0.20, 0.88, 0.5),
						"8":(0.50, 0.09, 0.79, 0.5),
						"9":(0.98, 0.36, 0.67, 0.5),
						"10":(0.75, 0.75, 0.75, 1),
						"11":(0.25, 0.25, 0.25, 0.5)
						}
		self.w = FloatingWindow((self.barWidth+30,self.height), "Font Dashboard")
		self.w.frame = Group((0, 0, self.barWidth+30,self.height))
		self.w.frame.swatches = CanvasView((0, 0, 0, 0), self)
		self.w.center()
		self.w.open()

	@objc.python_method
	def draw(self, view):
		posY = 10
		posYBar = self.height-26

		for master in self.font.masters:
			setattr(self.w, master.name, TextBox((12, posY, -10, 17), master.name))
			
			xPos = 15
			posY += 22
			posYBar -= 22

			def GetDicLayerColorLabel(self):
				self.LayerColorLabel = {"0":0,"2":0,"3":0,"4":0,"5":0, "6":0, "7":0, "9":0, "10":0, "11":0, "1":0, "8":0}

				for glyph in self.font.glyphs:
					color = str(glyph.layers[master.id].color)
					if color != "None":
						self.LayerColorLabel[color] += 1
				return self.LayerColorLabel
			GetDicLayerColorLabel(self)
		
			for color in self.LayerColorLabel:
				self.barWidthDic[color]= (self.barWidth/len(self.font.glyphs))*self.LayerColorLabel[color]
		
			
			for k, v in self.LayerColorLabel.items():
				if self.barWidthDic[k] != 0:

					rect = NSMakeRect(xPos,posYBar, self.barWidthDic[k], self.barHeight)
					NSColor.colorWithRed_green_blue_alpha_(*self.colorKeys[str(k)]).set()
					path = NSBezierPath.bezierPathWithRoundedRect_xRadius_yRadius_(rect,0,0)
					path.fill()
					NSColor.colorWithRed_green_blue_alpha_(0.4,0.4,0.4,1).set()
					path.stroke()

					
					percent = round(100/len(self.font.glyphs)*self.LayerColorLabel[k])
					if self.barWidthDic[k] >= 30:
						setattr(self.w, master.name+str(k)+"value", TextBox((xPos+3, posY, -10, 17), f"{str(percent)}%",  sizeStyle='small'))
					
					xPos += self.barWidthDic[k]


			rect = NSMakeRect(15,posYBar, self.barWidth, self.barHeight)
			NSColor.colorWithRed_green_blue_alpha_(0.4,0.4,0.4,1).set()
			path = NSBezierPath.bezierPathWithRoundedRect_xRadius_yRadius_(rect,0,0)
			path.stroke()

			posY += 22
			posYBar -= 22

			xLabel = 15

		posY += 20
		posYBar -= 16


		for k in self.LayerColorLabel.keys():
			if k == "5":
				posY += 18
				posYBar -= 18
				xLabel = 15

			if k == "10":
				posY += 18
				posYBar -= 18
				xLabel = 15

			#rect = NSMakeRect(xLabel,posYBar, 10, 10)
			NSColor.colorWithRed_green_blue_alpha_(*self.colorKeys[str(k)]).set()
			NSBezierPath.bezierPathWithOvalInRect_(((xLabel,posYBar), (10, 10))).fill()
			NSColor.colorWithRed_green_blue_alpha_(0.4,0.4,0.4,1).set()
			NSBezierPath.bezierPathWithOvalInRect_(((xLabel,posYBar), (10, 10))).stroke()

			#NSBezierPath.bezierPathWithOvalInRect_(((0, height - (num * self.elementHeight)), (keyDiameter, keyDiameter))).fill()
			xLabel += 14

			meaning = self.meaning[k]
			setattr(self.w, meaning, TextBox((xLabel, posY, -10, 17), meaning,  sizeStyle='small'))
			xLabel += 800/4.3
				

	@objc.python_method
	def getKeyFile(self):
		keyFile = None
		try:
			thisDirPath = os.path.dirname(self.font.filepath)
			localKeyFile = thisDirPath + '/color.txt'
			if os.path.exists(localKeyFile):
				keyFile = localKeyFile
		except:
			pass

		dirInfo = os.path.expanduser("~/Library/Application Support/Glyphs 3/info")
		if not os.path.exists(dirInfo):
			os.mkdir(dirInfo)

		if keyFile is None:
			keyFile = os.path.expanduser('~/Library/Application Support/Glyphs 3/info/color.txt')

		if not os.path.exists(keyFile):
			f = open(keyFile,"w+")
			f.write("red=Red\norange=Orange\nbrown=Brown\nyellow=Yellow\nlightGreen=Light green\ndarkGreen=Dark green\nlightBlue=Light blue\ndarkBlue=Dark blue\npurple=Purple\nmagenta=Magenta\nlightGray=Light Gray\ncharcoal=Charcoal") 
		else:
			pass
		return keyFile

	# Build Dic from color.txt content
	@objc.python_method
	def mapKeys(self, keyFile):

		self.colourLabels = {}
		if os.path.exists(keyFile):
			with codecs.open(keyFile, "r", "utf-8") as file:
				for line in file:
					colour = re.match(r".*?(?=\=)", line).group(0)
					label = re.search(r"(?<=\=).*", line).group(0)
					self.colourLabels[colour] = label
		switch = {}
		replace = {"red":"0", "orange":"1", "brown":"2", "yellow":"3", "lightGreen":"4", "darkGreen":"5", "lightBlue":"6", "darkBlue":"7", "purple":"8", "magenta":"9", "lightGray":"10", "charcoal":"11"}

		for k, v in self.colourLabels.items():
			switch[replace[k]] = v

		self.colourLabels = switch
		return self.colourLabels


	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
