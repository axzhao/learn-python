#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


class Quantity:

    def __init__(self, storage_name):
        self.storage_name = storage_name  # 托管实例中存储值的属性的名称

    def __set__(self, instance, value):  # 为托管类赋值会调用 dunder-set方法
        if value > 0:
            # 如果使用内置的setattr函数，会再次触发dunder-set方法，导致无限递归
            # 管理实例属性的描述符应该把值存在托管实例中
            instance.__dict__[self.storage_name] = value
        else:
            raise ValueError('value must be > 0')


class LineItem:
    weight = Quantity('weight')  # 描述符实例绑定给weight属性
    price = Quantity('price')

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight  # 特性已经激活了, 因为特性是覆盖型描述符
        self.price = price

    def subtotal(self):
        return self.weight * self.price
