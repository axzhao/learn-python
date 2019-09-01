#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


"""

    >>> from class_meta_demo import *
    >>> Dog = record_factory('Dog', 'name weight owner')
    >>> rex = Dog('Rex', 30, 'Bob')
    >>> rex
    Dog(name='Rex', weight=30, owner='Bob')
    >>> name, weight, _ = rex
    >>> name, weight
    ('Rex', 30)
    >>> "{2}'s dog weights {1}kg".format(*rex)
    "Bob's dog weights 30kg"
    >>> rex.weight = 32
    >>> rex
    Dog(name='Rex', weight=32, owner='Bob')
    >>> Dog.__mro__
    (<class 'class_meta_demo.Dog'>, <class 'object'>)

"""


import collections
from descriptor_demo2 import Validated, NonBlack, Quantity


def record_factory(cls_name, field_names):
    """
    我们本可以把dunder-slots类属性的名称改成其他值，不过要是那样的话，就要实现dunder-setattr方法，
    为属性赋值时验证属性的名称，因为对于记录这样的类，我们希望属性始终是固定的那几个，而且顺序相同。

    局限不能序列化，即不能使用pickle模块里的dump/load函数处理。
    """
    try:
        field_names = field_names.replace(',', ' ').split()
    except AttributeError:
        pass
    field_names = tuple(field_names)

    def __init__(self, *args, **kwargs):
        attrs = dict(zip(self.__slots__, args))
        attrs.update(kwargs)
        for name, value in attrs.items():
            setattr(self, name, value)

    def __iter__(self):
        for name in self.__slots__:
            yield getattr(self, name)

    def __repr__(self):
        values = ', '.join('{}={!r}'.format(*i)
                           for i in zip(self.__slots__, self))
        return '{}({})'.format(self.__class__.__name__, values)

    cls_attrs = dict(__slots__=field_names,
                     __init__=__init__,
                     __iter__=__iter__,
                     __repr__=__repr__)

    return type(cls_name, (object,), cls_attrs)


"""

    >>> raisins = LineItem('Golden raisins', 10, 6.95)
    >>> dir(raisins)[:3]
    ['_NonBlack#description', '_Quantity#price', '_Quantity#weight']
    >>> LineItem.description.storage_name
    '_NonBlack#description'
    >>> raisins.description
    'Golden raisins'

"""


def entity(cls):
    for key, attr in cls.__dict__.items():
        if isinstance(attr, Validated):
            type_name = type(attr).__name__
            attr.storage_name = '_{}#{}'.format(type_name, key)
    return cls


@entity
class LineItem:
    description = NonBlack()
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


"""
定制描述类的元类
"""


class EntityOrdedMeta(type):
    """元类，用于创建带有验证字段的业务实体"""

    @classmethod
    def __prepare__(cls, name, bases):
        return collections.OrderdDict()

    def __init__(cls, name, bases, attr_dict):
        super().__init__(name, bases, attr_dict)
        cls._field_names = []
        for key, attr in attr_dict.items():
            if isinstance(attr, Validated):
                type_name = type(attr).__name__
                attr.storage_name = '_{}#{}'.format(type_name, key)
                cls._field_names.append(key)


class EntityOrded(metaclass=EntityOrdedMeta):
    """带有验证字段的业务实体"""

    @classmethod
    def field_names(cls):
        for name in cls._field_names:
            yield name


class EntityMeta(type):
    """元类，用于创建带有验证字段的业务实体"""

    def __init__(cls, name, bases, attr_dict):
        super().__init__(name, bases, attr_dict)
        for key, attr in attr_dict.items():
            if isinstance(attr, Validated):
                type_name = type(attr).__name__
                attr.storage_name = '_{}#{}'.format(type_name, key)


class Entity(metaclass=EntityMeta):
    """带有验证字段的业务实体"""


class LineItem2(Entity):
    description = NonBlack()
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price
