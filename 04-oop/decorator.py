#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


# 函数装饰器

def decorator(F):
    def wrapper(*args):
    return wrapper

@decorator
def func(x,y):...

class decorator:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args):
        ...

@decorator
def func(x,y):...

class C:
    @decorator
    def method(self, x, y):...

# 类装饰器

@decorator
class C:...

class C:...
C = decorator(C)


def decorator(cls):
    class Wrapper:
        def __init__(self, *args):
            self.wrapper = cls(*args)

        def __getattr__(self, name):
            return getattr(self.wrapped, name)

    return Wrapper


@decorator
class C:
    def __init__(self, x, y):
        self.attr = 'spam'


x = C(6, 7)
print(x.attr)

class Decorator:
    def __init__(self, C):
        self.C = C
    def __call__(self, *args):
        self.wrapped = self.C(*args)
        return self
    def __getattr__(self, attrname):
        return getattr(self.wrapped, attrname)
    
@Decorator
class C:...

x = C()

def decorator(C):
    class Wrapper:
        def __init__(self, *args):
            self.wrapped = C(*args)
    return Wrapper

class Wrapper: ...

def decorator(C):
    def onCall(*args):
        return Wrapper(C(*args))
    return onCall



def d1(F): return lambda: 'X' + F()
def d2(F): return lambda: 'Y' + F()
def d3(F): return lambda: 'Z' + F()

@d1
@d2
@d3
def func():
    return 'spam'

print(func())

# lambda 函数来实现包装器层，每个层在一个封闭的作用域里保持了包装的函数。
