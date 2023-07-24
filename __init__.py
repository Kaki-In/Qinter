#-*-coding:utf8;-*-
	
import fsw2modif as _fsw2
from androidhelper import Android as _Android
import random
import os

_fsw2.FullScreenWrapper2App.initialize(_Android())

class TagNames:
    LINEAR_LAYOUT          = 0
    TEXT_VIEW              = 1
    EDIT_TEXT              = 2
    BUTTON                 = 3
    SCROLL_VIEW            = 4
    HORIZONTAL_SCROLL_VIEW = 5
    LIST_VIEW              = 6
    VIEW                   = 7
    RELATIVE_LAYOUT        = 8
    NUMBER_PICKER          = 9
    RADIO_GROUP            = 10
    RADIO_BUTTON           = 11
    SEEK_BAR               = 12
    IMAGE_VIEW             = 13
    IMAGE_BUTTON           = 14

class _xmlScreen(_fsw2.Layout):
    def __init__(self, xml, parent):
        super().__init__(xml, "QSL4AUI")
        self.parent = parent

    def on_show(self):
        self.parent._on_show()

    def on_close(self):
        self.parent._on_close()

class Layout():
    def __init__(self, view=None):
        super().__init__()
        self._view = view

    def setView(self, view):
        self._view = view

    def getView(self):
        return self._view

    def show(self, keep = False):
        if self._view != None:
            a = """<?xml version="1.0" encoding="utf-8"?>
<LinearLayout
    android:layout_width="fill_parent"
    android:layout_height="fill_parent"
    android:background="#0000"
    xmlns:android="http://schemas.android.com/apk/res/android">"""
            a += " " + str( self._view ).replace("\n", "\n ")
            a += "\n</LinearLayout>"
            screen = _xmlScreen(a, self)
            self._screen = screen
            _fsw2.FullScreenWrapper2App.show_layout(screen, 0 if keep else 1)

    def _on_show(self):
        self._view._load_xmlConfig(self._screen.views)
        self.onShow()
    
    def onShow(self):
        pass

    def _on_close(self):
        self.onClose()
    
    def onClose(self):
        pass

    def findViewById(self, id):
        return self._view.findViewById(id)
    
    def addKeyEvent(self, key, func):
        self._screen.add_event(_fsw2.key_EventHandler(key, self._screen, func))
        
    def addDelay(self, timeout, func):
        self._screen.add_delay(_fsw2.DelayHandler(timeout, func))
    
    def main(self):
        _fsw2.FullScreenWrapper2App.eventloop()
    
    def close(self):
        _fsw2.FullScreenWrapper2App.close_layout()
     
    def getFullScreenWrapper2AppLayout(self):
        return self._screen
    
class _Orientable():
    def setOrientation(self, orient):
        self._args["orientation"] = orient
        try:
            self._view.orientation = orient
        except:
            pass

    def getOrientation(self):
        return self._args["orientation"]

class _Colored():
    def setTextColor(self, color):
        self._args["textColor"] = color
        try:
            self._view.textColor = color
        except:
            pass

    def getTextColor(self):
        return self._args["textColor"]

class _Textable(_Colored):
    def setText(self, text):
        self._args["text"] = text
        try:
            self._view.text = text
        except:
            pass

    def getText(self):
        try:
            return self._view["text"]
        except:
            return self._args["text"]

    def setTextSize(self, size):
        self._args["textSize"] = size
        try:
            self._view.textSize=size
        except:
            pass

    def getTextSize(self):
        try:
            return self._view["textSize"]
        except:
            return self._args["textSize"]

class _Modifiable(_Textable):
    def setInputType(self, t):
        self._args["inputType"] = t
        try:
            self._view.inputType = t
        except:
            pass

    def getInputType(self):
        return self._args["inputType"]

    def setHint(self, h):
        self._args["hint"] = h
        try:
            self._view.hint = h
        except:
            pass

    def getHint(self):
        return self._args["hint"]

    def _onclick(self, view, key):
        if hasattr(self, '_funcs'):
            self._funcs[key](self, key)

    def setOnKey(self, key, func):
        if not hasattr(self, '_funcs'):
            self._funcs = {}
        self._funcs.update( {key: func} )
        self._view.add_event(_fsw2.key_EventHandler(key, self._view, lambda self, view, k=key:self._onclick(view, k)))
        
