#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


# %%

""" GC """
import os
import sys
a = 5555
a = 6666
print(sys.getrefcount(a))

# %%

""" 文档资源

#注释，文件中的文档
dir函数，对象中可用属性的列表
文档字符串dunder-doc，附加在对象上的文件中的文档
pydoc，help函数
pydoc，html报表

import doc_demo
print(doc_demo.__doc__)
print(doc_demo.square.__doc__)
print(doc_demo.Employee.__doc__)

"""


# %%

""" 迭代器，可迭代对象 

手动迭代：iter和next，内置的next函数自动调用一个对象的dunder-next方法。
列表以及很多其他的内置对象，不是自身的迭代器，因为他们支持多次打开迭代器。对于这样的对象，必需使用iter来启动迭代。

    >>> l = [1, 2, 3]
    >>> iter(l) is l
    False
    >>> i = iter(l)
    >>> i.__next__()
    1
    >>> next(i)
    2

for循环使用迭代协议来遍历迭代对象。技术上讲，for循环调用内部等价的dunder-next，而不是next。这两者几乎没有区别。
但是，有些内置对象，支持dunder-next而不支持next，但仍然可以在for循环中迭代。

"""

p = os.popen("ls")
p.__next__()
p.__next__()

# 多个迭代器
r = range(3)
try:
    next(r)
except TypeError:
    print("range是自己的迭代器，手动迭代时，使用iter产生一个迭代器")
i = iter(r)
next(i)
next(i)
i2 = iter(r)
next(i2)
next(i2)

# 单个迭代器, zip, map, filter
z = zip((1, 2, 3), (10, 11, 12))
i1 = iter(z)
i2 = iter(z)
next(i1)
next(i1)
next(i2)
