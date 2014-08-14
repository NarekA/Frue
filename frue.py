from random import choice

class Frue:
    """This class is true, except when it is false"""
    def __init__(self):
        pass

    def __bool__(self):
        return choice([True, False])

    __nonzero__=__bool__


if __name__ == '__main__':
    frue = Frue()
    for i in xrange(100):
        if frue:
            print i