class _Clickable():
    def _onclick(self, view, dummy):
        self._func(self, dummy)

    def setOnClickListener(self, func):
        self._func=func
        self._view.add_event(_fsw2.click_EventHandler(self._view, self._onclick))

class _itemClickable():
    def _onclick(self, view, dummy):
        if hasattr(self, '_func'):
            self._func(self, dummy)

    def setOnItemClickListener(self, func):
        self._func=func
        self._view.add_event(_fsw2.itemclick_EventHandler(self._view, self._onclick))

class _Valueable():
    def setValue(self, value):
        self._args["value"] = value
        try:
            self._view.value = value
        except:
            pass

    def getValue(self):
        try:
            return self._view["value"]
        except:
            return self._args["value"]

    def setMinValue(self, value):
        self._args["min"] = value
        self._args["minValue"] = value
        try:
            self._view.min = value
            self._view.minValue = value
        except:
            pass

    def getMinValue(self):
        try:
            return self._view["min"] or self._view["minValue"]
        except:
            return self._args["min"]

    def setMaxValue(self, value):
        self._args["max"]=value
        self._args["maxValue"]=value
        try:
            self._view.max=value
            self._view.maxValue=value
        except:
            pass

    def getMaxValue(self):
        try:
            return self._view["max"] or self._view["maxValue"]
        except:
            return self._args["max"]

class _Checkable():
    def setChecked(self, checked):
        self._args["checked"] = checked
        try:
            self._view.checked = checked
        except:
            pass

    def getChecked(self):
        try:
            return self._view["checked"]
        except:
            return self._args["checked"]

class _Sourced():
    def setSource(self, source):
        self._args["src"] = source
        try:
            self._view.src = source
        except:
            pass

    def getSource(self):
        return self._args["src"]

def getSymbolName(symbol):
    if type(symbol) is int:
        return ['fill_parent', 
                'match_parent', 
                'wrap_content', 
                'visible', 
                'invisible', 
                'horizontal', 
                'vertical',
                'center',
                'center-vertical',
                'right', 
                'left', 
                'top', 
                'bottom', 
                'top|left', 
                'top|right', 
                'bottom|left'
                'bottom|right',
                'date',
                'datetime',
                'none',
                'number',
                'numberDecimal',
                'numberPassword',
                'numberSigned',
                'phone',
                'text',
                'textAutoComplete',
                'textAutoCorrect',
                'textCapCharacters',
                'textCapSentences',
                'textCapWords',
                'textEmailAddress',
                'textEmailSubject',
                'textEnableTextConversionSuggestions',
                'textFilter',
                'textImeMultiLine',
                'textLongMessage',
                'textMultiLine',
                'textNoSuggestions',
                'textPassword',
                'textPersonName',
                'textPhonetic',
                'textPostalAddress',
                'textShortMessage',
                'textUri',
                'textVisiblePassword',
                'textWebEditText',
                'textWebEmailAddress',
                'textWebPassword',
                'time'][symbol]

    elif type(symbol) is bool:
        return "true" if symbol else "false"
        
    elif type(symbol) is list:
        a = ""
        for i in symbol:
            if a: 
                a += "|"
            a += getSymbolName(i)
        return a

    return symbol

def _getRandomString(length):
    a = ''
    for i in range(length):
        a += random.choice([random.choice([chr(i+0x41) for i in range(26)]), random.choice([chr(i+0x61) for i in range(26)])])
    return a

