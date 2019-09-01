#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# %%

""" base """

import decimal
import os
import sys
print(sys.platform)
print(os.getcwd())

# from importlib import reload
# reload(moduleName) # 仅当前模块
# exec(open("base.py").read()) # 重载

print(0.3 == 3 * 0.1)

l = []
if type(l) == type([]) and type(l) == list and isinstance(l, list):
    print("the same")

# %%

""" number """


# %%

""" decimal """

d = decimal.Decimal("3.141")
decimal.getcontext().prec = 2
print(d, decimal.Decimal("3.141"), decimal.Decimal(1)+d)

# %%

""" 字符串 """

print("%s, %d" % ("a", 1))
print("{}, {}".format("a", 1))


# %%

""" dict set """

d = {}
print(d["f"] if "f" in d else 0)

s = set()
s = {1, 1, 2, 3}
z = {3, 4, 5}
print(s)
print(s & z, s | z, s-z)


# %%

def numbers():
    print(8/5)  # division always returns a floating point number


def strings():
    print('doesn\'t')
    print("doesn't")
    print("""\
        Usage: thingy [OPTIONS]
            -h                        Display this usage message
            -H hostname               Hostname to connect to
        """)
    print('''\
        Usage: thingy [OPTIONS]
            -h                        Display this usage message
            -H hostname               Hostname to connect to
        ''')
    print('Py' 'thon')  # can't concatenate a variable and a string literal
    print('Py'
          'thon')

    word = 'Python'
    print(word[0])
    print(word[-1])


if __name__ == "__main__":
    # strings()
    pass


# %%
