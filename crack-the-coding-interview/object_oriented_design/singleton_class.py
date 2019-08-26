

class Singleton(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if Singleton.__instance is None:
            Singleton.__instance = object.__new__(cls, *args, **kwargs)
        else:
            return Singleton.__instance





if __name__ == "__main__":
    a = Singleton()
    print id(a)
    b = Singleton()
    print id(b)