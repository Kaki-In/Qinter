from threading import Thread as _thread
import fsw2modif as _fsw2

class Thread():
    def __init__(self):
        self._canrun = False

    def start(self):
        self._canrun = True
        _thread(target=self._main).start()

    def _main(self):
        try:
            self.run()
        except:
            raise
        finally:
            self.stop()

    def run(self):
        pass

    def canBeRunning(self):
        return self._canrun

    def stop(self):
        self._canrun = False

class Signal():
    def __init__(self):
        self._funcs = []

    def connect(self, func):
        self._funcs.append(func)

    def disconnect(self, func):
        self._funcs.remove(func)

    def emit(self, *args, **kwargs):
        for f in self._funcs:
            _fsw2.FullScreenWrapper2App._layouts[-1].add_delay(_fsw2.DelayHandler(100, lambda a=args, kw=kwargs, func=f:func(*a, **kw)))

class Timer(Thread):
    def __init__(self):
        super().__init__()
        self.signal = Signal()
        self._timeout = -1
        
    def setTimeout(self, t):
        self._timeout = t
    
    def run(self):
        while self.canBeRunning():
            n = monotonic()
            while monotonic()-n > self._timeout and self.canBeRunning():
                sleep(0.1)
            if self.canBeRunning():
                self.signal.emit()
    
    def timeout(self):
        return self._timeout
