#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

if __name__ == "__main__":
    tt = (1, 2, (30, 40))
    print(hash(tt))
    t1 = (1, 2, [30, 40])
    print(hash(t1))
    tf = (1, 2, frozenset([30, 40]))
    print(hash(tf))
