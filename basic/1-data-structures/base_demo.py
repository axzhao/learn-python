#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# %%

""" Python """

# 运算符重载
try:
    print("42" + 1)
except TypeError:
    print("设计上，因为+既能够进行加法运算也能够进行合并操作，这种转换的选择会变得模棱两可")

# 列表 append，sort 就地修改，返回None

# 列表
try:
    l = []
    l[99] = 'spam'
except IndexError:
    print("在列表末尾外的偏移赋值是非法的")

# %%

""" Numeric

# floor : next-lower integer
# trunc : drop decimal digits
# round : 四舍五入

# 尽管可以把浮点数转换为分数，但是可能会有不避免的的精度损失

    >>> from fractions import Fraction
    >>> 4.0 / 3
    1.3333333333333333
    >>> (4.0 / 3).as_integer_ratio()
    (6004799503160661, 4503599627370496)
    >>> x = Fraction(1, 3)
    >>> a = x + Fraction(*(4.0 / 3).as_integer_ratio())
    >>> a
    Fraction(22517998136852479, 13510798882111488)
    >>> 22517998136852479 / 13510798882111488
    1.6666666666666665
    >>> a.limit_denominator(10)
    Fraction(5, 3)

"""

import copy
from fractions import Fraction
from decimal import Decimal
import decimal
import random
import math
import sys

# ord 单个自负的字符串装换乘整数字符编码
print(ord("2"), chr(50))

