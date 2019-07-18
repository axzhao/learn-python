#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

x = 1
import mod2
print(x, end='')
print(mod2.x, end='')
print(mod2.mod3.x)

# import mod2.mod3
# print(mod2.mod3.x)

from mod2 import x
# from . import x