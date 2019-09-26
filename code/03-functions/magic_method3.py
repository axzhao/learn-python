#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


class PrivateExc(Exception):
    pass


class Privacy:
    def __setattr__(self, attr, value):
        if attr in self.privates:
            raise PrivateExc(attr, self)
        else:
            self.__dict__[attr] = value


class Test1(Privacy):
    privates = ['age']


class Test2(Privacy):
    privates = ['name', 'pay']

    def __init__(self):
        self.__dict__['name'] = 'Tom'


def examplePrivacy():
    """
    >>> from magic_method3 import *
    >>> x = Test1()
    >>> y = Test2()
    >>> 
    >>> x.name = 'Bob'
    >>> y.name = 'Sue'
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "/Users/Dev/vscode_python/03-class/magic_method3.py", line 12, in __setattr__
        raise PrivateExc(attr, self)
    magic_method3.PrivateExc: ('name', <magic_method3.Test2 object at 0x10b09d5c0>)
    >>> 
    >>> y.age = 30
    >>> z.age = 30
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    NameError: name 'z' is not defined
    """


class adder:
    def __init__(self, value=0):
        self.data = value

    def __add__(self, other):
        self.data += other


class addrepr(adder):
    def __repr__(self):
        return 'addrepr (%s)' % self.data


class addstr(adder):
    def __str__(self):
        return 'addstr (%s)' % self.data


class addboth(adder):
    def __str__(self):
        return '[value: %s]' % self.data

    def __repr__(self):
        return 'addboth (%s)' % self.data


class Printer:
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return str(self.val)


class Printer2(Printer):
    def __repr__(self):
        return str(self.val)


def exampleReprAndStr():
    """
    # addrepr
    >>> from magic_method3 import *
    >>> x = adder()
    >>> print(x)
    <magic_method3.adder object at 0x103a87550>
    >>> x
    <magic_method3.adder object at 0x103a87550>
    >>> x = addrepr(2)
    >>> x + 1
    >>> x
    addrepr (3)
    >>> str(x), repr(x)
    ('addrepr (3)', 'addrepr (3)')
    
    # addstr
    >>> x = addstr(3)
    >>> x + 1
    >>> x
    <magic_method3.addstr object at 0x10da73550>
    >>> print(x)
    addstr (4)
    >>> str(x), repr(x)
    ('addstr (4)', '<magic_method3.addstr object at 0x10da73550>')
    
    # addboth
    >>> x = addboth(4)
    >>> x + 1
    >>> x
    addboth (5)
    >>> print(x)
    [value: 5]
    >>> str(x), repr(x)
    ('[value: 5]', 'addboth (5)')
    
    # printer
    >>> objs = [Printer(2), Printer(3)]
    >>> for x in objs: print(x)
    ... 
    2
    3
    >>> print(objs)
    [<magic_method3.Printer object at 0x1071cd588>, <magic_method3.Printer object at 0x1071e6d30>]
    >>> objs
    [<magic_method3.Printer object at 0x1071cd588>, <magic_method3.Printer object at 0x1071e6d30>]
    >>> objs = [Printer2(2), Printer2(3)]
    >>> for x in objs: print(x)
    ... 
    2
    3
    >>> print(objs)
    [2, 3]
    >>> objs
    [2, 3]
    """


class Commuter:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other

    def __radd__(self, other):
        print('radd', self.val, other)
        return other + self.val


class Commuter2:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        if isinstance(other, Commuter2): other = other.val
        return Commuter2(self.val + other)

    def __radd__(self, other):
        return Commuter2(other + self.val)

    def __str__(self):
        return '<Commuter2: %s>' % self.val


def exampleCommuter():
    """
    >>> from magic_method3 import *
    >>> x = Commuter(88)
    >>> y = Commuter(99)
    >>> x + 1
    add 88 1
    89
    >>> 1 + y
    radd 99 1
    100
    >>> x + y # instance + instance, triggers __radd__
    add 88 <magic_method3.Commuter object at 0x105d645c0> 
    radd 99 88
    187
    >>> x = Commuter2(88)
    >>> y = Commuter2(99)
    >>> print(x+10)
    <Commuter2: 98>
    >>> print(10+y)
    <Commuter2: 109>
    >>> z = x+y  # not nested: doesn't recur to __radd__
    >>> print(z)
    <Commuter2: 187>
    >>> print(z+10)
    <Commuter2: 197>
    >>> print(z+z)
    <Commuter2: 374>
    """


class Number:
    def __init__(self, val):
        self.val = val

    def __iadd__(self, other):  # explicit: x += y
        self.val += other
        return self  # usually returns self

    def __add__(self, other):  # fallback: x = (x+y)
        return Number(self.val + other)  # propagates class type


def exampleNumber():
    """
    >>> from magic_method3 import *
    >>> x = Number(5)
    >>> x += 1
    >>> x += 1
    >>> x.val
    7
    """