#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""

覆盖型描述符的行为

    >>> obj = Managed() 
    >>> obj.over  # 触发描述符get方法，第二个参数的值是托管实例obj
    -> Overriding.__get__(<Overriding object>, <Managed object>, <class Managed>)
    >>> Managed.over # 触发描述符get方法，第二个参数的值是instance，None
    -> Overriding.__get__(<Overriding object>, None, <class Managed>)
    >>> obj.over = 7  
    -> Overriding.__set__(<Overriding object>, <Managed object>, 7)
    >>> obj.over  
    -> Overriding.__get__(<Overriding object>, <Managed object>, <class Managed>)
    >>> obj.__dict__['over'] = 8  # 跳过描述符访问实例属性
    >>> vars(obj)  
    {'over': 8}
    >>> obj.over  # 覆盖读取
    -> Overriding.__get__(<Overriding object>, <Managed object>, <class Managed>)

没有get方法的覆盖型描述符

    >>> obj.over_no_get # 没有get方法，获取描述符实例
    <descriptorkinds.OverridingNoGet object at 0x...>
    >>> Managed.over_no_get 
    <descriptorkinds.OverridingNoGet object at 0x...>
    >>> obj.over_no_get = 7
    -> OverridingNoGet.__set__(<OverridingNoGet object>, <Managed object>, 7)
    >>> obj.over_no_get  # 描述符实例
    <descriptorkinds.OverridingNoGet object at 0x...>
    >>> obj.__dict__['over_no_get'] = 9 # 跳过描述符访问实例属性
    >>> obj.over_no_get # 因为没有get方法，访问实例属性
    9
    >>> obj.over_no_get = 7
    -> OverridingNoGet.__set__(<OverridingNoGet object>, <Managed object>, 7)
    >>> obj.over_no_get
    9

没有实现set方法的非覆盖型描述符

    >>> obj = Managed()
    >>> obj.non_over  
    -> NonOverriding.__get__(<NonOverriding object>, <Managed object>, <class Managed>)
    >>> obj.non_over = 7  # 无干涉赋值操作的set方法
    >>> obj.non_over  
    7
    >>> Managed.non_over  
    -> NonOverriding.__get__(<NonOverriding object>, None, <class Managed>)
    >>> del obj.non_over  
    >>> obj.non_over  # 描述符的get方法，第二个参数的值是托管实例
    -> NonOverriding.__get__(<NonOverriding object>, <Managed object>, <class Managed>)

在类中覆盖描述符

    >>> obj = Managed() 
    >>> Managed.over = 1  # 覆盖类中的描述符属性
    >>> Managed.over_no_get = 2
    >>> Managed.non_over = 3
    >>> obj.over, obj.over_no_get, obj.non_over   
    (1, 2, 3)

方法是非覆盖型描述符

    >>> obj.spam   # 获取绑定方法对象
    <bound method Managed.spam of <descriptorkinds.Managed object at 0x...>>
    >>> Managed.spam # 获取的是函数
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
    >>> obj.spam = 7 # 遮盖类属性
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




import collections
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
    normal = 1

    def spam(self):  # 对比，因为方法也是描述符
        print('-> Managed.spam({})'.format(display(self)))


"""
    >>> word = Text('forward')
    >>> word  
    Text('forward')
    >>> word.reverse()  
    Text('drawrof')
    >>> Text.reverse(Text('backward'))  
    Text('drawkcab')
    >>> type(Text.reverse), type(word.reverse)  # function函数，method方法
    (<class 'function'>, <class 'method'>)
    >>> list(map(Text.reverse, ['repaid', (10, 20, 30), Text('stressed')])) 
    ['diaper', (30, 20, 10), Text('desserts')]
    >>> Text.reverse.__get__(word)  # 函数都是非覆盖型描述符，得到绑定到那个实例上的方法
    <bound method Text.reverse of Text('forward')>
    >>> Text.reverse.__get__(None, Text)  
    <function Text.reverse at 0x101244e18>
    >>> word.reverse   # 会调用 Text.reverse.__get__(word) 返回对应的绑定方法
    <bound method Text.reverse of Text('forward')>
    >>> word.reverse.__self__   # 调用这个方法的实例引用
    Text('forward')
    >>> word.reverse.__func__ is Text.reverse # 绑定方法__func__属性是依附在托管类上那个原始函数的引用
    True
"""


class Text(collections.UserString):

    def __repr__(self):
        return 'Text({!r})'.format(self.data)

    def reverse(self):
        return self[::-1]
