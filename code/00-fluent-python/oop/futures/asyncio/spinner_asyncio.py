#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import asyncio
import itertools
import sys


async def spin(msg):  # 打算交给asyncio处理的协程
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        print(status, flush=True, end='\r')
        try:
            await asyncio.sleep(.1)  # 代替 time.sleep(.1)这样的休眠不会阻塞事件循环
        except asyncio.CancelledError:  # 发出了取消请求
            break
    print(' ' * len(status), end='\r')


async def slow_function():  # 继续执行事件循环
    await asyncio.sleep(3)  # 把控制权交给主循环，在休眠结束后恢复这个协程
    return 42


async def supervisor():
    # async函数排定spin协程的运行事件，使用一个Task对象包装spin协程
    spinner = asyncio.create_task(spin('thinking!'))
    print('spinner object:', spinner)  # 显示Task对象
    # 驱动slow_funciton函数，结束后获取返回值。同时事件循环继续，
    # 因为slow_function中yield from asyncio.sleep(3)，把控制权交给主循环
    result = await slow_function()
    # task对象可以取消，取消后会在协程当前暂停的yield处抛出asyncio.CancelledError异常。
    # 协程可以捕获这个异常，也可以延迟取消，甚至拒绝取消
    spinner.cancel()
    return result


def main():
    result = asyncio.run(supervisor())  # 驱动supervisor协程
    print('Answer:', result)


if __name__ == "__main__":
    main()
