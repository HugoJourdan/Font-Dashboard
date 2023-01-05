#MenuTitle: Color Font Dashboard Markdown
# -*- coding: utf-8 -*-
__doc__="""
Generate .md file,which summarises the progress of the open glyph file according to Layer Colors Labels set.
"""

from glyphsLib import*
import codecs
import os
import re
import datetime
import subprocess
import time

from glyphsLib import GSFont

import argparse
parser = argparse.ArgumentParser(description='A test program.')
parser.add_argument("print_string", help="Prints the supplied argument.")
args = parser.parse_args()

if args.print_string.endswith(".glyphspackage"):
	command = "glyphspkg " + args.print_string
	os.system(command)
	glyphs_file = args.print_string.removesuffix(".glyphspackage") + ".glyphs"
else:
	glyphs_file = args.print_string
font = GSFont(glyphs_file)
filePath = font.filepath
nbGlyphs = len([glyph for glyph in font.glyphs if glyph.export])



def Get_Key_File():
	keyFile = None
	try:
		thisDirPath = os.path.dirname(font.filepath)
		localKeyFile = thisDirPath + '/colorNames.txt'
		if os.path.exists(localKeyFile):
			keyFile = localKeyFile
	except:
		pass

	dirInfo = os.path.expanduser("~/Library/Application Support/Glyphs 3/info")

	if keyFile is None:
		keyFile = os.path.expanduser('~/Library/Application Support/Glyphs 3/info/colorNames.txt')

	if not os.path.exists(keyFile):
		f = open(keyFile,"w+")
		f.write("None=🫥 None\nred=🚨 Red\norange=🦊 Orange\nbrown=🪵 Brown\nyellow=🌼 Yellow\nlightGreen=🍀 Light green\ndarkGreen=🫑 Dark green\nlightBlue=💎 Light blue\ndarkBlue=🌀 Dark blue\npurple=🔮 Purple\nmagenta=🌺 Magenta\nlightGray=🏐 Light Gray\ncharcoal=🎱 Charcoal")
	else:
		pass
	return keyFile

# Build Dic from ColorNames.txt content
def Map_Keys(keyFile):

	colourLabels = {}
	if os.path.exists(keyFile):
		with codecs.open(keyFile, "r", "utf-8") as file:
			for line in file:
				colour = re.match(r".*?(?=\=)", line).group(0)
				label = re.search(r"(?<=\=).*", line).group(0)
				colourLabels[colour] = label
	switch = {}
	replace = {"None":None,"red":0, "orange":1, "brown":2, "yellow":3, "lightGreen":4, "darkGreen":5, "lightBlue":6, "darkBlue":7, "purple":8, "magenta":9, "lightGray":10, "charcoal":11}

	for k, v in colourLabels.items():
		switch[replace[k]] = v

	colourLabels = switch.copy()
	for k,v in switch.items():
		if not v:
			colourLabels.pop(k)
	return colourLabels

def buildMasterColorLayersDic():
	font = GSFont(glyphs_file)
	mastersColorLayersDic = {}
	for master in font.masters:
		masterName = master.name
		mastersColorLayersDic[master.id]={}
		for glyph in font.glyphs:
			for layer in glyph.layers:
				if layer.name == masterName and layer.associatedMasterId == master.id:
					layerColor = layer.color
					if layerColor == None and glyph.color != None:
						layerColor = glyph.color

					if not str(layerColor) in mastersColorLayersDic[master.id]:
						mastersColorLayersDic[master.id][str(layerColor)] = []
					glyphName = glyph.string if glyph.string else glyph.name
					mastersColorLayersDic[master.id][str(layerColor)].append(glyphName)
	return mastersColorLayersDic

def reportColorChanges():
	reportColorChanges = {}
	
	for MASTER in masterLayerColorGlyphs:
		reportColorChanges[MASTER]={}
		for color in masterLayerColorGlyphs[MASTER]:
			for glyphName in masterLayerColorGlyphs[MASTER][color]:
				for oldColor in oldValues[MASTER]:
					if glyphName in oldValues[MASTER][oldColor] and color != oldColor:
						reportColorChanges[MASTER][glyphName]=[oldColor, color]

	return reportColorChanges

if not font.userData['com.HugoJourdan.saveMastersColorLayers']:
	font.userData['com.HugoJourdan.saveMastersColorLayers'] = buildMasterColorLayersDic()

# Build data for Advanced Report
oldValues = font.userData['com.HugoJourdan.saveMastersColorLayers']
masterLayerColorGlyphs = buildMasterColorLayersDic()

reportColorChanges = reportColorChanges()



now = datetime.datetime.now()
date = now.strftime("%m%d%Y")


