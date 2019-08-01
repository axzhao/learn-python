#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import collections

if __name__ == "__main__":
    ct = collections.Counter("abracadabra")
    print(ct)
    ct.update("aaaaazzz")
    print(ct)
    print(ct.most_common(2))
