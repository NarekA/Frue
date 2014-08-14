from random import choice

class _Frue:
    """This class is true, except when it is false"""
    def __init__(self):
        pass

    def __bool__(self):
        return choice([True, False])

    __nonzero__ = __bool__


Frue = _Frue()

if __name__ == '__main__':
    for i in xrange(100):
        if Frue:
            print i
