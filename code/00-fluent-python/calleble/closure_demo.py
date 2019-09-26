#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# way 1


class Averager():
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)

# way 2，效率不高


def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)    # 利用了列表是可变的对象
        total = sum(series)
        return total/len(series)
    return averager

# way 3


def make_averager2():
    count = 0
    total = 0

    def averager(new_value):
        # UnboundLocalError: local variable 'count' referenced before assignment
        # count += 1
        # 隐式创建局部变量count，这样count就不是自由变量了，因此不会保存在闭包中
        # count = count + 1
        nonlocal count, total  # 标记自由变量
        count += 1
        total += new_value
        return total / count
    return averager

# way 4
# 好处是，total和count声明为局部变量即可，无需使用实例属性或闭包在多次调用之间保持上下文。


def averager4():
    """
    仅当调用方在协程上调用.close()方法，或者没有对协程的引用而被垃圾回收程序回收时，这个协程才会终止。
    """
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count


if __name__ == "__main__":
    avg = Averager()
    print(avg(10))
    print(avg(11))
    print(avg(12))

    avg2 = make_averager()
    print(avg2(10))
    print(avg2(11))
    print(avg2(12))

    print(avg2.__code__.co_varnames)
    print(avg2.__code__.co_freevars)
    print(avg2.__closure__)
    print(avg2.__closure__[0].cell_contents)

    coro_avg = averager4()
    next(coro_avg)
    coro_avg.send(10)
    coro_avg.send(30)
    coro_avg.send(5)
