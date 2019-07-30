#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from types import MappingProxyType

if __name__ == "__main__":
    d = {1: "A"}
    d_proxy = MappingProxyType(d)
    print(d_proxy)
    print(d_proxy[1])
    d_proxy[2] = "x"
    d[2] = "B"
    print(d_proxy)
    print(d_proxy[2])
