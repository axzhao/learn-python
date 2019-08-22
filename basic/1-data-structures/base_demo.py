#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

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

""" 列表 list

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

print("%(n)d %(x)s" % {"n": 1, "x": "spam"})

# page: 232
print("{0:.2f}".format(1/3.0), "{0:.{1}f}".format(1/3.0, 4))


# %%
