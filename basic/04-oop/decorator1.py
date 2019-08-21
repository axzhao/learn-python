#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# demo1


# 当用于类方法的时候，失效，因为self是装饰器的示例，并且装饰的主体类的示例没有包含在*args中
# 只传递了tracer实例，没有在参数列表中传递person主体
# tracer不知道要用方法调用处理的person实例的信息，没有办法创建一个带有一个实例的绑定的方法
class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)


@tracer
def spam(a, b, c):
    print(a + b + c)


spam(1, 2, 3)
spam(a=1, b=2, c=3)


class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    @tracer
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    @tracer
    def lastName(self):
        return self.name.split()[-1]


bob = Person('Bob', 5000)
bob.giveRaise(.25)
print(bob.lastName())

# 函数可能更加方便，避免了意外地直接调用最初的函数

calls = 0


def tracer(func, *args):
    global calls
    calls += 1
    print('call %s to %s' % (calls, func.__name__))
    func(*args)


def spam(a, b, c):
    print(a, b, c)


spam(1, 2, 3)
trancer(spam, 1, 2, 3)

# demo2

calls = 0


def tracer(func, *args):
    def wrapper(*args, **kwargs):
        global calls
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)

    return wrapper


@tracer
def spam(a, b, c):
    print(a, b, c)


spam(1, 2, 3)

# demo3


def tracer(func, *args):
    calls = 0

    def wrapper(*args, **kwargs):
        nonlocal calls
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)

    return wrapper


@tracer
def spam(a, b, c):
    print(a, b, c)


spam(1, 2, 3)


def tracer(func, *args):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


# demo4


class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)

    def __get__(self, instance, owner):
        return wrapper(self, instance)


class wrapper:
    def __init__(self, desc, subj):
        self.desc = desc
        self.subj = subj

    def __call__(self, *args, **kwargs):
        return self.desc(self.subj, *args, **kwargs)


@tracer
def spam(a, b, c):
    print(a, b, c)


class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    @tracer
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    @tracer
    def lastName(self):
        return self.name.split()[-1]


class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)

    def __get__(self, instance, owner):
        def wrapper(*args, **kwargs):
            return self(instance, *args, **kwargs)

        return wrapper