# divide, floor divide, floor, trunc
print(repr(5/3), str(5/3))
print(5/2, 5//2, math.floor(-2.5), math.trunc(2.5))
print(math.floor(-2.5), math.trunc(-2.5))

# oct, hex, bin
print(0o100, 0x40, 0b1000000)
print(oct(64), hex(64), bin(64))
print(int('0o100', 8), int('0x40', 16), int('0b1000000', 2))

# eval : 将字符串作为python代码运行
print(eval('64'), eval('0o100'))

# format string
print('{0:o}, {1:x}, {2:b}'.format(64, 64, 64))
print('%o, %x, %X' % (64, 255, 255))

# random
print(random.random())
print(random.randint(1, 10))
print(random.choice(['a', 'b', 'c']))

# decimal
print(0.1 + 0.1 + 0.1 - 0.3)
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.30'))
decimal.getcontext().prec = 4
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.30'))
with decimal.localcontext() as ctx:
    ctx.prec = 2
    print(Decimal('1.00') / decimal.Decimal('3.00'))


# fraction
print(Fraction(4, 6))
print(Fraction.from_float(1.75), (2.5).as_integer_ratio())
print(Fraction(*2.5.as_integer_ratio()))


# bool
print(isinstance(True, int))

# %%

""" 字符串

str：Unicode文本
bytes：二进制数据
bytearray：可变的bytes

# open(r'C:\new')
# open('C:\\new')
# print(r'1\nb\tc\\'[:-1], r'1\nb\tc' + '\\', '1\\nb\\tc\\')

字符串格式化代码 %[(name)][flags][width][.precesion]typecode
falgs：左对齐 -， 正负号 +，补零 0
typecode：s: dunder-str r: dunder-repr c: char d: 十进制 i: 整数 u: 无符号整数 
        o: 八进制整数 x: 十六进制整数 X: 大写 e: 浮点指数 E: 大写
        f: 浮点十进制 F: 浮点十进制 g: 浮点e或f G: 浮点E或F %: 常量%

格式化字符串代码 {filedname!conversionflag:formatspec}
filedname：或偏移量n，或fieldname[index]，或filedname.name
conversionflag：r: dunder-repr, s: dunder-st, a: ascii
formatspec：[[fill]align][sign][#][o][with][.precesion][typecode]
formatspec：字段宽度，对齐方式，补零，小数点精度，并且以一个可选的数据类型编码结束
align: >, <, =, ^ 左对齐，右对齐，补充，居中

"""

print("haha\n", r"haha\n", b"haha\n")
s = "\n hahahaha \n"
print(s.find('hah'), s.lstrip(), s.split('h'))
print(s.isdigit(), s.endswith('\n'), ".".join(['1', '2']))
print(chr(115))


x = 1.23456789
print("{0:,d}".format(999999999))
print("%e | %f | %g" % (x, x, x))
print("%-6.2f | %05.2f | %+06.1f" % (x, x, x))
print("%f | %.2f | %.*f" %(1/3.0, 1/3, 4, 1/3.0)) # * 计算得出width和precision
print("{motto}, {0} and {food}".format(42, motto=3.14, food=[1,2]))
print("%(n)d %(x)s" % {"n": 1, "x": "spam"})
print('My {1[spam]} runs {0.platform}'.format(sys, {'spam': "laptop"}))
print('My {config[spam]} runs {sys.platform}'.format(sys=sys,config={'spam':'laptop'}))
print("{0:.2f}".format(1/3.0), "{0:.{1}f}".format(1/3.0, 4))

somelist = list('SPAM')
print("first={0[0]}, third={0[2]}".format(somelist))
print("first={0}, last={1}".format(somelist[0], somelist[-1]))

print("{0:10} = {1:10}".format("spam", 123.4567))
print("{0:>10} = {1:<10}".format("spam", 123.4567))
print("{0.platform:>10} = {1[item]:<10}".format(sys, dict(item='laptop')))
print("{0:f}, {1:.2f}, {2:06.2f}".format(x, x, x))

print("{0:X}, {1:o}, {2:b}".format(255,255,255))

# %%

""" 元组 tuple

t = (0,)
t = 1, 2, 3
t = (1, 2, 3)

"""

# %%

""" 列表 list

分片赋值最好分成两步理解
1. 删除，删除等号左边指定的分片
2. 插入。将包含在等号右边对象中的片段插入旧分片被删除的位置

l2 = l[:]               # Make top-level "shallow" copy
l2 = copy.copy(l)       # same
l2 = copy.deepcopy(l)   # Make deep copy of any object l: copy all nested parts

    >>> l
    [1, [2, [3, 4]]]
    >>> l2
    [1, [2, [3, 4]]]
    >>> l3
    [1, [2, [3, 4]]]
    >>> l4
    [1, [2, [3, 4]]]
    >>> l[1][1][0] = 9
    >>> l2
    [1, [2, [9, 4]]]
    >>> l3
    [1, [2, [9, 4]]]
    >>> l4
    [1, [2, [3, 4]]]
    >>> l[0] = 6
    >>> l2
    [1, [2, [9, 4]]]
    >>> l3
    [1, [2, [9, 4]]]
    >>> l4
    [1, [2, [3, 4]]]

"""

l = [1,2,3,4]
l[1:2] = []
print(l) # l[1:2] = [] 其实是删除操作
l[len(l):] = [6]
print(l) # l.append(6), 和‘+’ 合并不同，append不用产生新对象，执行起来更快

l = ['abc', 'ABD', 'aBe']
l.sort(key=str.lower, reverse=True) # 非同类型列表sort TypeError
print(l)

print(sorted(l, key=str.lower, reverse=True)) # 非原地修改sort

# list comprehension

# %%

""" 字典 dict
key：hashable

字典，关联数组 associative array，散列表 hash

字典视图：keys, values, items 都返回视图对象
视图对象是可迭代的，这意味着对象每次产生一个结果项，而不是在内存中立即产生结果列表。
keys视图支持集合操作，values由于不是唯一的所以不支持集合操作。
但items结果是的，如果(key, value)对是唯一的并且可散列的话。
"""

print(dict([('name', 'mel'), ('age', 45)]))
print(dict.fromkeys(['a', 'b'], 0))
d = dict(zip(['a', 'b'], [1, 2]))
print(d.keys(), d.values(), d.items())
dd = d.copy()
print('c' in dd, dd.get('c', 'default'), dd.keys() & d.keys())
print(d.update(dd)) # 合并，盲目覆盖
del d['a']
print(d.pop('a', 'default'))

# 字典用于稀疏数据结构
m = {(2,3,4): 88, (7,8,9): 99}
print(m)

d = {'a':1, 'b':2, 'c':3}
k = d.keys()
print(k | {'x': 4}, k | {'x'})

# %%

""" 集合 set, fronzenset
元素：hashable

# a none dict: {}
# a none set:  set()

# x > y superset, x < y subset

"""


engineers = {'bob', 'sue', 'ann', 'vic'}
managers = {'tom', 'sue'}
print('bob' in engineers)
# who is both engineer and manager
print(engineers & managers)
# all people in either category
print(engineers | managers)
# engineers who are not managers
print(engineers - managers)
# are all managers engineers? superset
print(engineers > managers)
# are both engineers? subset
print({'bob', 'sue'} < engineers)
# all people is a suerpser of managers
print((managers | engineers) > managers)
# who is in one but not both
print(managers ^ engineers)
# intersection
print((managers | engineers) - (managers ^ engineers))

x = set([666])
y = {999}
x.add('ha')
x.update(set([1, 2]))
x.remove('ha')
print(x)
print(x.intersection(y), x.union(y), x.issubset(y))

# %%

