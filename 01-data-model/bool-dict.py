#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


def exampleBool():
    """
    >>> type(True)
    <class 'bool'>
    >>> isinstance(True,int)
    True
    >>> True == 1 # save value
    True
    >>> True is 1 # but different object
    False
    >>> True or False
    True
    >>> True + 4
    5

    >>> [] or 3
    3
    >>> [] or {}
    {}
    >>> [] and {}
    []
    >>> 3 and []
    []

    >>> x = 1
    >>> if x:
    ...     a = 2
    ... else:
    ...     a = 3
    ... 
    >>> a
    2
    >>> a = 2 if x else 3
    >>> a
    2
    >>> a = [3, 2][bool(x)]
    >>> a
    2

    >>> x = "X" or "x" or None
    >>> x
    'X'
    """

def ExampleDict():
    """
    >>> a = {1:'a',2:'b',3:33,'d':4}
    >>> a['5']
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    KeyError: '5'
    >>> '5' in a
    False
    >>> a.get('5', 0)
    0
    >>> a['5'] if '5' in a else 0
    0

    >>> list(zip(['a','b','c'],[1,2,3]))
    [('a', 1), ('b', 2), ('c', 3)]
    >>> zip(['a','b','c'],[1,2,3])
    <zip object at 0x102ed1208>
    >>> dict(zip(['a','b','c'],[1,2,3]))
    {'a': 1, 'b': 2, 'c': 3}
    >>> {k:v for (k,v) in zip(['a','b','c'],[1,2,3])}
    {'a': 1, 'b': 2, 'c': 3}

    >>> dict.fromkeys(['a','b','c'], 0)
    {'a': 0, 'b': 0, 'c': 0}
    >>> {k:None for k in ['a','b','c']}
    {'a': None, 'b': None, 'c': None}

    >>> d = dict(a=1,b=2,c=3)
    >>> d
    {'a': 1, 'b': 2, 'c': 3}
    >>> k = d.keys()
    >>> k
    dict_keys(['a', 'b', 'c'])
    >>> list(k)
    ['a', 'b', 'c']
    >>> v = d.values()
    >>> v
    dict_values([1, 2, 3])
    >>> list(v)
    [1, 2, 3]
    >>> list(d.items())
    [('a', 1), ('b', 2), ('c', 3)]

    >>> d = {}
    >>> d[1]='a'
    >>> d[2]='b'
    >>> d
    {1: 'a', 2: 'b'}
    >>> d[(1,2,3)] = 'c'
    >>> d
    {1: 'a', 2: 'b', (1, 2, 3): 'c'}


    >>> d = {1:'a', 2:'b'}
    >>> for key in d:
    ...     print(key, '=>', d[key])
    ... 
    1 => a
    2 => b
    """

    