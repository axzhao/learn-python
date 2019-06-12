#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

def exampleRecursive():
    """
    >>> def mysum(L):
    ...     if not L:
    ...             return 0
    ...     else:
    ...             return L[0]+mysum(L[1:])
    ... 
    >>> mysum([1,2,3,4,5])
    15
    >>> def mysum(L):
    ...     return 0 if not L else L[0]+mysum(L[1:])
    ... 

    # 下面两种对其他类型友好
    >>> def mysum(L):
    ...     return L[0] if len(L)==1 else L[0] + mysum(L[1:])
    ... 
    >>> def mysum(L):
    ...     first, *rest = L
    ...     return first if not rest else first + mysum(rest)
    >>> mysum([1])
    1
    >>> mysum(('s','p'))
    'sp'

    # 递归在内存空间和执行时间方面效率很能更低
    >>> L = [1,2,3,4,5]
    >>> sum = 0
    >>> for x in L: sum+= x
    ... 
    >>> sum
    15

    >>> def sumtree(L):
    ...     tot = 0
    ...     for x in L:
    ...             if not isinstance(x,list):
    ...                     tot += x
    ...             else:
    ...                     tot += sumtree(x)
    ...     return tot
    ... 
    >>> L = [1,[2,[3,4,5],6,[7,8]]]
    >>> print(sumtree(L))
    36
    """

def exampleIntrospection():
    """
    >>> def func(a):
    ...     b = 'spam'
    ...     return b * a
    ... 
    >>> func(8)
    'spamspamspamspamspamspamspamspam'
    >>> func.__name__
    'func'
    >>> func.__code__
    <code object func at 0x10b750ed0, file "<stdin>", line 1>
    >>> dir(func.__code__)
    ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'co_argcount', 'co_cellvars', 'co_code', 'co_consts', 'co_filename', 'co_firstlineno', 'co_flags', 'co_freevars', 'co_kwonlyargcount', 'co_lnotab', 'co_name', 'co_names', 'co_nlocals', 'co_stacksize', 'co_varnames']
    >>> func.__code__.co_varnames
    ('a', 'b')
    >>> func.__code__.co_argcount
    1
    """

def exampleAnnotations():
    """
    >>> def func(a:'spam', b:(1,10), c:float) -> int:
    ...     return a+b+c
    ... 
    >>> func(1,2,3)
    6
    >>> func.__annotations__
    {'a': 'spam', 'b': (1, 10), 'c': <class 'float'>, 'return': <class 'int'>}
    >>> func.__annotations__['a']
    'spam'
    >>> def func(a:'spam'=4, b:(1,10)=5, c:float=6) -> int:
    ...     return a+b+c
    ... 
    >>> func.__annotations__
    {'a': 'spam', 'b': (1, 10), 'c': <class 'float'>, 'return': <class 'int'>}
    """


def exampleLambda():
    """
    >>> def func(x,y,z): return x+y+z
    ... 
    >>> func(2,4,5)
    11
    >>> f = lambda x,y,z:x+y+z
    >>> f(2,4,5)
    11

    >>> x = (lambda a="fee",b="fie",c="foe":a+b+c)
    >>> x("wee")
    'weefiefoe'

    >>> def knights():
    ...     title = 'Sir'
    ...     action = (lambda x:title+' '+x)
    ...     return action
    ... 
    >>> act = knights()
    >>> act('robin')
    'Sir robin'
    >>> 
    >>> L = [lambda x:x**2, lambda x:x**3, lambda x:x**4]
    >>> for f in L:
    ...     print(f(2))
    ... 
    4
    8
    16
    >>> print(L[0](3))
    9
    """

def exampleMapFilterReduce():
    """
    >>> pow(3,4)
    81
    >>> list(map(pow,[1,2,3], [2,3,4]))
    [1, 8, 81]
    >>> list(filter((lambda x:x>0), range(-5,5)))
    [1, 2, 3, 4]
    >>> from functools import reduce
    >>> reduce((lambda x,y:x+y),[1,2,3,4])
    10
    """

def exampleGenerate():
    """
    >>> (x ** 2 for x in range(4))
    <generator object <genexpr> at 0x10b8307c8>

    >>> sum(x ** 2 for x in range(4))
    14
    >>> sorted(x ** 2 for x in range(4))
    [0, 1, 4, 9]
    >>> sorted((x ** 2 for x in range(4)), reverse=True)
    [9, 4, 1, 0]
    
    >>> def gen():
    ...     for i in range(10):
    ...             x = yield i
    ...             print(x)
    ... 
    >>> g = gen()
    >>> next(g)
    0
    >>> g.send(77)
    77
    1
    >>> g.send(88)
    88
    2
    >>> next(g)
    None
    3

    >>> def mymap(func,*seqs):
    ...     res = []
    ...     for args in zip(*seqs):
    ...             yield func(*args)
    ... 
    >>> list(mymap(abs,[-2]))
    [2]

    >>> def myzip(*seqs):
    ...     minlen = min(len(s) for s in seqs)
    ...     return [tuple(s[i] for s in seqs) for i in range(minlen)] # list
    ... 
    >>> print(myzip('abc','123'))
    [('a', '1'), ('b', '2'), ('c', '3')]

    >>> def myzip(*seqs):
    ...     minlen = min(len(s) for s in seqs)
    ...     return (tuple(s[i] for s in seqs) for i in range(minlen)) # generate
    ... 
    >>> print(myzip('abc','123'))
    [('a', '1'), ('b', '2'), ('c', '3')]
    """

def example():
    """
    # 默认参数是在def语句运行时评估并保存的，而不是在函数调用时
    # def saver(x=None)
    >>> def saver(x=[]):
    ...     x.append(1)
    ...     print(x)
    ... 
    >>> saver([2])
    [2, 1]
    >>> saver()
    [1]
    >>> saver()
    [1, 1]
    >>> saver()
    [1, 1, 1]

    # 便于理解
    >>> def saver():
    ...     saver.x.append(1)
    ...     print(saver.x)
    ... 
    >>> saver.x = []
    >>> saver()
    [1]
    >>> saver()
    [1, 1]
    >>> saver()
    [1, 1, 1]
    """
