#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import functools
import time


def clock(func):
    """缺点

    1. 不支持关键字参数
    2. 掩盖了被装饰器函数的__name__和__doc__属性
    """
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked


def clock2(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_lsg = []
        if args:
            arg_lsg.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_lsg.append(', '.join(pairs))
        arg_str = ', '.join(arg_lsg)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)


if __name__ == "__main__":
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling snooze(6)')
    print('6! =', factorial(6))
    print(factorial.__name__)  # clocked
