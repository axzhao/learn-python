#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import itertools
import random
from tombola import Tombola


class BingoCage(Tombola):

    def __init__(self, items):
        # random.SystemRandom使用os.urandom实现ramdom API，根据os模块的文档，os.urandom生成适合用于加密的随机字节序列
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        self.pick()


class AddableBingoCage(BingoCage):
    """
    不用定义radd方法，因为不需要。如果右操作数是相同类型，那么正向方法add会处理。因此，python计算a+b的时候，
    如果a是AddableBingoCage实例，而b不是，那么会返回NotImplementd，此时或许可以让b所属的类接手处理。可是，
    如果表达式是b+a，而b不是AddableBingoCage实例，返回了NotImplementd，那么最好方法，抛出TypeError，因为无法处理b
    """

    def __add__(self, other):
        if isinstance(other, Tombola):
            return AddableBingoCage(self.inspect() + other.inspect())
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Tombola):
            other_iterable = other.inspect()
        else:
            try:
                other_iterable = iter(other)  # 构建大量数据，所以不用tuple(other)
            except TypeError:
                self_cls = type(self).__name__
                msg = "right operand in += must be {!r} or an iterable"
                raise TypeError(msg.format(self_cls))
        self.load(other_iterable)
        return self