class View():
    FILL_PARENT                                   = 0
    MATCH_PARENT                                  = 1
    WRAP_CONTENT                                  = 2
    VISIBLE                                       = 3
    INVISIBLE                                     = 4
    HORIZONTAL                                    = 5
    VERTICAL                                      = 6
    CENTER                                        = 7
    CENTER_VERTICAL                               = 8
    RIGHT                                         = 9
    LEFT                                          = 10
    TOP                                           = 11
    BOTTOM                                        = 12
    TOP_LEFT                                      = 13
    TOP_RIGHT                                     = 14
    BOTTOM_LEFT                                   = 15
    BOTTOM_RIGHT                                  = 16
    
    INPUT_DATE                                    = 17
    INPUT_DATETIME                                = 18
    INPUT_NONE                                    = 19
    INPUT_NUMBER                                  = 20
    INPUT_NUMBER_DECIMAL                          = 21
    INPUT_NUMBER_PASSWORD                         = 22
    INPUT_NUMBER_SIGNED                           = 23
    INPUT_PHONE                                   = 24
    INPUT_TEXT                                    = 25
    INPUT_TEXT_AUTO_COMPLETE                      = 26
    INPUT_TEXT_AUTO_CORRECT                       = 27
    INPUT_TEXT_CAP_CHARACTERS                     = 28
    INPUT_TEXT_CAP_SENTENCES                      = 29
    INPUT_TEXT_CAP_WORDS                          = 30
    INPUT_TEXT_EMAIL_ADDRESS                      = 31
    INPUT_TEXT_EMAIL_SUBJECT                      = 32
    INPUT_TEXT_ENABLE_TEXT_CONVERSION_SUGGESTIONS = 33
    INPUT_TEXT_FILTER                             = 34
    INPUT_TEXT_IME_MULTI_LINE                     = 35
    INPUT_TEXT_LONG_MESSAGE                       = 36
    INPUT_TEXT_MULTI_LINE                         = 37
    INPUT_TEXT_NO_SUGGESTIONS                     = 38
    INPUT_TEXT_PASSWORD                           = 39
    INPUT_TEXT_PERSON_NAME                        = 40
    INPUT_TEXT_PHONETIC                           = 41
    INPUT_TEXT_POSTAL_ADDRESS                     = 42
    INPUT_TEXT_SHORT_MESSAGE                      = 43
    INPUT_TEXT_URI                                = 44
    INPUT_TEXT_VISIBLE_PASSWORD                   = 45
    INPUT_TEXT_WEB_EDIT_TEXT                      = 46
    INPUT_TEXT_WEB_EMAIL_ADDRESS                  = 47
    INPUT_TEXT_WEB_PASSWORD                       = 48
    INPUT_TIME                                    = 49


    def __init__(self, tagName=TagNames.VIEW, id=None, **args):
        self._type = tagName
        self._args = {}
        self._id = id
        self._main_id = _getRandomString(16)
        for i in _expected:
            self._args[i] = _expected[i][1]
            if _expected[i][1] is Exception and not i in _args:
                raise ValueError("'" + i + "' is required")
        for i in args:
            if not i in _expected:
                raise ValueError("cannot find symbol '" + str(i) + "'")
            if type(args[i]) is int:
                if not args[i] in _expected[i][0]:
                    raise TypeError("invalid argument for " + str(i))
            elif not type(args[i]) in _expected[i][0]:
                raise TypeError("invalid argument for " + str(i))
            elif type(args[i]) is list:
                for k in args[i]:
                    if type(k) is int:
                        if not k in _expected[i][0]:
                            raise TypeError("invalid argument for " + str(i))
                    elif not type(k) in _expected[i][0]:
                        raise TypeError("invalid argument for " + str(i))
        self._args.update(args)
        self._args['id'] = "@id/"+self._main_id
        self._view = None

    def setLayoutWidth(self, lw):
        self._args["layout_width"] = lw
        try:
            self._view.layout_width = lw
        except:
            pass

    def getLayoutWidth(self):
        return self._args["layout_width"]

    def setLayoutHeight(self, lh):
        self._args["layout_height"] = lh
        try:
            self._view.layout_height = lh
        except:
            pass

    def getLayoutHeight(self):
        return self._args["layout_height"]

    def setLayoutWeight(self, lw):
        self._args["layout_weight"] = lw
        try:
            self._view.layout_weight = lw
        except:
            pass

    def getLayoutWeight(self):
        return self._args["layout_weight"]

    def setLayoutGravity(self, lg):
        self._args["layout_gravity"] = lg
        try:
            self._view.layout_gravity = lg
        except:
            pass

    def getLayoutGravity(self):
        return self._args["layout_gravity"]

    def setBackground(self, back):
        self._args["background"] = back
        try:
            self._view.background = back
        except:
            pass

    def getBackground(self):
        return self._args["background"]

    def setVisibility(self, lv):
        self._args["visibility"] = lv
        try:
            self._view.visibility = lv
        except:
            pass

    def getVisibility(self):
        return self._args["visibility"]

    def setId(self, id):
        self._id=id

    def getId(self):
        return self._id

    def getTagName(self):
        for i in dir(TagNames):
            return ["LinearLayout", "TextView", "EditText", "Button", "ScrollView", "HorizontalScrollView", "ListView", "View", "RelativeLayout", "NumberPicker", "RadioGroup", "RadioButton", "SeekBar", "ImageView", "ImageButton"][self._type]

    def _load_xmlConfig(self, views):
        self._view=views[self._main_id]

    def setAlignParentTop(self, alp):
        self._args['layout_alignParentTop'] = alp
        try:
            self._view.layout_alignParentTop = alp
        except:
            pass

    def getAlignParentTop(self):
        return self._args['layout_alignParentTop']

    def setAlignParentBottom(self, alb):
        self._args['layout_alignParentBottom'] = alb
        try:
            self._view.layout_alignParentBottom = alb
        except:
            pass

    def getAlignParentBottom(self):
        return self._args['layout_alignParentBottom']

    def setAlignParentRight(self, alr):
        self._args['layout_alignParentRight'] = alr
        try:
            self._view.layout_alignParentRight = alr
        except:
            pass

    def getAlignParentRight(self):
        return self._args['layout_alignParentRight']

    def setAlignParentLeft(self, all):
        self._args['layout_alignParentLeft'] = all
        try:
            self._view.layout_alignParentLeft = all
        except:
            pass

    def getAlignParentLeft(self):
        return self._args['layout_alignParentLeft']

    def setCenterInParent(self, cip):
        self._args['layout_centerInParent'] = cip
        try:
            self._view.layout_centerInParent = cip
        except:
            pass

    def getCenterInParent(self):
        return self._args['layout_centerInParent']

    def setRotation(self, r):
        self._args['rotation'] = r
        try:
            self._view.rotation = r
        except:
            pass

    def getRotation(self):
        return self._args['rotation']

    def findViewById(self, id):
        if self.getId() == id:
            return self

    def __str__(self):
        a = "<" + self.getTagName()
        for i in _expected:
            if self._args[i] != _expected[i][1]:
                a += "\n android:" + str(i) + "=" + repr(str(getSymbolName(self._args[i])))
        a += "/>"
        return a

    def __repr__(self):
        return "<" + self.getTagName() + "/>"

