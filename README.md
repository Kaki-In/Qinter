# Qinter
An alternative module to fullscreenwrapper2app for QPython OS/OL. 

## The UI

To import the ui of Qinter, simply do : 
``` python
from Qinter import *
```

---

Then you'll have to define a Layout, the support of your application : 

``` python
class MainLayout(Layout):
    def __init__(self):
        super().__init__()
        self.initUI()
        ... # write what you need for your app
    
    def initUI(self):
        ... # here is the place where you'll define your views. 
        # There is no way to parse a file for the moment

    def onShow(self):
        ...
        # There, you'll have to add the events handlers (button clicks, Back key, etc...) or start threads
        # And do others thing you want
    
    def onClose(self):
        ...
        # There, you'll have to put what to do when closing the application (close connections, ...)
    
```

Note that you can also remove the `onShow` and `onClose` methods, that by default don't do anything.

---
When creating a layout, you need to use views. 
Here is the list of the different views :

#### Containers (can contain multiple views) :
 - Relative Layout
 - Linear Layout

#### Lists (can contain multiple items) :
 - ListView

#### Dsiplayers (can contain only one single view) :
 - ScrollView
 - HorizontalScrollView

#### Others (interactive views, or just shapes):
 - TextView
 - EditText
 - Button
 - SimpleView (the equivalent of a View, the name has been changed for generical reasons)
 - NumberPicker
 - SeekBar
 - RadioGroup
 - RadioButton
 - ImageView
 - ImageButton

---


To define a view, simply do it using his name : 

``` python
a = TextView(id="textId", gravity=View.TOP_LEFT, ...)
```

All the constants are defined into the `View` class : 

- FILL_PARENT
- MATCH_PARENT
- WRAP_CONTENT
- VISIBLE
- INVISIBLE
- HORIZONTAL
- VERTICAL
- CENTER
- CENTER_VERTICAL
- RIGHT
- LEFT
- TOP
- BOTTOM
- TOP_LEFT
- TOP_RIGHT
- BOTTOM_LEFT
- BOTTOM_RIGHT

Note that you can also modify the properties of the view that don't have any id.

If we consider that `v` is a view that doesn't have any id : 
``` python
v.setVisibility(View.INVISIBLE)
```

will still work.

### The Layout class : 



## The control

## The musics

## The threads

## Examples


