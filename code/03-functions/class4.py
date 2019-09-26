#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


def exampleClass4():
    """
    >>> class Spam:
    ...     numInstances = 0
    ...     def __init__(self):
    ...             Spam.numInstances = Spam.numInstances + 1
    ...     def printNumInstances():
    ...             print('Number of instances created: ', Spam.numInstances)
    ... 
    >>> a = Spam()
    >>> b = Spam()
    >>> c = Spam()
    >>> Spam.printNumInstances()
    Number of instances created:  3
    >>> a.printNumInstances()
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: printNumInstances() takes 0 positional arguments but 1 was given
    """


class Spam:
    num = 0

    def __init__(self):
        Spam.num += 1

    def printNum(cls):
        print("Number of instances:", cls.num)

    printNum = classmethod(printNum)


class Sub(Spam):
    def printNum(cls):
        print("Extra stuff...", cls)
        Spam.printNum()

    printNum = classmethod(printNum)


class Other(Spam):  # inherit class method
    pass


def exampleClass5():
    """
    >>> from class4 import *
    >>> 
    >>> x, y = Sub(), Spam()
    >>> x.printNum()
    Extra stuff... <class 'class4.Sub'>
    Number of instances: 2
    >>> Sub.printNum()
    Extra stuff... <class 'class4.Sub'>
    Number of instances: 2
    >>> y.printNum()
    Number of instances: 2
    >>> z = Other()
    >>> z.printNum()
    Number of instances: 3
    """


class Spam2:
    num = 0

    def __init__(self):
        self.count()

    def count(cls):
        cls.num += 1

    count = classmethod(count)


class Sub2(Spam2):
    num = 0

    def __init__(self):
        Spam2.__init__(self)


class Other2(Spam2):  # inherit class method
    num = 0


def exampleClass6():
    """
    >>> from class4 import *
    >>> x = Spam2()
    >>> y1, y2 = Sub2(), Sub2()
    >>> z1, z2, z3 = Other2(), Other2(), Other2()
    >>> x.num,y1.num,z1.num
    (1, 2, 3)
    >>> Spam.num, Sub.num, Other.num
    (0, 0, 0)
    """