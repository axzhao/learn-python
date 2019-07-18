#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


class ListInstance:
    def __str__(self):
        return '<Instance of %s, address %s:\n%s>' % (
            self.__class__.__name__, id(self), self.__attrnames())

    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += '\tname %s=%s\n' % (attr, self.__dict__[attr])
        return result


def exampleInstance():
    """
    >>> from oop import *
    >>> class Spam(ListInstance):
    ...     def __init__(self):
    ...             self.data1 = 'food'
    ... 
    >>> x = Spam()
    >>> print(x)
    <Instance of Spam, address 4436048752:
            name data1=food
    >
    >>> str(x)
    '<Instance of Spam, address 4436048752:\n\tname data1=food\n>'
    >>> x
    <__main__.Spam object at 0x10868bb70>
    >>> 
    >>> class Super:
    ...     def __init__(self):
    ...             self.data1 = 'spam'
    ...     def ham(self):
    ...             pass
    ... 
    >>> class Sub(Super, ListInstance):
    ...     def __init__(self):
    ...             Super.__init__(self)
    ...             self.data2 = 'eggs'
    ...             self.data3 = 42
    ...     def spam(self):
    ...             pass
    ... 
    >>> x = Sub()
    >>> print(x)
    <Instance of Sub, address 4436049480:
            name data1=spam
            name data2=eggs
            name data3=42
    >
    >>> 
    >>> class C(ListInstance): pass
    ... 
    >>> x = C()
    >>> x.a = 1; x.b = 2; x.c = 3
    >>> print(x)
    <Instance of C, address 4436049592:
            name a=1
            name b=2
            name c=3
    >
    """


class ListInherited:
    # 也显示继承的方法，必须使用str而不是repr来重载打印，不然会循环
    # 显示一个方法的值，触发该方法的类的repr，从而显示该类
    # 如果repr试图显示一个方法，显示该方法的类将再次触发repr
    # 如果使用repr，可以使用isinstance来比较属性值的类型和标准库中的types.MethodType来省略，避免循环。
    def __str__(self):
        return '<Instance of %s, address %s:\n%s>' % (
            self.__class__.__name__, id(self), self.__attrnames())

    def __attrnames(self):
        result = ''
        for attr in dir(self):
            if attr[:2] == '__' and attr[-2:] == '__':
                result += '\tname %s=<>\n' % attr
            else:
                result += '\tname %s=%s\n' % (attr, getattr(self, attr))
        return result


def exampleInherited():
    """
    >>> class Super:
    ...     def __init__(self):     
    ...             self.data1 = 'spam'
    ...     def ham(self):
    ...             pass
    ... 
    >>> class Sub(Super, ListInherited):
    ...     def __init__(self):
    ...             Super.__init__(self)
    ...             self.data2 = 'eggs'
    ...             self.data3 = 42
    ...     def spam(self):
    ...             pass
    ... 
    >>> x = Sub()
    >>> print(x)
    <Instance of Sub, address 4321980088:
            name _ListInherited__attrnames=<bound method ListInherited.__attrnames of <__main__.Sub object at 0x1019c2eb8>>
            name __class__=<>
            name __delattr__=<>
            name __dict__=<>
            name __dir__=<>
            name __doc__=<>
            name __eq__=<>
            name __format__=<>
            name __ge__=<>
            name __getattribute__=<>
            name __gt__=<>
            name __hash__=<>
            name __init__=<>
            name __init_subclass__=<>
            name __le__=<>
            name __lt__=<>
            name __module__=<>
            name __ne__=<>
            name __new__=<>
            name __reduce__=<>
            name __reduce_ex__=<>
            name __repr__=<>
            name __setattr__=<>
            name __sizeof__=<>
            name __str__=<>
            name __subclasshook__=<>
            name __weakref__=<>
            name data1=spam
            name data2=eggs
            name data3=42
            name ham=<bound method Super.ham of <__main__.Sub object at 0x1019c2eb8>>
            name spam=<bound method Sub.spam of <__main__.Sub object at 0x1019c2eb8>>
    >
    """


class ListTree:
    def __str__(self):
        self.__visited = {}
        return '<Instance of {0}, address {1}:{2}{3}>'.format(
            self.__class__.__name__, id(self), self.__attrnames(self, 0),
            self.__listclass(self.__class__, 4))

    def __listclass(self, aClass, indent):
        dots = '.' * indent
        if aClass in self.__visited:
            return '\n{0}<Class {1}:, address {2}: (see above)>\n>'.format(
                dots, aClass.__name__, id(aClass))
        else:
            self.__visited[aClass] = True
            genabove = (self.__listclass(c, indent + 4)
                        for c in aClass.__bases__)
            return '{0}<Class {1}:, address {2}: \n{3}-{4}-{5}>\n'.format(
                dots, aClass.__name__, id(aClass),
                self.__attrnames(aClass, indent), ''.join(genabove), dots)

    def __attrnames(self, obj, indent):
        spaces = ' ' * (indent + 4)
        result = ''
        for attr in sorted(obj.__dict__):
            if attr.startswith('__') and attr.endswith('__'):
                result += spaces + '{0}=<>\n'.format(attr)
            else:
                result += spaces + '{0}={1}\n'.format(attr, getattr(obj, attr))
        return result


def exampleListTree():
    """
    >>> from magic_method4 import *
    >>> 
    >>> 
    >>> from oop import *
    >>> class Super:
    ...     def __init__(self):   
    ...             self.data1 = 'spam'
    ...     def ham(self):
    ...             pass
    ... 
    >>> class Sub(Super, ListTree):
    ...     def __init__(self):
    ...             Super.__init__(self)
    ...             self.data2 = 'eggs'
    ...             self.data3 = 42
    ...     def spam(self):
    ...             pass
    ... 
    >>> x = Sub()
    >>> print(x)
    <Instance of Sub, address 4303988664:    _ListTree__visited={}
        data1=spam
        data2=eggs
        data3=42
    ....<Class Sub:, address 140414878426328: 
            __doc__=<>
            __init__=<>
            __module__=<>
            spam=<function Sub.spam at 0x10082eae8>
    -........<Class Super:, address 140414875110360: 
                __dict__=<>
                __doc__=<>
                __init__=<>
                __module__=<>
                __weakref__=<>
                ham=<function Super.ham at 0x10082e9d8>
    -............<Class object:, address 4300381856: 
                    __class__=<>
                    __delattr__=<>
                    __dir__=<>
                    __doc__=<>
                    __eq__=<>
                    __format__=<>
                    __ge__=<>
                    __getattribute__=<>
                    __gt__=<>
                    __hash__=<>
                    __init__=<>
                    __init_subclass__=<>
                    __le__=<>
                    __lt__=<>
                    __ne__=<>
                    __new__=<>
                    __reduce__=<>
                    __reduce_ex__=<>
                    __repr__=<>
                    __setattr__=<>
                    __sizeof__=<>
                    __str__=<>
                    __subclasshook__=<>
    --............>
    -........>
    ........<Class ListTree:, address 140414876270056: 
                _ListTree__attrnames=<function ListTree.__attrnames at 0x10082e8c8>
                _ListTree__listclass=<function ListTree.__listclass at 0x10082e840>
                __dict__=<>
                __doc__=<>
                __module__=<>
                __str__=<>
                __weakref__=<>
    -
    ............<Class object:, address 4300381856: (see above)>
    >-........>
    -....>
    >
    >>> 
    """