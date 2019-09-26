#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

def exampleArgs():
    """
    # 默认参数 和 关键字参数
    >>> def func(spam, eggs, toast=0, ham=0):
    ...     print((spam, eggs, toast, ham))
    ... 
    >>> func(1,2)
    (1, 2, 0, 0)
    >>> func(1,ham=1,eggs=0)
    (1, 0, 0, 1)
    >>> func(spam=1,eggs=0)
    (1, 0, 0, 0)
    >>> func(1,2,3,4)
    (1, 2, 3, 4)

    # 任意参数
    >>> def f(a, *pargs, **kargs): print(a, pargs, kargs)
    ... 
    >>> f(1,2,3,x=1,y=2)
    1 (2, 3) {'x': 1, 'y': 2}

    # 解包参数
    >>> def func(a,b,c,d): print(a,b,c,d)
    ... 
    >>> args = (1,2)
    >>> args += (3,4)
    >>> func(*args)
    1 2 3 4
    >>> func(*(1,2),**{'d':4,'c':5})
    1 2 5 4
    >>> func(1, c=3, *(2,),**{'d':4})
    1 2 3 4
    >>> func(1, c=3, *(2,),**{'d':4})
    1 2 3 4
    >>> func(1,*(2,3),d=4)
    1 2 3 4
    >>> func(1,*(2,3),4)
    1 2 3 4

    # * 号分隔
    >>> def kwonly(a,*,b,c):
    ...     print(a,b,c)
    ... 
    >>> kwonly(1,c=3,b=2)
    1 2 3
    >>> kwonly(c=3,b=2,a=1)
    1 2 3
    >>> def kwonly(a,*,b='spam',c='ham'):
    ...     print(a,b,c)
    ... 
    >>> kwonly(1)
    1 spam ham
    >>> kwonly(c=3,b=2,a=1)
    1 2 3
    >>> 

    # ex
    >>> def minmax(test, *args):
    ...     res = args[0]
    ...     for arg in args[1:]:
    ...             if test(arg, res):
    ...                     res = arg
    ...     return res
    ... 
    >>> def lessthan(x,y): return x < y
    ... 
    >>> def grtrthan(x,y): return x > y
    ... 
    >>> print(minmax(lessthan, 4,2,1,5,6,3))
    1
    >>> print(minmax(grtrthan, 4,2,1,5,6,3))
    6
    """

