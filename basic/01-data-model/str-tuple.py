#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


def exampleTuple():
    """
    >>> x = (40)
    >>> x
    40
    >>> x = (40, )
    >>> x
    (40,)
    """

def exampleStr():
    """
    >>> s = 's\np'
    >>> print(s)
    s
    p
    >>> s = r's\np'
    >>> print(s)
    s\np
    
    >>> 'spam'[1:3]
    'pa'
    >>> 'spam'[slice(1,3)]
    'pa'
    >>> 'spam'[::-1]
    'maps'
    >>> 'spam'[slice(None,None,-1)]
    'maps'

    >>> print(str('spam'), repr('spam'))
    spam 'spam'

    >>> "%(n)d%(x)s" % {"n":1, "x":"spam"}
    '1spam'
    >>> '{motto},{0} and {food}'.format(42, motto=3.14, food=[1,2])
    '3.14,42 and [1, 2]'

    >>> import sys
    >>> 'My {1[spam]} runs {0.platform}'.format(sys, {'spam':'laptop'})
    'My laptop runs darwin'
    >>> 'My {config[spam]} runs {sys.platform}'.format(sys=sys, config={'spam':'laptop'})
    'My laptop runs darwin'


    >>> print('%s=%s' % ('spam', 12))
    spam=12
    >>> print('{0}={1}'.format('spam', 12))
    spam=12

    >>> s="spam"
    >>> s[0][0][0][0][0][0]
    's'


    >>> s = '''aaa
    ... bbb
    ... ccc'''
    >>> s
    'aaa\nbbb\nccc'
    >>> s = ('aaaa'
    ... 'bbbb'
    ... 'cccc')
    >>> s
    'aaaabbbbcccc'
    """