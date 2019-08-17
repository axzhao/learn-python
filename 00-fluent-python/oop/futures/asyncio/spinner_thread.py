#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import threading
import itertools
import time
import sys


class Signal:
    go = True  # 用于从外部控制线程


def spin(msg, signal):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('\/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))  # \x08 退格符
        time.sleep(.1)
        if not signal.go:
            break
    write(' ' * len(status) + '\x08' * len(status))


def slow_function():
    # 假装等待IO一段时间
    time.sleep(3)  # 阻塞主线程，不过一定要这么做，以便释放GIL，创建从属线程
    return 42


def supervisor():  # 从属线程
    signal = Signal()
    spinner = threading.Thread(target=spin, args=('thinking!', signal))
    print('spinner object:', spinner)
    spinner.start()  # 启动从属线程
    result = slow_function()  # 阻塞主线程，同时显示动画
    signal.go = False
    spinner.join()  # 等待spinner线程结束
    return result


def main():
    result = supervisor()
    print('Answer:', result)


if __name__ == "__main__":
    main()
