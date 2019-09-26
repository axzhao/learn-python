#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import threading
import itertools
import time
import sys


def spin(msg, done):
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        print(status, end='\r')
        if done.wait(.1):
            break
    print(' ' * len(status), end='\r')


def slow_function():
    # 假装等待IO一段时间
    time.sleep(3)  # 阻塞主线程，不过一定要这么做，以便释放GIL，创建从属线程
    return 42


def supervisor():  # 从属线程
    done = threading.Event()
    spinner = threading.Thread(target=spin, args=('thinking!', done))
    print('spinner object:', spinner)
    spinner.start()  # 启动从属线程
    result = slow_function()  # 阻塞主线程，同时显示动画
    done.set()
    spinner.join()  # 等待spinner线程结束
    return result


def main():
    result = supervisor()
    print('Answer:', result)


if __name__ == "__main__":
    main()
