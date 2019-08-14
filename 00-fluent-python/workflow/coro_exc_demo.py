#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


class DemoException(Exception):
    pass


def demo_exc_handling():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:
            print('*** DemoException handled. Continuing...')
        else:
            print('-> coroutine received: {!r}'.format(x))
    # 因为只有未处理的异常才会中止那个循环，而一旦出现未处理的异常，协程会立即终止
    raise RuntimeError('This line should never run.')


def demo_finally():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:
            print('*** DemoException handled. Continuing...')
        else:
            print('-> coroutine received: {!r}'.format(x))
        finally:
            print('-> coroutine ending')


def exampleCoroExcDemo():
    """
    >>> exc_coro = demo_exc_handling()
    >>> next(exc_coro)
    -> coroutine started
    >>> exc_coro.send(11)
    -> coroutine received: 11
    >>> exc_coro.send(22)
    -> coroutine received: 22
    >>> exc_coro.close()
    >>> from inspect import getgeneratorstate
    >>> getgeneratorstate(exc_coro)
    'GEN_CLOSED'
    >>> 
    >>> exc_coro = demo_exc_handling()
    >>> next(exc_coro)
    -> coroutine started
    >>> exc_coro.send(11)
    -> coroutine received: 11
    >>> exc_coro.throw(DemoException)
    *** DemoException handled. Continuing...
    >>> getgeneratorstate(exc_coro)
    'GEN_SUSPENDED'
    >>> exc_coro = demo_exc_handling()
    >>> 
    >>> next(exc_coro)
    -> coroutine started
    >>> exc_coro.send(11)
    -> coroutine received: 11
    >>> exc_coro.throw(ZeroDivisionError)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "/Users/Dev/vscode_python/00-fluent-python/workflow/coro_exc_demo.py", line 13, in demo_exc_handling
        x = yield
    ZeroDivisionError
    >>> getgeneratorstate(exc_coro)
    'GEN_CLOSED'
    """
