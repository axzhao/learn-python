#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


import struct
import os

# 使用 mmap 模块把图像打开为内存映射文件，那么会复制少量字节。
# 结构体的格式：< 是小字节序，3s3s 是两个 3 字节序列，HH 是两个 16 位二进制整数。
fmt = '<3s3sHH'

if __name__ == "__main__":
    with open('img.gif', 'rb') as fp:
        img = memoryview(fp.read())
    header = img[:10]  # 这里不会复制字节序列。
    print(bytes(header))
    print(struct.unpack(fmt, header))  # 拆包 memoryview 对象，得到一个元组，包含类型、版本、宽度和高度。
    del header  # 删除引用，释放 memoryview 实例所占的内存。
    del img

    for codec in ['latin_1', 'utf_8', 'utf_16']:
        print(codec, 'El Niño'.encode(codec), sep='\t')
