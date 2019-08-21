#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# demo 1


def deco(func):
    def inner():
        print('running inner()')
    return inner


@deco
def target():
    print('running target()')


def target2():
    print('running target2()')


target2 = deco(target2)

# demo 2
registry = []


def register(func):
    """函数装饰器在导入模块时立即执行，而被装饰的函数只在明确调用时运行。"""
    print('running register(%s)' % func)
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


def f3():
    print('running f3()')


def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()


if __name__ == "__main__":
    target()
    target2()
    main()


