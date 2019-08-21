#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# 直接管理函数和类
# 例子：注册函数，在对象定义之后手动调用该函数

registry = {}


def register(obj):
    registry[obj.__name__] = obj
    return obj


@register
def spam(x):
    return (x**2)


@register
def ham(x):
    return (x**3)


@register
class Eggs:
    def __init__(self, x):
        self.data = x**4

    def __str__(self):
        return str(self.data)


print('Manual calls:')
print(spam(2))
print(ham(2))
x = Eggs(2)
print(x)

print('Registry calls')
for name in registry:
    print(name, '=>', registry[name](3))
