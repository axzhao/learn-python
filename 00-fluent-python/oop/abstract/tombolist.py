#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


from random import randrange
from tombola import Tombola


@Tombola.register
class TomboList(list):
    """
    list的真实子类和Tombola的虚拟子类
    """

    def pick(self):
        if self:
            position = randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('pop from empty TomboList')

    load = list.extend

    def loaded(self):  # 不能采用load方法的那种方式，因为list类型没有实现loaded方法需要的dunder-bool方法。而内置的bool函数不需要dunder-bool方法，因为其还可以使用dunder-len方法。
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))

# Tombola.register(TomboList)
