#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from concurrent import futures
from flags import save_flag, get_flag, show, main

MAX_WORKERS = 20  # 最多使用几个线程


def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc


def download_many(cc_list):
    workers = min(MAX_WORKERS, len(cc_list))
    # executor.__exit__方法会调用executor.shutdown(wait=True)方法，会在所有线程完成前阻塞线程
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(download_one, sorted(cc_list))

    return len(list(res))  # 如果有线程抛出异常，异常会在这里抛出。这与隐式调用next()函数从迭代器中获取相应的返回值一样


if __name__ == "__main__":
    main(download_many)
