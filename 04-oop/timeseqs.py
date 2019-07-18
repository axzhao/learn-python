#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import time
import sys

reps = 1000
repslist = range(reps)

def timer(func, *pargs, **kargs):
     start = time.perf_counter()
     for i in repslist:
         ret = func(*pargs, **kargs)
     elapsed = time.perf_counter() - start
     return (elapsed, ret)

def forLoop():
     res = []
     for x in repslist:
          res.append(abs(x))
     return res

def listComp():
     return [abs(x) for x in repslist]

def mapCall():
     return list(map(abs, repslist))

def genExpr():
     return list(abs(x) for x in repslist)

def genFunc():
     def gen():
          for x in repslist:
               yield abs(x)
     return list(gen())

print(sys.version)
for test in (forLoop, listComp, mapCall, genExpr, genFunc):
     elapsed, result = timer(test)
     print('-'*32)
     print('%-9s: %.5f => [%s...%s]' % (test.__name__, elapsed, result[0], result[-1]))

