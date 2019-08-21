#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


from collections import namedtuple

Result = namedtuple('Result', 'count average')


def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break  # 为了返回值，协程必须正常终止
        total += term
        count += 1
        average = total/count
    return Result(count, average)


def exampleCoroutine2():
    """
    >>> coro_avg = averager()
    >>> next(coro_avg)
    >>> coro_avg.send(10)
    >>> coro_avg.send(30)
    >>> coro_avg.send(6.5)
    >>> coro_avg.send(None)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    StopIteration: Result(count=3, average=15.5)
    >>> 
    >>> coro_avg = averager()
    >>> next(coro_avg)
    >>> coro_avg.send(10)
    >>> coro_avg.send(30)
    >>> coro_avg.send(6.5)
    >>> try:
    ...     coro_avg.send(None)
    ... except StopIteration as exc:
    ...     result = exc.value
    ... 
    >>> result
    Result(count=3, average=15.5)
    """
