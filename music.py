from androidhelper import Android
from Qinter.thread import Thread
import random
import time
import os

_musicInstances = {}

_droid = Android()

class PlayError(Exception):
    pass

def _getRandomString(length):
    a = ''
    for i in range(length):
        a+=random.choice([random.choice([chr(i+0x41) for i in range(26)]), random.choice([chr(i+0x61) for i in range(26)])])
    return a

def forceDestroyMusics():
    for i in _droid.mediaPlayList().result:
        _droid.mediaPlayClose(i)

def getMusicsList():
    return list(_musicInstances)

class Loop():
    def __init__(self, start=None, end=None):
        self._start = start
        self._end = end
    
    def end(self):
        return self._end
    
    def start(self):
        return self._start
    
    def setEnd(self, end):
        self._end = end
    
    def setStart(self, start):
        self._start = start

class _musicThread(Thread):
    def __init__(self, music):
        self._music = music
        
    def run(self):
        while self.canBeRunning() and self._music.isPlaying():
            if self._music.loop().end() <= self._music.position():
                self._music.setPosition(self._music.loop().start())
            time.sleep(max([0, min([1, (self._music.loop().end()-self._music.position())/2000])]))

class Music():
    def __init__(self, path=None):
        self._path=path
        if not os.path.exists(path):raise FileNotFoundError("file {} has not been find".format(repr(path)))
        self._musicId=_getRandomString(8)
        while self._musicId in _musicInstances:
            self._musicId=_getRandomString(8)
        _musicInstances.update({self._musicId:self})
        self._loop=None

    def setLoop(self, *loop):
        if len(loop)==1:
            self._loop=loop[0]
        else:
            self._loop=Loop(*loop)
        
    def removeLoop(self):
        self._loop=False
        
    def loop(self):
        return self._loop
    
    def play(self):
        a = _droid.mediaPlay(self._path, self._musicId)
        if not a:
            raise PlayError("could not start the music")
        if type(self._loop)==Loop:
            self._mainLoop()
    
    def _mainLoop(self):
        _musicThread(self).start()
    
    def position(self):
        try:
            return _droid.mediaPlayInfo(self._musicId).result['position']
        except:
            return 0
    
    def setPosition(self, pos):
        _droid.mediaPlaySeek(pos, self._musicId)
    
    def pause(self):
        _droid.mediaPlayPause(self._musicId)
    
    def stop(self):
        _droid.mediaPlayClose(self._musicId)
    
    def isPlaying(self):
        return _droid.mediaIsPlaying(self._musicId).result

    def getLength(self):
        return _droid.mediaPlayInfo(self._musicId).result['duration']
