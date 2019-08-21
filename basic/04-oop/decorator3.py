#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# 单体类

instances = {}


def getInstance(aClass, *args):
    if aClass not in instances:
        instances[aClass] = aClass(*args)
    return instances[aClass]


# # python的内省工具来从一个已准备创建好的实例获取类
# # 假设创建一个初始化实例是可以接受的
# instances = {}
# def getInstance:
#     aClass = object.__class__
#     if aClass not in instances:
#         instances[aClass] = object
#     return instances[aCalss]


def singleton(aClass):
    def onCall(*args):
        return getInstance(aClass, *args)

    return onCall


@singleton
class Person:
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate

    def pay(self):
        return self.hours * self.rate


@singleton
class Spam:
    def __init__(self, val):
        self.attr = val


bob = Person('Bob', 40, 10)
print(bob.name, bob.pay())

sue = Person('Sue', 50, 20)
print(sue.name, sue.pay())

x = Spam(42)
y = Spam(99)
print(x.attr, y.attr)


# 为每个类使用了一个封闭作用域，而不是为每个类使用一个全局表入口
def singleton(aClass):
    instance = None

    def onCall(*args):
        nonlocal instance
        if instance == None:
            instance = aClass(*args)
        return instance

    return onCall


# 只想要一个实例，但并不总是这样的
class singleton:
    def __init__(self, aClass):
        self.aClass = aClass
        self.instance = None

    def __call__(self, *args):
        if self.instance == None:
            self.instance = self.aClass(*args)
        return self.instance


# 跟踪对象接口


def Tracer(aClass):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.fetches = 0
            self.wrapped = aClass(*args, **kwargs)

        def __getattr__(self, attrname):
            print('Trace: ' + attrname)
            self.fetches += 1
            return getattr(self.wrapped, attrname)

    return Wrapper


@Tracer
class Spam:
    def display(self):
        print('Spam!' * 8)


@Tracer
class Person:
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate

    def pay(self):
        return self.hours * self.rate


food = Spam()
food.display()
print([food.fetches])

bob = Person('Bob', 40, 50)
print(bob.name)
print(bob.pay())

print('')
sue = Person('Sue', rate=100, hours=60)
print(sue.name)
print(sue.pay())

print(bob.name)
print(bob.pay())
print([bob.fetches, sue.fetches])

# 类错误二：保持多个实例


class Trace:
    def __init__(self, aClass):
        self.aClass = aClass

    def __call__(self, *args):
        self.wrapped = self.aClass(*args)
        return self

    def __getattr__(self, attrname):
        print('Trace:' + attrname)
        return getattr(self.wrapped, attrname)


@Tracer
class Spam:
    def display(self):
        print('Spam!' * 8)


food = Spam()
food.display()


@Tracer
class Person:
    def __init__(self, name):
        self.name = name


bob = Person('Bob')
print(bob.name)
sue = Person('Sue')
print(sue.name)
print(bob.name)