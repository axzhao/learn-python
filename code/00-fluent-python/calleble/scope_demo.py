#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


def f1(a):
    print(a)
    print(b)  # NameError, global name 'b' is not defined


b2 = 6


def f2(a):
    print(a)
    print(b2)


b3 = 6


def f3(a):
    print(a)
    print(b3)  # UnboundLocalError: local variable 'b' referenced before assignment
    b3 = 9


b4 = 6


def f4(a):
    global b4
    print(a)
    print(b4)
    b4 = 9


if __name__ == "__main__":
    try:
        f1(3)
    except:
        pass
    f2(3)
    try:
        f3(3)
    except:
        pass
    f4(3)
    print(b4)
    from dis import dis
    print("-"*5, "dis f1")
    dis(f1)
    print("-"*5, "dis f2")
    dis(f2)
    print("-"*5, "dis f3")
    dis(f3)
    print("-"*5, "dis f4")
    dis(f4)
