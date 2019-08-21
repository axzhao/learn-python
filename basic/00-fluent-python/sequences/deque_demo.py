#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


if __name__ == "__main__":
    """
    队列deque
    - 利用append和pop方法，可以把列表当作栈或者队列来用。但是删除新增操作是很耗时的。collections.deque双向队列是一个线程安全，可以快速添加删除的数据类型。
    - 除了deque外还有其他标准库也有队列的实现
    -- queue：提供同步线程安全类Queue，LifoQueue，PriorityQueue，不同线程可以利用这些数据类型交换数据。可选参数maxsize限制队列大小。队列满了会被锁住，直到另外的线程移除了某个元素腾出位置。
    -- multiprocessing：类似queue.Queue设计给进程通信用的。还有专门的multiprocessing.JoinableQueue类型，让管理更方便。
    -- asyncio：里面有Queue，LifoQueue，PriorityQueue和JoinableQueue，受到queue和multiprocessing模块的影响，但是为异步编程里的任务管理提供了便利。
    -- heapq：没有队列类而是提供了heappush和heappop方法，把可变序列当作队列来使用。
    """
    from collections import deque
    dq = deque(range(10), maxlen=10)
    print(dq)
    dq.rotate(3)
    print(dq)
    dq.rotate(-4)
    print(dq)
    dq.appendleft(-1)
    print(dq)
    dq.extend([11, 22, 33])
    print(dq)
    dq.extendleft([10, 20, 30, 40])
    print(dq)
