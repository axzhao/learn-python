#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


def exampleStdout():
    """
    # f-string
    >>> year = 2016
    >>> event = "haha"
    >>> f'Results of the {year} {event}'
    'Results of the 2016 haha'
    
    >>> yes_votes = 42_572_654
    >>> no_votes = 43_132_495
    >>> percentage = yes_votes / (yes_votes + no_votes)
    >>> '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
    ' 42572654 YES votes  49.67%'
    
    >>> import math
    >>> print(f'The value of pi is approximately {math.pi:.3f}.')
    The value of pi is approximately 3.142.
    
    >>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
    >>> for name, phone in table.items():
    ...     print(f'{name:10} ==> {phone:10d}')
    ...
    
    # '!a' 应用 ascii() ，'!s' 应用 str()，还有 '!r' 应用 repr()
    >>> animals = 'eels'
    >>> print(f'My hovercraft is full of {animals}.')
    My hovercraft is full of eels.
    >>> print(f'My hovercraft is full of {animals!r}.')
    My hovercraft is full of 'eels'.
    
    # str.format()
    >>> print('We are the {} who say "{}!"'.format('knights', 'Ni'))
    We are the knights who say "Ni!"
    >>> print('{1} and {0}'.format('spam', 'eggs'))
    eggs and spam
    >>> print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))
    The story of Bill, Manfred, and Georg.
    >>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
    >>> print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
    ...       'Dcab: {0[Dcab]:d}'.format(table))
    Jack: 4098; Sjoerd: 4127; Dcab: 8637678
    >>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
    >>> print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
    Jack: 4098; Sjoerd: 4127; Dcab: 8637678

    # manual
    >>> for x in range(1, 11):
    ...     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    ...     # Note use of 'end' on previous line
    ...     print(repr(x*x*x).rjust(4))
    ...
    >>> '12'.zfill(5)
    '00012'
    >>> '-3.14'.zfill(7)
    '-003.14'
    >>> '3.14159265359'.zfill(5)
    '3.14159265359'
    
    # sprintf
    >>> import math
    >>> print('The value of pi is approximately %5.3f.' % math.pi)
    The value of pi is approximately 3.142.
    
    # file
    >>> with open("myfile.txt") as f:
    ...     for line in f:
    ...             print(line, end="")
    ... 
    >>> f = open("myfile.txt", "r", encoding="utf-8")
    
    # JSON
    >>> import json
    >>> json.dumps([1, 'simple', 'list'])
    '[1, "simple", "list"]'
    
    # pickle
    """


# pickle 是一种允许对任意复杂 Python 对象进行序列化的协议。因此，它为 Python 所特有，不能用于与其他语言编写的应用程序通信。
# 默认情况下它也是不安全的：如果数据是由熟练的攻击者精心设计的，则反序列化来自不受信任来源的 pickle 数据可以执行任意代码。