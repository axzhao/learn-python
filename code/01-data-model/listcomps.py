#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


def example():

    # python2.x 中列表推导中的for关键字后的赋值操作可能会影响列表推导上下文中的同名变量
    # python3 都有了自己的局部作用域
    """
    >>> x = 'ABC'
    >>> dummy = [ord(x) for x in x]
    >>> print(x)
    ABC

    >>> dummy
    [65, 66, 67]
    """


def example2():

    # 列表推导式同filter和map比较
    """
    >>> x = 'ABC'
    >>> beyond_ascii = [ord(s) for s in x if ord(s) < 127]
    >>> beyond_ascii
    [65, 66, 67]

    >>> beyond_ascii = list(filter(lambda c: c < 127, map(ord, x)))
    >>> beyond_ascii
    [65, 66, 67]
    """


def example3():

    # 笛卡尔积
    """
    >>> colors = ['black', 'white']
    >>> sizes = ['S', 'M', 'L']
    >>> tshirts = [(color, size) for color in colors for size in sizes]
    >>> tshirts
    [('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'), ('white', 'M'), ('white', 'L')]
    >>> for color in colors:
    ...     for size in sizes:
    ...             print((color, size))
    ... 
    ('black', 'S')
    ('black', 'M')
    ('black', 'L')
    ('white', 'S')
    ('white', 'M')
    ('white', 'L')

    >>> colors = ['black', 'white']
    >>> sizes = ['S', 'M', 'L']
    >>> for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    ...     print(tshirt)
    ... 
    black S
    black M
    black L
    white S
    white M
    white L
    """


def example4():

    # 生成器表达式初始话元组和数组
    """
    >>> symbols = 'ABC'
    >>> tuple(ord(symbol) for symbol in symbols)
    (65, 66, 67)
    >>> import array
    >>> array.array('I', (ord(symbol) for symbol in symbols))
    array('I', [65, 66, 67])

    # 笛卡尔积
    >>> `[(a, b) for a in as for b in bs]`
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod()
