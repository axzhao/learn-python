#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

def exampleList():
    """
    >>> L = [1,2,3]
    >>> M = ['X', L[:], 'Y']
    >>> L[1] = 0
    >>> L
    [1, 0, 3]
    >>> M
    ['X', [1, 2, 3], 'Y']

    # 不要循环引用
    >>> L = ['grail']
    >>> L.append(L)
    >>> L
    ['grail', [...]]


    >>> seq = [1,2,3,4]
    >>> a,b,c,*d = seq
    >>> print(a,b,c,d)
    1 2 3 [4]
    >>> a,b,c,d,*e = seq
    >>> print(a,b,c,d,e)
    1 2 3 4 []
    >>> *a, b = seq
    >>> print(a,b)
    [1, 2, 3] 4
    >>> a, b = seq[:-1], seq[-1]
    >>> print(a,b)
    [1, 2, 3] 4
    >>> 
    >>> a,b,c,d,e = seq
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    ValueError: not enough values to unpack (expected 5, got 4)


    >>> for (a,*b,c) in [(1,2,3,4), (5,6,7,8)]:
    ...     print(a,b,c)
    ... 
    1 [2, 3] 4
    5 [6, 7] 8

    >>> L = [1,2]
    >>> L[3]
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    IndexError: list index out of range
    >>> L[-44:100]
    [1, 2]
    >>> L[3:1]
    []

    >>> l = ['s','p','a','m']
    >>> l[0][0][0][0][0][0]
    's'

    >>> s = 'spam'
    >>> for (offset, item) in enumerate(s):
    ...     print(offset, item)
    ... 
    0 s
    1 p
    2 a
    3 m

    >>> list(zip([1,2]))
    [(1,), (2,)]
    """


def ExampleSet():
    """
    >>> x = set('abcde')
    >>> y = set('bdxyz')
    >>> 'e' in x
    True
    >>> x-y
    {'e', 'a', 'c'}
    >>> x|y
    {'a', 'x', 'b', 'd', 'e', 'y', 'z', 'c'}
    >>> x&y
    {'d', 'b'}
    >>> x^y
    {'e', 'y', 'z', 'a', 'x', 'c'}
    >>> x>y,x<y
    (False, False)
    >>> z = x.intersection(y)
    >>> z
    {'d', 'b'}
    >>> z.add('spam')
    >>> z
    {'spam', 'd', 'b'}
    >>> z.update(set(['X','Y']))
    >>> z
    {'spam', 'd', 'Y', 'X', 'b'}
    >>> z.remove('b')
    >>> z.add(1)
    >>> z
    {1, 'spam', 'd', 'Y', 'X'}
    """

def ExampleSet2():
    """
    >>> engineers = {'bob', 'sue', 'ann', 'vic'}
    >>> managers = {'tom', 'sue'}
    >>> 'bob' in engineers
    True
    >>> engineers & managers
    {'sue'}
    >>> engineers - managers
    {'ann', 'vic', 'bob'}
    >>> engineers > managers # are all managers engineers?
    False
    """

if __name__ == "__main__":
    import doctest
    doctest.testmod()

