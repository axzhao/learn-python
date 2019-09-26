#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import array

if __name__ == "__main__":
    """
    内存试图memoryview
    - 不复制内容的情况下操作同一个数组的不同切片，在数据结构之间共享内存，收到NumPy的启发。其中数据结构可以是任何形式，比如PIL图片，NumPy的数组。在处理大型数据集合的时候非常重要。
    - memoryview.cast能用不同的方式读写同一块内存数据，而且内容字节不会随意移动。把同一块内存里的内容打包成一个新的memoryview对象给你。
    """
    numbers = array.array("h", [-2, -1, 0, 1, 2])
    memv = memoryview(numbers)
    print(len(memv, memv[0]))
    memv_oct = memv.cast("B")
    print(memv_oct.tolist())
    memv_oct[5] = 4
    print(numbers)
