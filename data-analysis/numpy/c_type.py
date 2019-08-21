#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import numpy as np
import time

""" 在 axis 上的动作 """

col_major = np.zeros((10, 10), order='C')    # C-type
row_major = np.zeros((10, 10), order='F')    # Fortran

a = np.zeros((200, 200), order='C')
b = np.zeros((200, 200), order='F')
N = 9999


def f1(a):
    for _ in range(N):
        np.concatenate((a, a), axis=0)


def f2(b):
    for _ in range(N):
        np.concatenate((b, b), axis=0)


def f3(a):
    for _ in range(N):
        np.vstack((a, a))


t0 = time.time()
f1(a)
t1 = time.time()
f2(b)
t2 = time.time()
f3(a)
t3 = time.time()

print((t1-t0)/N)     # 0.000040
print((t2-t1)/N)     # 0.000070
print((t3-t2)/N)     # 0.000060

""" 对上面用 "C-type" 创建的 a 矩阵选点 """

indices = np.random.randint(0, 100, size=10, dtype=np.int32)
a[indices, :]     # 0.000003
a[:, indices]     # 0.000006
