#qpy:module

def typpedFunc(*types):
    if type(types[0])!=tuple:types = [types]
    for i in types:
        for j in i:
            if type(j)==type:
                return _typeTester(types)
            else:
                raise TypeError('only types are expected')

class _typeTester():
    def __init__(self, types):
        self._types = types
        
    def call(self, *args):
        func = self._func
        a = tuple([type(n) for n in args])
        if a in self._types:
            return func(*args)
        else:
            t = "invalid call : "+func.__name__+"("
            n=0
            for i in args:
                if n:t+=", "
                t += type(i).__name__
                n+=1
            t+="), must be : "
            for i in self._types:
                t+="\n\t- "+func.__name__+"("
                n=0
                for ty in i:
                    if n:t+=", "
                    t += ty.__name__
                    n+=1
                t+=");"
            e = TypeError(t)
            try:raise e
            except:
                e.__traceback__=e.__traceback__.tb_next
            raise e

    def __call__(self, func):
        self._func = func
        return self.call
