#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


class GetAttr:
    eggs = 88  # eggs stored on class, spam on instance

    def __init__(self):
        self.spam = 77

    def __len__(self):  # len here, else __getattr__ called with __len__
        print('__len__: 42')
        return 42

    def __getattr__(self, attr):  # provide __str__ if asked, else dummy func
        print('getattr: ' + attr)
        if attr == '__str__':
            return lambda *args: '[Getattr str]'
        else:
            return lambda *args: None


class GetAttribute:
    eggs = 88

    def __init__(self):
        self.spam = 77

    def __len__(self):
        print('__len__: 42')
        return 42

    def __getattribute__(self, attr):
        print('getattribute: ' + attr)
        if attr == '__str__':
            return lambda *args: '[Getattr str]'
        else:
            return lambda *args: None


for Class in GetAttr, GetAttribute:
    print('\n' + Class.__name__.ljust(50, '='))
    x = Class()
    x.eggs
    x.spam
    x.other
    len(x)
    try:
        x[0]  # __getitem__ ?
    except:
        print('fail []')

    try:
        x + 99  # __add__ ?
    except:
        print('fail []')

    try:
        x()  # __call__ ? implicit via built-in
    except:
        print('fail ()')

    x.__call__()  # __call__ ? explicit, not inherited
    print(x.__str__())  # __str__ ? explicit, inherited from type
    print(x)  # __str__ ? implicit via built-in
