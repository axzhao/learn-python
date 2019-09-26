#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import time

import sys


class Timer:
    def __init__(self, func):
        self.func = func
        self.alltime = 0

    def __call__(self, *args, **kwargs):
        start = time.clock()
        result = self.func(*args, **kwargs)
        elapsed = time.clock()
        self.alltime += elapsed
        print('%s: %.5f, %.5f' % (self.func.__name__, elapsed, self.alltime))
        return result


@Timer
def listcomp(N):
    return [x * 2 for x in range(N)]


if sys.version_info[0] == 2:

    @Timer
    def mapcall(N):
        return map((lambda x: x**2), range(N))

else:

    @Timer
    def mapcall(N):
        return list(map((lambda x: x**2), range(N)))


result = listcomp(5)
listcomp(50000)
listcomp(500000)
listcomp(1000000)
print(result)
print('allTime= %s' % listcomp.alltime)

print('')
result = mapcall(5)
mapcall(50000)
mapcall(500000)
mapcall(1000000)
print(result)
print('allTime= %s' % listcomp.alltime)

print('map/comp = %s' % round(mapcall.alltime / listcomp.alltime, 3))

# map内置函数在python3中返回一个迭代器，2里面是立标，所以python3的map不能和一个列表解析器的工作直接对应。


def timer(label='', trace=True):
    class timer:
        def __init__(self, func):
            self.func = func
            self.alltime = 0

        def __call__(self, *args, **kwargs):
            start = time.clock()
            result = self.func(*args, **kwargs)
            elapsed = time.clock()
            self.alltime += elapsed
            print('%s: %.5f, %.5f' % self.func.__name__, elapsed, self.alltime)
            return result


@timer(label='[ccc]===>')
def listcomp2(N):
    return [x * 2 for x in range(N)]


@timer(trace=True, label='[mmm]===>')
def mapcall2(N):
    return list(map((lambda x: x**2), range(N)))


for func in (listcomp2, mapcall2):
    print('')
    result = func(5)
    func(50000)
    func(500000)
    func(1000000)
    print(result)
    print('allTime= %s' % func.alltime)

    print('map/comp = %s' % round(mapcall.alltime / listcomp.alltime, 3))