#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


class Callee:
    def __call__(self, *pargs, **kargs):
        print('Called: ', pargs, kargs)


def exampleCallee():
    """
    >>> from magic_method4 import *
    >>> c = Callee()
    >>> c(1,2,3)
    Called:  (1, 2, 3) {}
    >>> c(1,2,3,x=4,y=5)
    Called:  (1, 2, 3) {'x': 4, 'y': 5}
    """


class Prod:
    def __init__(self, value):
        self.value = value

    def __call__(self, other):
        return self.value * other


def exampleProd():
    """
    >>> from magic_method4 import *
    >>> x = Prod(2)
    >>> x(3)
    6
    >>> x(4)
    8
    """


class Life:
    def __init__(self, name='unkonw'):
        print('Hello', name)
        self.name = name

    def __del__(self):
        print('Goodbye', self.name)


def exampleLife():
    """
    >>> from importlib import reload
    >>> import magic_method4
    >>> reload(magic_method4)
    <module 'magic_method4' from '/Users/Dev/vscode_python/03-class/magic_method4.py'>
    >>> from magic_method4 import *
    >>> brian = Life('Brian')
    Hello Brian
    >>> brian = 'loretta'
    Goodbye Brian
    """


class wrapper:
    def __init__(self, object):
        self.wrapped = object

    def __getattr__(self, attr):
        print('Trace:', attr)
        return getattr(self.wrapped, attr)


def exampleWrapper():
    """
    >>> from magic_method4 import *
    >>> x = wrapper([1,2,3])
    >>> x.append(4)
    Trace: append
    >>> x.wrapped
    [1, 2, 3, 4]
    >>> x = wrapper({"a":1, "b":2})
    >>> x.keys()
    Trace: keys
    dict_keys(['a', 'b'])
    """
