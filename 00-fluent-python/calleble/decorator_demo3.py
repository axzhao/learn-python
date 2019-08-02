#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

registry = set()  # 添加和删除函数的速度更快


def register(active=True):  # 装饰器工厂
    def decorate(func):  # 装饰器
        print('running register(active=%s)->decorate(%s)' % (active, func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)
        return func
    return decorate


@register(active=False)
def f1():
    print('running f1()')


@register()
def f2():
    print('running f2()')


def f3():
    print('running f3()')


if __name__ == "__main__":
    print(registry)
    print(register()(f3))
    print(registry)
    print(register(active=False)(f2))
    print(registry)
