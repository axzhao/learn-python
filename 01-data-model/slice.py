#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


def example():
    """
    >>> l = list(range(10))
    >>> l
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> l[2:5] = [20, 30]
    >>> l
    [0, 1, 20, 30, 5, 6, 7, 8, 9]
    >>> del l[5:7]
    >>> l
    [0, 1, 20, 30, 5, 8, 9]

    >>> l = [1, 2, 3]
    >>> l * 5
    [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]

    # 错误的行为
    >>> board = [['_'] * 3 for i in range(3)]
    >>> board
    [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    >>> board[1][2] = 'X'
    >>> board
    [['_', '_', '_'], ['_', '_', 'X'], ['_', '_', '_']]
    >>> weird_board = [['_'] * 3] * 3
    >>> weird_board
    [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    >>> weird_board[1][2] = '0'
    >>> weird_board
    [['_', '_', '0'], ['_', '_', '0'], ['_', '_', '0']]
    >>> board = []
    >>> for i in range(3):
    ...     row = ['_'] * 3
    ...     board.append(row)
    ... 
    >>> board
    [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    >>> board[2][0] = 'X'
    >>> board
    [['_', '_', '_'], ['_', '_', '_'], ['X', '_', '_']]
    >>> 
    >>> row = ['_'] * 3
    >>> board = []
    >>> for i in range(3):
    ...     board.append(row)
    ... 
    >>> board
    [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    >>> board[2][0] = 'X'
    >>> board
    [['X', '_', '_'], ['X', '_', '_'], ['X', '_', '_']]

    # *= : __imul__
    >>> l = [1, 2, 3]
    >>> id(l)
    4373144520
    >>> l *= 2
    >>> l
    [1, 2, 3, 1, 2, 3]
    >>> id(l)
    4373144520
    >>> t = (1, 2, 3)
    >>> id(t)
    4373075216
    >>> t *= 2
    >>> id(t)
    4372131176

    # 一个谜题
    >>> t = (1, 2, [30, 40])
    >>> t[2] += [50, 60]
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
    TypeError: 'tuple' object does not support item assignment
    >>> t
    (1, 2, [30, 40, 50, 60])
    >>> t = (1, 2, [30, 40])
    >>> t[2].extend([50, 60])
    >>> t
    (1, 2, [30, 40, 50, 60])

    # 字节码
    >>> import dis
    >>> dis.dis('s[a]+=b')
    1           0 LOAD_NAME                0 (s)
                2 LOAD_NAME                1 (a)
                4 DUP_TOP_TWO
                6 BINARY_SUBSCR
                8 LOAD_NAME                2 (b)
                10 INPLACE_ADD
                12 ROT_THREE
                14 STORE_SUBSCR
                16 LOAD_CONST               0 (None)
                18 RETURN_VALUE
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod()

