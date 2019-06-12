#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

def exampleIter():
    """
    >>> l = [1,2,3]
    >>> i = iter(l)
    >>> i
    <list_iterator object at 0x10ef4c208>
    >>> while True:
    ...     try:
    ...             x = next(i)
    ...     except StopIteration:
    ...             break
    ...     print(x, end=' ')
    ... 
    1 2 3

    # zip, map, filter 不支持相同结果上的多个活跃迭代器
    # 单个的迭代器意味着一个对象返回其自身
    >>> m = map(abs, (-1,0,1))
    >>> i1 = iter(m); i2 = iter(m)
    >>> print(next(i1), next(i2))
    1 0
    >>> print(next(i1), next(i2))
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    StopIteration
    """