#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


from abc import ABC, abstractclassmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')

# 策略模式
# 策略对象通常是很好的享元，享元是可共享的对象，可以同时在多个上下文中使用
# 函数比定义的类的实例轻量，而且无需使用享元模式，因为各个策略函数在只会创建一次

# 找出模块中的全部策略
# 模块也是一等函数，globals()返回一个表示当前的全局符号表的一个字典，这个符号表始终针对当前模块
# 对函数或方法来说，是指定义他们的模块，而且不是调用他们的模块


class LineItem:

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:  # 上下文
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = cart
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())

# @promotion


def fidelity_promo(order):
    """为积分为1000或以上的顾客提供5%折扣"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

# @promotion


def bulk_item_promo(self, order):
    """单个商品为20个或以上时提供10%折扣"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

# @promotion


def large_order_promo(self, order):
    """订单中的不同商品达到10个或以上时提供7%折扣"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0

# 装饰器优点
# 0. 不用每用一个要加入
# 1. 策略函数不用使用特殊名称
# 2. 方便禁用策略，对比添加
# 3. 可以在其他模块运行
# promos = []
# def promotion(promo_func):
#     promos.append(promo_func)
#     return promo_func

# promos = [fidelity_promo, bulk_item_promo, large_order_promo]
promos = [globals()[name] for name in globals()
          if name.endswith('_promo') and name != 'best_promo']

# 将promotions的独立模块内构建策略函数列表
# promos = [func for name, func in inspect.getmembers(promotions, inspect.isfunction)]


def best_promo(order):
    """选择可用的最佳折扣
    """
    return max(promo(order) for promo in promos)


def exampleDesignPatternDemo():
    """
    >>> joe = Customer('John Doe', 0)
    >>> ann = Customer('Ann Smith', 1100)
    >>> cart = [LineItem('banana', 4, .5), LineItem('apple', 10, 1.5), LineItem('watermellon', 5, 5.0)]
    >>> Order(joe, cart, fidelity_promo)
    <Order total: 42.00 due: 42.00>
    >>> Order(ann, cart, fidelity_promo)
    <Order total: 42.00 due: 39.90>
    >>> banana_cart = [LineItem('banana', 30, .5), LineItem('apple', 10, 1.5)]
    >>> Order(joe, banana_cart, bulk_item_promo)
    <Order total: 30.00 due: 28.50>
    >>> long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
    >>> Order(joe, long_order, large_order_promo)
    <Order total: 10.00 due: 9.30>
    >>> Order(joe, cart, large_order_promo)
    <Order total: 42.00 due: 42.00>
    >>> Order(joe, cart, best_promo)
    >>> Order(joe, banana_cart, best_promo)
    >>> Order(joe, cart, best_promo)
    """


# 命令模式是回调机制的面向对象替代品

class MacroCommand:
    """一个执行一组命令的命令"""

    def __init__(self, commands):
        self.commands = list(commands)

    def __call__(self):
        for command in self.commands:
            command()