class _listed(View):
    def __init__(self, tagName, **args):
        super().__init__(tagName, **args)
        self._list = []

    def setList(self, liste):
        try:
            self._view.set_listitems(list(liste))
        except:
            pass
        self._list = list(liste)

    def getList(self):
        return self._list

    def _load_xmlConfig(self, views):
        super()._load_xmlConfig(views)
        self.setList(self.getList())

class _containerView(View):
    def __init__(self, tagName, **args):
        super().__init__(tagName, **args)
        self._views = []

    def addView(self, view):
        self._views.append(view)

    def removeView(self, view):
        self._views.remove(view)

    def _load_xmlConfig(self, views):
        self._view=views[self._main_id]
        for i in self._views:
            i._load_xmlConfig(views)

    def findViewById(self, id):
        if self.getId() == id:
            return self

        for i in self._views:
            j = i.findViewById(id)
            if j is not None:
                return j

    def __str__(self):
        a = "<" + self.getTagName()
        for i in _expected:
            if self._args[i] != _expected[i][1]:
                a += "\n android:" + str(i) + "=" + repr(str(getSymbolName(self._args[i])))

        if self._views:
            a += ">\n"
            for i in self._views:
                b = str(i)
                a += " " + b.replace("\n", "\n ") + "\n"
            a += "</" + self.getTagName() + ">"
        else:
            a += "/>"
        return a

