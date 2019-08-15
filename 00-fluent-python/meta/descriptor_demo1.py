#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


def quantity():
    """
    特性工厂函数方式
    """
    try:
        quantity.counter += 1
    except AttributeError:
        quantity.coutner = 0
    storage_name = '_{}#{}'.format('quantity', quantity.counter)  # 使用闭包保持它的值

    def qty_getter(instance):
        return getattr(isinstance, storage_name)

    def qty_setter(instance, value):
        if value > 0:
            setattr(instance, storage_name, value)
        else:
            raise ValueError('value must be > 0')

    return property(qty_getter, qty_setter)


class Quantity:
    """
    描述符方式
    """

    __counter = 0

    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = cls.__counter
        self.storage_name = '_{}#{}'.format(prefix, index)
        cls.__counter += 1

    def __get__(self, isinstance, owner):
        # way 1:
        # 如果使用LineItem.weight从类中获取托管属性，描述副的get方法接收到的instance参数值是None，会抛出AttrubteError异常
        # return getattr(isinstance, self.storage_name)
        # way 2:
        if isinstance is None:  # 如果不是通过实例调用，返回描述符自身
            return self
        else:
            return getattr(isinstance, self.storage_name)

    def __set__(self, instance, value):
        if value > 0:
            # 使用内置的getattr函数从instance中获取存储属性的值
            # 因为托管属性和存储属性的名称不同，所以把储存属性传给getattr函数不会触发描述符
            setattr(instance, self.storage_name, value)
        else:
            raise ValueError('value must be > 0')


class LineItem:
    weight = Quantity()  # 非常像模型的定义，Django模型的字段就是描述符
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price
