#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


class C:
    """doc"""

    data = 'the class data'

    def __init__(self, instanceData):
        self.instanceData = instanceData

    def f(self):
        return 'the func data'

    @property
    def prop(self):
        return 'the property data'


if __name__ == "__main__":
    c = C("instanceData")
    print(C.__dict__)
    print(c.__dict__)  # vars(c)

    print(C.prop)
    print(c.prop)
    try:
        c.prop = 'foo'
    except AttributeError:
        print('AttributeError')
    c.__dict__['prop'] = 'foo'
    print(vars(c))
    print(c.prop)
    C.prop = 'baz'
    print(c.prop)

    print(c.data)
    print(C.data)
    C.data = property(lambda self: 'the "data" prop value')
    print(c.data)
    del C.data
    try:
        print(c.data)
    except AttributeError:
        print('AttributeError')
