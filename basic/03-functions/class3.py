#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


def exampleSelfless():
    """
    >>> class Selfless:
    ...     def __init__(self, data):
    ...             self.data = data
    ...     def selfless(arg1, arg2):
    ...             return arg1 + arg2
    ...     def normal(self, arg1, arg2):
    ...             return self.data + arg1 + arg2
    ... 
    >>> x = Selfless(2)
    >>> x.normal(3,4)
    9
    >>> Selfless.normal(x, 3, 4)
    9
    >>> Selfless.selfless(3, 4)
    7
    >>> x.selfless(3,4)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: selfless() takes 2 positional arguments but 3 were given
    >>> Selfless.normal(3,4)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: normal() missing 1 required positional argument: 'arg2'
    """


class Number:
    def __init__(self, base):
        self.base = base

    def double(self):
        return self.base * 2

    def triple(self):
        return self.base * 3


def exampleNumber():
    """
    >>> from class3 import *
    >>> x = Number(2)
    >>> y = Number(3)
    >>> z = Number(4)
    >>> acts = [x.double, y.double, y.triple, x.triple]
    >>> for act in acts:
    ...     print(act())
    ... 
    4
    6
    9
    6
    >>> bound = x.double
    >>> bound.__self__
    <class3.Number object at 0x10d04f5c0>
    >>> bound.__func__
    <function Number.double at 0x10d03bd08>
    >>> bound.__self__.base
    2
    >>> bound()
    4
    
    
    >>> def square(arg):
    ...     return arg ** 2
    ... 
    >>> class Sum:
    ...     def __init__(self, val):
    ...             self.val = val
    ...     def __call__(self, arg):
    ...             return self.val + arg
    >>> class Product:
    ...     def __init__(self, val):
    ...             self.val = val
    ...     def method(self, arg):
    ...             return self.val + arg
    ... 
    >>> sobj = Sum(2)
    >>> pobj = Product(3)
    >>> actions = [square, sobj, pobj.method]
    >>> for act in actions:
    ...     print(act(5))
    ... 
    25
    7
    8
    >>> [act(5) for act in actions]
    [25, 7, 8]
    >>> list(map(lambda act:act(5), actions))
    [25, 7, 8]
    >>> 
    """
