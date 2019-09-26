#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import contextlib


@contextlib.contextmanager
def looking_glass():

    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    # way 1
    # 严重错误：如果在with块中抛出异常，解释器会捕获然后在yield表达式再次抛出。但是，这里没有错误处理代码，因此函数会中止，永远无法恢复原来的sys.stdout.write方法了
    # yield 'JABBERWOCKY'
    # sys.stdout.write = original_write
    # way2
    msg = ''
    try:
        yield 'JABBERWOCKY'
    except ZeroDivisionError:
        msg = 'Please DO NOT divide by zero!'
    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)


def exampleMirrorGen():
    """
    >>> from mirror_gen import looking_glass
    >>> with looking_glass() as what:
    ...     print('Alice, Kitty and Snowdrop')
    ...     print(what)
    ... 
    pordwonS dna yttiK ,ecilA
    YKCOWREBBAJ
    >>> what
    'JABBERWOCKY'
    """
