
# Font Dashboard

Font Dashboard is a Genearl Plugin which opens a window with Progress Bar showing Layer Colors for all Masters.  
Available from `Window > Font Dashboard`

<img src="https://github.com/HugoJourdan/Font-Dashboard/blob/main/FontDashboard-preview.jpg" width="800" />

It requires a `ColorNames.txt` file stored in either `~/Library/Application Support/Glyphs 3/info` or the same directory as the current Glyphs source file. Preference is given to the latter allowing for the sharing of the `ColorNames.txt` file with glyphs source files to retain labelling information between project contributors. 

The `ColorNames.txt` file requires the formatting `colorName=meaning`, with each key on a newline and with no space surrounding the '='.  
An example, with the defined colorNames is given below. 

```
red=Red
orange=Orange
brown=Brown
yellow=Yellow
lightGreen=Light green
darkGreen=Dark green
lightBlue=Light blue
darkBlue=Dark blue
purple=Purple
magenta=Magenta
lightGray=Light Gray
charcoal=Charcoal
```

Color order can be modified by changing line order and a color can be hided by deleting the line associated with it.
Here is an example :

```
red=Red
magenta=Magenta
yellow=Yellow
lightBlue=Light blue
purple=Purple
lightGreen=Light green
```

# TIPS

To  quickly export the dashboard, press ` ⇧ + ⌘ + 4 ` , then Space to screenshot Font Dashboard window.
