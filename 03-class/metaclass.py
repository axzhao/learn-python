#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


def exampleType():
    """
    >>> class C:pass
    ... 
    >>> i = C()
    >>> type(i)
    <class '__main__.C'>
    >>> i.__class__
    <class '__main__.C'>
    >>> type(C)
    <class 'type'>
    >>> C.__class__
    <class 'type'>
    >>> C.__base__
    <class 'object'>
    >>> type([1,2,3])
    <class 'list'>
    >>> type(list)
    <class 'type'>
    
    >>> type([1,2,3])
    <class 'list'>
    >>> type(list)
    <class 'type'>
    >>> 
    >>> 
    >>> type(type)
    <class 'type'>
    >>> type(object)
    <class 'type'>
    >>> isinstance(type, object)
    True
    >>> isinstance(object, type)
    True
    >>> type is object
    False
    >>> object is type
    False
    """


def exampleTree():
    """
    >>> class A(object): attr=1
    ... 
    >>> class B(A): pass
    ... 
    >>> class C(A): attr=2
    ... 
    >>> class D(B,C): pass
    ... 
    >>> x = D()
    >>> x.attr
    2
    >>> class D(B,C): attr=C.attr
    ... 
    >>> x = D()
    >>> x.attr
    2
    """


def exampleSlots():
    """
    >>> class E:
    ...     __slots__ = ['c', 'd']
    ... 
    >>> class D(E):
    ...     __slots__ = ['a', '__dict__']
    ... 
    >>> x = D()
    >>> x.a = 1; x.b=2; x.c = 3
    >>> E.__slots__
    ['c', 'd']
    >>> D.__slots__
    ['a', '__dict__']
    >>> x.__slots__
    ['a', '__dict__']
    >>> x.__dict__
    {'b': 2}
    >>> E.__dict__
    mappingproxy({'__module__': '__main__', '__slots__': ['c', 'd'], 'c': <member 'c' of 'E' objects>, 'd': <member 'd' of 'E' objects>, '__doc__': None})
    >>> D.__dict__
    mappingproxy({'__module__': '__main__', '__slots__': ['a', '__dict__'], 'a': <member 'a' of 'D' objects>, '__dict__': <attribute '__dict__' of 'D' objects>, '__doc__': None})
    
    
    >>> class classic:
    ...     def __getattr__(self, name):
    ...             if name == 'age':
    ...                     return 40
    ...             else:
    ...                     raise AttributeError
    
    >>> class newprops(object):
    ...     def getage(self):
    ...             return 40
    ...     def setage(self, value):
    ...             print('set age:', value)
    ...             self._age= value
    ...     age = property(getage, setage, None, None) # get, set, del, docs
    ... 
    >>> x = newprops()
    >>> x.age
    40
    >>> x.age = 42
    set age: 42
    >>> x._age
    42
    >>> x.job = 'trainer'
    >>> x.job
    'trainer'
    >>> x.name
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    AttributeError: 'newprops' object has no attribute 'name'
    """