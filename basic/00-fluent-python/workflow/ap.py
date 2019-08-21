#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# 内置range函数用于生成有穷整数等差数列ArithmeticProgression，AP。itertools.cout函数用于生成无穷等差数列。

# way 1
import itertools


class ArithmeticProgression:

    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end  # None -> 无穷数列

    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)  # 算数运算符会隐式应用数值强制转换规则
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            # 使用index变量，把self.begin与self.step和index计算，以此降低处理浮点数时累积效应致错的风险
            result = self.begin + self.step * index

# way 2
# 如果一个类只是为了构建生成器而去实现iter方法，那还不如使用生成器函数。毕竟，生成器函数是制造生成器的工厂


def aritprog_gen(begin, step, end=None):
    result = type(begin + step)(begin)  # 算数运算符会隐式应用数值强制转换规则
    forever = end is None
    index = 0
    while forever or result < end:
        yield result
        index += 1
        # 使用index变量，把begin与step和index计算，以此降低处理浮点数时累积效应致错的风险
        result = begin + step * index


# way 3
gen = itertools.count(1, .5)
next(gen)

# 生成一个使用另一个生成器的生成器，在指定的条件计算结果为False时停止。
gen = itertools.takewhile(lambda n: n < 3, itertools.count(1, .5))
list(gen)


def aritprog_gen2(begin, step, end=None):
    first = type(begin + step)(begin)
    ap_gen = itertools.count(first, step)
    if end is not None:
        ap_gen = itertools.takewhile(lambda n: n < end, ap_gen)
    return ap_gen
