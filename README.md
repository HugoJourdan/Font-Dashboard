# Font Dashboard

<img alt="Font Dahsboard screenshot" src="https://user-images.githubusercontent.com/76793951/210555511-04db9b29-86c0-4d28-b63e-6afbdf07444d.png">

Font Dashboard is a python script which generate markdown reporter showing Layer/Glyph Color Labels `.glyphs` or `.glyphspackage` file.
Layer Color Labels are used in priority, if no Layer Color Label are assigned, it will use Glyph Color Label.

<br>
<br>

# How to use it

If you don't have glyphLib and glyphspkg packages installed:

1. Open Terminal
2. Type `pip3 install -r`, drag and drop `requirement.txt` and press `Enter`

Else :
1. Clone/Download this repository
4. Open "Terminal"
5. Type `python` in Terminal
6. Drag and drop `fontDashboard.py`
7. Drag and drop your `.glyph` or `.glyphpackage`
8. Press `Enter` 

It will create a markdown file next to your glyph file following this nomenclature : `{date}_FontDashboard_{glyphFileName}`

<br>

# Customised meanings

Font Dashboard requires a `colorNames.txt` file stored in either `~/Library/Application Support/Glyphs 3/info` or the same directory as the current Glyphs source file.  Preference is given to the latter allowing for the sharing of the `colorNames.txt` file with glyphs source files to retain labelling information between project collaborators.
For customise it, you just have to edit `colorNames.txt` file. (Only edit text after '=')

```
None=🫥 None
red=🚨 Red
orange=🦊 Orange
brown=🪵 Brown
yellow=🌼 Yellow
lightGreen=🍀 Light green
darkGreen=🫑 Dark green
lightBlue=💎 Light blue
darkBlue=🌀 Dark blue
purple=🔮 Purple
magenta=🌺 Magenta
lightGray=🏐 Light Gray
charcoal=🎱 Charcoal
```

By default, if there is no colorNames.txt, it will create a file stored in either `~/Library/Application Support/Glyphs 3/info`

<br>

# Advance Report
At each new report generated, if Color Labels data changed, you will see for each masters a new section `Detailed report`   
This section lists all the glyphs whose colour label has been changed.

<img alt="Font Dashboard screenshot" src="https://user-images.githubusercontent.com/76793951/210559895-78471cba-3545-426e-9bea-5de4f3366315.png">