class _displayerView(View):
    def __init__(self, tagName, **args):
        super().__init__(tagName, **args)
        self._mainview=None

    def setView(self, view):
        self._mainview = view

    def removeView(self):
        self._mainview = None

    def _load_xmlConfig(self, views):
        self._view = views[self._main_id]
        self._mainview._load_xmlConfig(views)

    def findViewById(self, id):
        if self.getId() == id:
            return self
        j = self._mainview.findViewById(id)
        if j is not None:
            return j

    def __str__(self):
        a = "<" + self.getTagName()
        for i in _expected:
            if self._args[i] != _expected[i][1]:
                a += "\n android:" + str(i) + "=" + repr(str(getSymbolName(self._args[i])))
        if not self._mainview is None:
            a += ">\n"
            b = str(self._mainview)
            a += " " + b.replace("\n", "\n ") + "\n"
            a += "</" + self.getTagName() + ">"
        else:
            a += "/>"
        return a

class TextView(View, _Textable):
    def __init__(self, **args):
        super().__init__(TagNames.TEXT_VIEW, **args)

class LinearLayout(_containerView, _Orientable):
    def __init__(self, **args):
        super().__init__(TagNames.LINEAR_LAYOUT, **args)

class EditText(View, _Modifiable, _Clickable):
    def __init__(self, **args):
        super().__init__(TagNames.EDIT_TEXT, **args)

class Button(View, _Textable, _Clickable):
    def __init__(self, **args):
        super().__init__(TagNames.BUTTON, **args)

class ScrollView(_displayerView, _Orientable):
    def __init__(self, **args):
        super().__init__(TagNames.SCROLL_VIEW, **args)

class HorizontalScrollView(_displayerView, _Orientable):
    def __init__(self, **args):
        super().__init__(TagNames.HORIZONTAL_SCROLL_VIEW, **args)

class ListView(_itemClickable, _listed):
    def __init__(self, **args):
        super().__init__(TagNames.LIST_VIEW, **args)

class RelativeLayout(_containerView):
    def __init__(self, **args):
        super().__init__(TagNames.RELATIVE_LAYOUT, **args)

class NumberPicker(View, _Valueable):
    def __init__(self, **args):
        super().__init__(TagNames.NUMBER_PICKER, **args)

class SeekBar(View, _Valueable, _itemClickable, _Orientable):
    def __init__(self, **args):
        super().__init__(TagNames.SEEK_BAR, **args)

class RadioGroup(_containerView):
    def __init__(self, **args):
        super().__init__(TagNames.RADIO_GROUP, **args)

class RadioButton(View, _Checkable):
    def __init__(self, **args):
        super().__init__(TagNames.RADIO_BUTTON, **args)

class ImageView(View, _Sourced):
    def __init__(self, **args):
        super().__init__(TagNames.IMAGE_VIEW, **args)

class ImageButton(View, _Sourced, _Clickable):
    def __init__(self, **args):
        super().__init__(TagNames.IMAGE_BUTTON, **args)

class CustomView(View):
    def __init__(self, **args):
        super().__init__(**args)
    
    def set(self, param, value):
        self._args[param] = value
        try:
            self._view[param] = value
        except:
            pass
    
    def get(self, param):
        try:
            return self._view[param], self._args[param]
        except:
            return None, self._args[param]

