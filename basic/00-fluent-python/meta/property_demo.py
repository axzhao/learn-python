#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


class LineItem0:
    """1. 特性，管理实例属性的类属性

    """

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight  # 特性启动
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value > 0:
            self.__weight = value + 10
        else:
            raise ValueError('value must be > 0')


def quantity(storage_name):
    """2. 特性工厂函数

    """

    def qty_getter(instance):
        return instance.__dict__[storage_name]

    def qty_setter(instance, value):
        if value > 0:
            # 值直接从__dict__获取，为的是跳过特性，防止无限递归
            instance.__dict__[storage_name] = value + 10
        else:
            raise ValueError('value must be > 0')

    return property(qty_getter, qty_setter)


class LineItem1:
    weight = quantity('weight')
    price = quantity('price')

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight  # 特性已经激活了, 因为特性是覆盖型描述符
        self.price = price

    def subtotal(self):
        return self.weight * self.price


if __name__ == "__main__":
    l0 = LineItem0('xx', 1, 2)
    print(l0.__dict__)  # description, price, _LineItem0_weight
    print(LineItem0.__dict__)
    print(l0.weight)  # 1
    print(LineItem0.weight)  # property object

    l1 = LineItem1('xx', 1, 2)
    print(l1.__dict__)  # description, price, weight
    print(LineItem1.__dict__)
    print(l1.weight)  # 11
    print(LineItem1.weight)  # property object

"""

    >>> from property_demo import *
    >>> knight = BlackKnight()
    >>> knight.member
    next member is:
    'an arm'
    >>> del knight.member
    BLACK KNIGHT (loses an arm)
    -- 'Tis but a scratch.
    >>> del knight.member
    BLACK KNIGHT (loses another arm)
    -- It's just a flesh wound.
    >>> del knight.member
    BLACK KNIGHT (loses a leg)
    -- I'm invincible!
    >>> del knight.member
    BLACK KNIGHT (loses another leg)
    -- All right, we'll call it a draw.

"""


class BlackKnight:
    """ 3. 特性的删除方法
    """

    def __init__(self):
        self.members = ['an arm', 'another arm', 'a leg', 'another leg']
        self.pharases = ["'Tis but a scratch.", "It's just a flesh wound.",
                         "I'm invincible!", "All right, we'll call it a draw."]

    @property
    def member(self):
        print('next member is:')
        return self.members[0]

    @member.deleter
    def member(self):
        text = 'BLACK KNIGHT (loses {})\n-- {}'
        print(text.format(self.members.pop(0), self.pharases.pop(0)))

    # member = property(member_getter, fdel=member_deleter)
