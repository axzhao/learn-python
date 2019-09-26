#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


import numbers
from collections import abc
from functools import singledispatch
import html
from decorator_demo2 import clock2
import functools


@clock2
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)


@functools.lru_cache()
@clock2
def fibonacci2(n):
    if n < 2:
        return n
    return fibonacci2(n-2) + fibonacci2(n-1)


def htmlize1(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)


@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)


@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return '<pre>{}</pre>'.format(content)


@htmlize.register(numbers.Integral)
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)


@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'


if __name__ == "__main__":
    print(fibonacci(6))
    print(fibonacci2(6))
    print(htmlize1({1, 2, 3}))
    print(htmlize1(abs))
    print(htmlize1('Heimlich & Co.\n- a game'))
    print(htmlize1(42))
    print(htmlize1(['alpha', 66, {3, 2, 1}]))
    print(htmlize({1, 2, 3}))
    print(htmlize(abs))
    print(htmlize('Heimlich & Co.\n- a game'))
    print(htmlize(42))
    print(htmlize(['alpha', 66, {3, 2, 1}]))
