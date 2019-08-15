#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""

覆盖型描述符的行为

    >>> obj = Managed() 
    >>> obj.over  
    -> Overriding.__get__(<Overriding object>, <Managed object>, <class Managed>)
    >>> Managed.over 
    -> Overriding.__get__(<Overriding object>, None, <class Managed>)
    >>> obj.over = 7  
    -> Overriding.__set__(<Overriding object>, <Managed object>, 7)
    >>> obj.over  
    -> Overriding.__get__(<Overriding object>, <Managed object>, <class Managed>)
    >>> obj.__dict__['over'] = 8  
    >>> vars(obj)  
    {'over': 8}
    >>> obj.over  
    -> Overriding.__get__(<Overriding object>, <Managed object>, <class Managed>)

没有get方法的覆盖型描述符

    >>> obj.over_no_get  
    <descriptorkinds.OverridingNoGet object at 0x...>
    >>> Managed.over_no_get 
    <descriptorkinds.OverridingNoGet object at 0x...>
    >>> obj.over_no_get = 7
    -> OverridingNoGet.__set__(<OverridingNoGet object>, <Managed object>, 7)
    >>> obj.over_no_get  
    <descriptorkinds.OverridingNoGet object at 0x...>
    >>> obj.__dict__['over_no_get'] = 9
    >>> obj.over_no_get
    9
    >>> obj.over_no_get = 7
    -> OverridingNoGet.__set__(<OverridingNoGet object>, <Managed object>, 7)
    >>> obj.over_no_get
    9

非覆盖型描述符

    >>> obj = Managed()
    >>> obj.non_over 
    -> NonOverriding.__get__(<NonOverriding object>, <Managed object>, <class Managed>)
    >>> obj.non_over = 7  
    >>> obj.non_over  
    7
    >>> Managed.non_over  
    -> NonOverriding.__get__(<NonOverriding object>, None, <class Managed>)
    >>> del obj.non_over  
    >>> obj.non_over  
    -> NonOverriding.__get__(<NonOverriding object>, <Managed object>, <class Managed>)

在类中覆盖描述符

    >>> obj = Managed() 
    >>> Managed.over = 1  
    >>> Managed.over_no_get = 2
    >>> Managed.non_over = 3
    >>> obj.over, obj.over_no_get, obj.non_over  
    (1, 2, 3)

方法是非覆盖型描述符

    >>> obj.spam  
    <bound method Managed.spam of <descriptorkinds.Managed object at 0x...>>
    >>> Managed.spam 
    <function Managed.spam at 0x...>
    >>> obj.spam()
    -> Managed.spam(<Managed object>)
    >>> Managed.spam()
    Traceback (most recent call last):
      ...
    TypeError: spam() missing 1 required positional argument: 'self'
    >>> Managed.spam(obj)
    -> Managed.spam(<Managed object>)
    >>> Managed.spam.__get__(obj)  # doctest: +ELLIPSIS
    <bound method Managed.spam of <descriptorkinds.Managed object at 0x...>>
    >>> obj.spam.__func__ is Managed.spam
    True
    >>> obj.spam = 7
    >>> obj.spam
    7
"""

"""
NOTE: These tests are here because I can't add callouts after +ELLIPSIS
directives and if doctest runs them without +ELLIPSIS I get test failures.
# BEGIN DESCR_KINDS_DEMO2
    >>> obj.over_no_get  # <1>
    <__main__.OverridingNoGet object at 0x665bcc>
    >>> Managed.over_no_get  # <2>
    <__main__.OverridingNoGet object at 0x665bcc>
    >>> obj.over_no_get = 7  # <3>
    -> OverridingNoGet.__set__(<OverridingNoGet object>, <Managed object>, 7)
    >>> obj.over_no_get  # <4>
    <__main__.OverridingNoGet object at 0x665bcc>
    >>> obj.__dict__['over_no_get'] = 9  # <5>
    >>> obj.over_no_get  # <6>
    9
    >>> obj.over_no_get = 7  # <7>
    -> OverridingNoGet.__set__(<OverridingNoGet object>, <Managed object>, 7)
    >>> obj.over_no_get  # <8>
    9
# END DESCR_KINDS_DEMO2
Methods are non-overriding descriptors:
# BEGIN DESCR_KINDS_DEMO5
    >>> obj = Managed()
    >>> obj.spam  # <1>
    <bound method Managed.spam of <descriptorkinds.Managed object at 0x74c80c>>
    >>> Managed.spam  # <2>
    <function Managed.spam at 0x734734>
    >>> obj.spam = 7  # <3>
    >>> obj.spam
    7
# END DESCR_KINDS_DEMO5
"""


### 辅助函数，仅用于显示 ###


def cls_name(obj_or_cls):
    cls = type(obj_or_cls)
    if cls is type:
        cls = obj_or_cls
    return cls.__name__.split('.')[-1]


def display(obj):
    cls = type(obj)
    if cls is type:
        return '<class {}>'.format(obj.__name__)
    elif cls in [type(None), int]:
        return repr(obj)
    else:
        return '<{} object>'.format(cls_name(obj))


def print_args(name, *args):
    pseudo_args = ', '.join(display(x) for x in args)
    print('-> {}.__{}__({})'.format(cls_name(args[0]), name, pseudo_args))


### 示例类 ###

class Overriding:
    """也称为数据描述符或强制描述符"""

    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)

    def __set__(self, instance, value):
        print_args('set', self, instance, value)


class OverridingNoGet:
    """没有dunder-get方法的覆盖型描述符"""

    def __set__(self, instance, value):
        print_args('set', self, instance, value)


class NonOverriding:
    """也称非数据描述符或遮盖性描述符"""

    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)


class Managed:
    over = Overriding()
    over_no_get = OverridingNoGet()
    non_over = NonOverriding()

    def spam(self):  # 对比，因为方法也是描述符
        print('-> Managed.spam({})'.format(display(self)))