colorMeaningDic = Map_Keys(Get_Key_File())
colorPNGs = {0:"https://raw.githubusercontent.com/HugoJourdan/Font-Dashboard-2/main/colorPNG/0.png?token=GHSAT0AAAAAABYZ6FTURHZLXVWZR2RINGJYY5UERAA",
             1:"https://raw.githubusercontent.com/HugoJourdan/Font-Dashboard-2/main/colorPNG/1.png?token=GHSAT0AAAAAABYZ6FTUFYO3FKBXVOLEHEQEY5UEG4Q",
             2:"https://raw.githubusercontent.com/HugoJourdan/Font-Dashboard-2/main/colorPNG/2.png?token=GHSAT0AAAAAABYZ6FTVDAQYDMEQIXTTWD6SY5UEHKQ",
             3:"https://raw.githubusercontent.com/HugoJourdan/Font-Dashboard-2/main/colorPNG/3.png?token=GHSAT0AAAAAABYZ6FTU2HOOAV7RR3JHSXNAY5UEIEQ",
             4:"https://raw.githubusercontent.com/HugoJourdan/Font-Dashboard-2/main/colorPNG/4.png?token=GHSAT0AAAAAABYZ6FTVI7Z2CWYSTEMJLUJWY5UEIQA",
             5:"https://raw.githubusercontent.com/HugoJourdan/Font-Dashboard-2/main/colorPNG/5.png?token=GHSAT0AAAAAABYZ6FTVUUKUIBGIJLOKQQOMY5UEI3A",
             6:"https://raw.githubusercontent.com/HugoJourdan/Font-Dashboard-2/main/colorPNG/5.png?token=GHSAT0AAAAAABYZ6FTVUUKUIBGIJLOKQQOMY5UEI3A",
             7:"https://raw.githubusercontent.com/HugoJourdan/Font-Dashboard-2/main/colorPNG/7.png?token=GHSAT0AAAAAABYZ6FTV7IWONGRUUFXDU22SY5UEJLA",
             8:"https://raw.githubusercontent.com/HugoJourdan/Font-Dashboard-2/main/colorPNG/8.png?token=GHSAT0AAAAAABYZ6FTUGQS2FGWYPZJVP4ASY5UENQA",
             9:"https://raw.githubusercontent.com/HugoJourdan/Font-Dashboard-2/main/colorPNG/9.png?token=GHSAT0AAAAAABYZ6FTVWSLV6NT5IK3DOR3MY5UENXA",
             10:"https://raw.githubusercontent.com/HugoJourdan/Font-Dashboard-2/main/colorPNG/10.png?token=GHSAT0AAAAAABYZ6FTUXRVLHQA6I25S4ZMGY5UEOCQ",
             11:"https://raw.githubusercontent.com/HugoJourdan/Font-Dashboard-2/main/colorPNG/11.png?token=GHSAT0AAAAAABYZ6FTUT4G3TMXA5XDJYD5KY5UEOIA",}

markdown = ""

markdown += f'''
# {font.familyName}  
Report from : {now.strftime("%m-%d-%Y")}  

### Font Info
```
Version      : {font.versionMajor}.{font.versionMinor}  
Axes         : {', '.join([axis.axisTag for axis in font.axes])}  
Masters      : {len(font.masters)}  
Instances    : {len(font.instances)}  
Glyphs       : {nbGlyphs}  
```

<br>
'''

for master in font.masters:
	masterName = master.name
	layerColorDic = {None:0, 0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0}
	for glyph in font.glyphs:
		layerColor = glyph.layers[master.id].color
		if layerColor == None and glyph.color != None:
			layerColor = glyph.color
		if layerColor != None:
			layerColorDic[layerColor] += 1
		else:
			layerColorDic[None] += 1

	markdown += f'''
<details>
<summary>{masterName}</summary>\n
<br>

| Color  | Meaning  | Progress | Diff    | Count  | % |
| -------  | -------  | -------- | ------- | -------  | -------- |
'''

	for color, count in layerColorDic.items():
		if color in layerColorDic and count != 0:
			colorMeaning = colorMeaningDic[color]
			percent = round(count/nbGlyphs*100)
			dif = "+0"
			try :
				oldValue = len(oldValues[master.id][color]) 
				dif = int(layerColorDic[color]-oldValue)
				dif = f"+{dif}" if dif >=0 else f"{dif}"
			except:pass
				
			# If data from last script execution
			if any(reportColorChanges.values()):
				#markdown += ""
				pass

			progressBar = round(percent/2.5)*"█"
			progressBar += (40-len(progressBar))*"░"
			markdown += f"| ![{color}](https://github.com/HugoJourdan/Font-Dashboard-2/blob/main/colorPNG/{color}.png) | {colorMeaning} | {progressBar} | `{dif}` | `{count}/{nbGlyphs}` | `{percent}%`  |\n"
	#markdown += f"</details>\n\n<!---{masterLayerColorGlyphs[master.id]}\n\n---\n"
	

	
	

	if any(reportColorChanges.values()):
		markdown += f"<details>\n<summary>Advance report</summary>\n\n<br>\n\n"
		markdown += "| Glyph  | Old Status  | New Status |  \n"
		markdown += "| -------  | -------  | -------- |  \n"

		if master.id in reportColorChanges:
			for glyph in reportColorChanges[master.id]:
				
				oldColor = reportColorChanges[master.id][glyph][0]
				newColor = reportColorChanges[master.id][glyph][1]

				markdown += f"| {glyph} | ![{oldColor}](https://github.com/HugoJourdan/Font-Dashboard-2/blob/main/colorPNG/{oldColor}.png) {colorMeaningDic[int(oldColor)]} | ![{newColor}](https://github.com/HugoJourdan/Font-Dashboard-2/blob/main/colorPNG/{newColor}.png) {colorMeaningDic[int(newColor)]} |  \n"
				
		markdown += "</details>\n\n"

	markdown += "<!---\n"
	# for color in masterLayerColorGlyphs[master.id]:
	# 	if color != "None":
	# 		markdown += f"{colorMeaningDic[int(color)]} : {masterLayerColorGlyphs[master.id][color]}\n"
	# 	else:
	# 		markdown += f"{colorMeaningDic[color]} : {masterLayerColorGlyphs[master.id][color]}\n"
	markdown += "-->\n\n"
	markdown += f"</details>\n\n---\n\n"

# Save current Layer Color datas in font.userData
font.userData['com.HugoJourdan.saveMastersColorLayers'] = masterLayerColorGlyphs
font.save(glyphs_file)

outpout = f"{os.path.dirname(filePath)}/{date}_ColorLabelReporter_{os.path.basename(filePath).split('.')[0]}.md"
with open(outpout, 'w') as f:
	f.write(markdown)
	f.close()

if args.print_string.endswith(".glyphspackage"):
    os.remove(glyphs_file)