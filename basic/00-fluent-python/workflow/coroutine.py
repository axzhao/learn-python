#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


"""
用于计算移动平均值的协程

    >>> coro_avg = averager4()
    >>> from inspect import getgeneratorstate
    >>> getgeneratorstate(coro_avg)
    'GEN_SUSPENDED'
    >>> coro_avg.send(10)
    10.0
    >>> coro_avg.send(30)
    20.0
    >>> coro_avg.send(5)
    15.0
    >>> coro_avg.send('spam')
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) for +=: 'float' and 'str'
    >>> coro_avg.send(60)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    StopIteration
"""

from coroutil import coroutine


@coroutine
def averager4():
    """
    仅当调用方在协程上调用.close()方法，或者没有对协程的引用而被垃圾回收程序回收时，这个协程才会终止。
    """
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count
