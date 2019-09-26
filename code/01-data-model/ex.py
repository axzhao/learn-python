#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


def example():
    """
    # 表达式可以作为语句出现，语句不能用作表达式
    >>> x = print('spam')
    spam
    >>> print(x)
    None
    >>> x

    >>> print(1,2,3,sep=', ',end='!\n')
    1, 2, 3!
    >>> print(1,2,3,sep=', ',end='!\n',file=open('data.txt','w'))
    >>> print(open('data.txt').read())
    1, 2, 3!

    # 等价
    >>> print("hello world!")
    hello world!
    >>> import sys
    >>> sys.stdout.write("hello world!")
    hello world!12
    """


def exmapleCopy():
    """
    >>> A = "spam"
    >>> B = A
    >>> B = "shrubbery"
    >>> A
    'spam'
    >>> 
    >>> A = ["spam"]
    >>> B = A
    >>> B[0] = "shrubbery"
    >>> A
    ['shrubbery']
    >>> 
    >>> A = ["spam"]
    >>> B = A[:]
    >>> B[0] = "shrubbery"
    >>> A
    ['spam']


    >>> import copy
    >>> origin = [1, 2, [3, 4]]
    >>> copy1 = copy.copy(origin)
    >>> copy2 = copy.deepcopy(origin)
    >>> copy1 is origin
    False
    >>> origin[2][0] = "hey!"
    >>> origin
    [1, 2, ['hey!', 4]]
    >>> copy1
    [1, 2, ['hey!', 4]]
    >>> copy2
    [1, 2, [3, 4]]
    >>> origin[1] = 9
    >>> origin
    [1, 9, ['hey!', 4]]
    >>> copy1
    [1, 2, ['hey!', 4]]
    >>> copy2
    [1, 2, [3, 4]]
    """

