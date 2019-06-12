#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

x = 1
y = [1, 2]

def func():
    print(x, y)

print(__name__)

def exampleSmall():
    """
    # from 复制的变量会变成共享对象的引用。

    >>> from small import x,y,func
    small
    >>> x = 42
    >>> y[0] = 42
    >>> func()
    1 [42, 2] 
    >>> 
    >>> import small
    >>> small.x
    1
    >>> small.y
    [42, 2]
    >>> from importlib import reload
    >>> reload(small)
    small
    <module 'small' from '/Users/Dev/vscode_python/02-def-module/module/module1/small.py'>
    >>> small.y
    [1, 2]
    """