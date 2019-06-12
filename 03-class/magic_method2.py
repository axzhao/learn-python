#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


class C:
    def __index__(self):
        return 255


class D(C):
    def __getitem__(self, index):
        return 1


def exampleCD():
    """
    >>> import magic_method2 as m
    >>> x = m.C()
    >>> hex(x)
    '0xff'
    >>> ('C'*256)[255]
    'C'
    >>> x[3]
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: 'C' object is not subscriptable
    >>> x = m.D()
    >>> x[3]
    1
    """


class Squares:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop

    def __iter__(self):  # get iterator object on iter
        return self

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value**2


def exampleSquares():
    """
    >>> import magic_method2 as m
    >>> for i in m.Squares(1,5):
    ...     print(i, end=' ')
    ... 
    1 4 9 16 25 
    >>> x = m.Squares(1,5)
    
    # 迭代器没有重载索引表达式。
    >>> x[0]
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: 'Squares' object is not subscriptable
    
    # 单迭代器对象
    # 每次新的循环，需要创建一个新的迭代器对象
    >>> [n for n in x]
    [1, 4, 9, 16, 25]
    >>> [n for n in x]
    []
    """


# 多迭代器对象
class SkipIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.offset = 0

    def __next__(self):
        if self.offset >= len(self.wrapped):
            raise StopIteration
        else:
            item = self.wrapped[self.offset]
            self.offset += 2
            return item


class SkipObject:
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def __iter__(self):
        return SkipIterator(self.wrapped)


def exampleSkipIterator():
    """
    >>> import magic_method2 as m
    >>> alpha = 'abcdef'
    >>> skipper = m.SkipObject(alpha)
    >>> print([x+y for x in skipper for y in skipper])
    ['aa', 'ac', 'ae', 'ca', 'cc', 'ce', 'ea', 'ec', 'ee']
    >>> I = iter(skipper)
    >>> print(next(I), next(I), next(I))
    a c e
    
    >>> s = 'abcdef'
    >>> s = s[::2]
    >>> print([x+y for x in s for y in s])
    ['aa', 'ac', 'ae', 'ca', 'cc', 'ce', 'ea', 'ec', 'ee']
    """


class Iters:
    def __init__(self, value):
        self.data = value

    def __getitem__(self, i):
        print('get[%s]: ' % i, end=' ')
        return self.data[i]

    def __iter__(self):
        print('iter=> ', end=' ')
        self.ix = 0
        return self

    def __next__(self):
        print('next: ', end=' ')
        if self.ix == len(self.data): raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item

    def __contains__(self, x):
        print('contains: ', end=' ')
        return x in self.data


def exampleIters():
    """
    >>> import magic_method2 as m
    >>> x = m.Iters([1,2,3,4,5])
    >>> print(3 in x)
    contains:  True
    >>> for i in x:
    ...     print(i, end='|')
    ... 
    iter=>  next:  1|next:  2|next:  3|next:  4|next:  5|next:  >>> 
    >>> print([i ** 2 for i in x])
    iter=>  next:  next:  next:  next:  next:  next:  [1, 4, 9, 16, 25]
    >>> print(list(map(bin, x)))
    iter=>  next:  next:  next:  next:  next:  next:  ['0b1', '0b10', '0b11', '0b100', '0b101']
    >>> I = iter(x)
    iter=>  >>> 
    >>> while True:
    ...     try:
    ...             print(next(I), end='@')
    ...     except StopIteration:
    ...             break
    ... 
    next:  1@next:  2@next:  3@next:  4@next:  5@next:  >>> 
    """


class empty:
    def __getattr__(self, attrname):
        if attrname == "age":
            return 40
        else:
            raise AttributeError(attrname)

    def __setattr__(self, attr, value):
        if attr == 'age':
            self.__dict__[attr] = value
        else:
            raise AttributeError(attr + ' not allowed')


def exampleEmpty():
    """
    >>> import magic_method2 as m
    >>> x = m.empty()
    >>> x.age
    40
    >>> x.name
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "/Users/Dev/vscode_python/03-class/magic_method2.py", line 169, in __getattr__
        raise AttributeError(attrname)
    AttributeError: name
    >>> x.name = 'mel'
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "/Users/Dev/vscode_python/03-class/magic_method2.py", line 175, in __setattr__
        raise AttributeError(attr + ' not allowed')
    AttributeError: name not allowed
    """