class Color():
    BLACK               = 0
    BLUE                = 0xff
    BROWN               = 0x880000
    CYAN                = 0xffff
    DARKBLUE            = 0x88
    DARKGREY            = 0x444444
    GREEN               = 0x8800
    GREY                = 0x888888
    LIGHTGREEN          = 0x00ff00
    LIGHTGREY           = 0xcccccc
    MAGENTA             = 0xff00ff
    MICROPORTAL         = 0x12b7ff
    NUMWORKS            = 0xf8b430
    ORANGE              = 0xff8800
    RED                 = 0xff0000
    WHITE               = 0xffffff
    YELLOW              = 0xffff00
    TRANSPARENT         = 0
    LIGHT_TRANSPARENT   = 0x44000000
    MEDIUM_TRANSPARENT  = 0x88000000
    LIGHT_OPAC          = 0xcc000000
    OPAC                = 0xff000000
    
    def __init__(self, col):
    	self._color = col

    def parseString(string):
        return Color(int(string[1:], 16))

    def fromARGB(argb):
        a = Color(0)
        a.setARGB(argb)
        return a

    def getColor(self):
        return self._color

    def setColor(self, col):
        self._color = col

    def getARGB(self):
        return tuple([self._color//0x1000000, (self._color//0x10000)%0x100, (self._color//0x100)%0x100, self._color%0x100])

    def setARGB(self, argb):
        self._color = sum([argb[i]*(0x100**(3-i)) for i in range(4)])

    def __str__(self):
        a = "#"
        for i in range(8):
            a += "0123456789ABCDEF"[(self._color//(16**(7-i)))%16]
        return a

    def __repr__(self):
        return "Color(" + hex(self._color) + ")"

class Size():
    UNIT_DP = 0
    UNIT_PX = 1
    
    def __init__(self, size, unit):
        self._size = [size, unit]

    def setSize(self, size):
        self._size[0] = size

    def getSize(self):
        return self._size[0]

    def setUnit(self, unit):
        self._size[1] = unit

    def getUnit(self):
        return self._size[1]

    def __str__(self):
        return str(self._size[0]) + ["dp", "px"][self._size[1]]

    def __repr__(self):
        return "Size(" + str(self._size[0]) + ", Size."+["UNIT_DP", "UNIT_PX"][self._size[1]]

class Value():
    def __init__(self, value):
        self._value = value

    def getValue(self):
        return self._value

    def setValue(self, value):
        self._value = value

    def __str__(self):
        return str(self._value)

class Path():
    def __init__(self, path):
        self.verify(path)
        self._path = path

    def verify(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError("couldn't find path for " + path)

    def setPath(self, path):
        self.verify(path)
        self._path = path

    getPath = lambda self: self._path

    def __str__(self):
        return "file://" + self._path

    def __repr__(self):
        return "Path(" + repr(self._path) + ")"

_expected={
	 "layout_width":[[View.FILL_PARENT, View.MATCH_PARENT, View.WRAP_CONTENT, Size], Size(0, Size.UNIT_DP)],
	 "layout_height":[[View.FILL_PARENT, View.MATCH_PARENT, View.WRAP_CONTENT, Size], Size(0, Size.UNIT_DP)],
	 "layout_weight":[[Value], Value(0)],
	 "layout_gravity":[[View.CENTER, View.CENTER_VERTICAL, View.RIGHT, View.LEFT, View.TOP, View.BOTTOM, View.TOP_LEFT, View.TOP_RIGHT, View.BOTTOM_LEFT, View.BOTTOM_RIGHT], View.TOP_LEFT],
	 "visibility":[[View.VISIBLE, View.INVISIBLE], View.VISIBLE],
	 "orientation":[[View.VERTICAL, View.HORIZONTAL], None],
	 "text":[[str], ""],
	 "textColor":[[Color], Color(Color.GREY+Color.MEDIUM_TRANSPARENT)],
	 "background":[[Color], Color(Color.TRANSPARENT)],
	 "layout_alignParentTop":[[bool], False],
	 "layout_alignParentBottom":[[bool], False],
	 "layout_alignParentLeft":[[bool], False],
	 "layout_alignParentRight":[[bool], False],
	 "layout_centerInParent":[[bool], False],
	 "textSize":[[Size], Size(16, Size.UNIT_DP)],
	 "inputType":[[list, View.INPUT_DATE, View.INPUT_DATETIME, View.INPUT_NONE, View.INPUT_NUMBER, View.INPUT_NUMBER_DECIMAL, View.INPUT_NUMBER_PASSWORD, View.INPUT_NUMBER_SIGNED, View.INPUT_PHONE, View.INPUT_TEXT, View.INPUT_TEXT_AUTO_COMPLETE, View.INPUT_TEXT_AUTO_CORRECT, View.INPUT_TEXT_CAP_CHARACTERS, View.INPUT_TEXT_CAP_SENTENCES, View.INPUT_TEXT_CAP_WORDS, View.INPUT_TEXT_EMAIL_ADDRESS, View.INPUT_TEXT_EMAIL_SUBJECT, View.INPUT_TEXT_ENABLE_TEXT_CONVERSION_SUGGESTIONS, View.INPUT_TEXT_FILTER, View.INPUT_TEXT_IME_MULTI_LINE, View.INPUT_TEXT_LONG_MESSAGE, View.INPUT_TEXT_MULTI_LINE, View.INPUT_TEXT_NO_SUGGESTIONS, View.INPUT_TEXT_PASSWORD, View.INPUT_TEXT_PERSON_NAME, View.INPUT_TEXT_PHONETIC, View.INPUT_TEXT_POSTAL_ADDRESS, View.INPUT_TEXT_SHORT_MESSAGE, View.INPUT_TEXT_URI, View.INPUT_TEXT_VISIBLE_PASSWORD, View.INPUT_TEXT_WEB_EDIT_TEXT, View.INPUT_TEXT_WEB_EMAIL_ADDRESS, View.INPUT_TEXT_WEB_PASSWORD, View.INPUT_TIME], View.INPUT_TEXT],
	 "hint":[[str], ""],
	 "gravity":[[View.CENTER, View.CENTER_VERTICAL, View.RIGHT, View.LEFT, View.TOP, View.BOTTOM, View.TOP_LEFT, View.TOP_RIGHT, View.BOTTOM_LEFT, View.BOTTOM_RIGHT], View.TOP_LEFT],
	 "padding":[[Size], Size(0, Size.UNIT_DP)],
	 "paddingTop":[[Size], Size(0, Size.UNIT_DP)],
	 "paddingBottom":[[Size], Size(0, Size.UNIT_DP)],
	 "paddingRight":[[Size], Size(0, Size.UNIT_DP)],
	 "paddingLeft":[[Size], Size(0, Size.UNIT_DP)],
	 "margin":[[Size], Size(0, Size.UNIT_DP)],
	 "marginTop":[[Size], Size(0, Size.UNIT_DP)],
	 "marginBottom":[[Size], Size(0, Size.UNIT_DP)],
	 "marginRight":[[Size], Size(0, Size.UNIT_DP)],
	 "marginLeft":[[Size], Size(0, Size.UNIT_DP)],
	 "value":[[Value], Value(0)],
	 "min":[[Value], Value(0)], 
	 "max":[[Value], Value(0)], 
	 "minValue":[[Value], Value(0)], 
	 "maxValue":[[Value], Value(0)], 
	 "checked":[[bool], False],
	 "rotation":[[Value], Value(0)],
	 "id":[[], None],
	 "src":[[Path], None]
}

class _ressource():
    def __init__(self, typeof):
        self._vals = {}
        self._type = typeof

    def __setattr__(self, attr, val):
        if attr in ['_vals', '_type']:
            return object.__setattr__(self, attr, val)
        if type(val) is self._type:
            self._vals[attr] = val
        else:
            raise TypeError("a {} is required, not a {}".format(self._type.__name__, type(val).__name__))

    def __getattr__(self, attr):
        if attr in ['_vals', '_type']:
            return {'_vals':object.__getattribute__(self, '_vals'), '_type':object.__getattribute__(self, '_type')}[attr]

        return self._vals[attr]

    def __dir__(self):
        return list(self._vals)

    def __repr__(self):
        return "<ressource({})>".format(self._type.__name__)

    def __str__(self):
        return "<ressource({})>".format(self._type.__name__)
        
class R:
    string = _ressource(str)
    color = _ressource(Color)
    dimen = _ressource(Size)
    integer = _ressource(int)
    bool = _ressource(bool)
    src = _ressource(Path)
