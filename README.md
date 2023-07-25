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
            # You can also parse a string containing your data, but note that it will generate only CustomViews (see Parsing strings section)

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
 - View
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

You can also use the CustomView, that inherits from all kind of views.

``` python
a = CustomView("TextView", id="textId", gravity=View.TOP_LEFT, ...)
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
- INPUT_DATE
- INPUT_DATETIME
- INPUT_NONE
- INPUT_NUMBER
- INPUT_NUMBER_DECIMAL
- INPUT_NUMBER_PASSWORD
- INPUT_NUMBER_SIGNED
- INPUT_PHONE
- INPUT_TEXT
- INPUT_TEXT_AUTO_COMPLETE
- INPUT_TEXT_AUTO_CORRECT
- INPUT_TEXT_CAP_CHARACTERS
- INPUT_TEXT_CAP_SENTENCES
- INPUT_TEXT_CAP_WORDS
- INPUT_TEXT_EMAIL_ADDRESS
- INPUT_TEXT_EMAIL_SUBJECT
- INPUT_TEXT_ENABLE_TEXT_CONVERSION_SUGGESTIONS
- INPUT_TEXT_FILTER
- INPUT_TEXT_IME_MULTI_LINE
- INPUT_TEXT_LONG_MESSAGE
- INPUT_TEXT_MULTI_LINE
- INPUT_TEXT_NO_SUGGESTIONS
- INPUT_TEXT_PASSWORD
- INPUT_TEXT_PERSON_NAME
- INPUT_TEXT_PHONETIC
- INPUT_TEXT_POSTAL_ADDRESS
- INPUT_TEXT_SHORT_MESSAGE
- INPUT_TEXT_URI
- INPUT_TEXT_VISIBLE_PASSWORD
- INPUT_TEXT_WEB_EDIT_TEXT
- INPUT_TEXT_WEB_EMAIL_ADDRESS
- INPUT_TEXT_WEB_PASSWORD
- INPUT_TIME


Note that you can also modify the properties of the view that don't have any id.

If we consider that `v` is a view that doesn't have any id : 
``` python
v.setVisibility(View.INVISIBLE)
```

will still work.

### The Layout class : 



## Parsing a string

You can also parse a string by this way :
```python
from Qinter.parser import parse
from Qinter import *

...
R.dimen.buttonExplode = Size(16,Size.UNIT_DP)
...

string = """
<LinearLayout
    android:layout_width="fill_parent"
    android:layout_height=View.MATCH_PARENT
    orientation="vertical"
    qinter:id="base layout"
    android:background=Color(Color.OPAC + Color.FLOPCREATION)>
    <TextView
        layout_width=View.FILL_PARENT
        layout_height="0dp"
        layout_weight=Value( 3 )
        qinter:id="mainTextView"
        text="ATTENTION !"
        textSize=Size(16, Size.UNIT_DP)
        textColor="#ffff0000"/>
    <Button
        layout_width=View.FILL_PARENT
        layout_height="0dp"
        layout_weight=Value( 1 )
        text="Exploser"
        textSize=R.dimen.buttonExplode
        textColor="#ffff0000"/>
</LinearLayout>
"""

element = parse(string)

```

It is better to use instanced values (`Size(16,Size.UNIT_DP)`) for the values that are susceptibles to be changed and the strings (`"#ffff0000"`) for those that will not be modified. You can also use the resources (`R.dimen.buttonExplode`) for the constants import.

Note that you can forget `android:` or `qpython:` in the beginning of the lines, that are there to be able to prase an xml android app, and if you add spaces into the constants (`Size(16, Size.UNIT_DP)` for example), the parse will not fail in the extent that they are into parenthesis (`[`, `{`, or `(`).

You'll then obtain a `LinearLayout` THAT CONTAINS THE `LinearLayout` IN THE STRING.
To get this one, you can use :

```python
lin = element.getViews()[0]
```

or

```python
lin = element.findViewById("base layout")
```

All elements parsed by the parser are in fact `CustomView`s.

## The control

## The musics

## The threads

## Examples


