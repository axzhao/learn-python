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
    cc_list = cc_list[:5]
    with futures.ThreadPoolExecutor(max_workers=3) as executor:  # 以便在输出中观察待完成的期物
        to_do = []
        for cc in sorted(cc_list):
            # 排定可调用对象的执行时间，然后返回一个期物，表示这个待执行的操作
            future = executor.submit(download_one, cc)
            to_do.append(future)
            msg = 'Scheduled for {}: {}'
            print(msg.format(cc, future))

        results = []
        for future in futures.as_completed(to_do):  # as_compled函数在期物运行结束后产出期物
            res = future.result()  # 绝不会阻塞，因为futer由as_completed函数产出
            msg = '{} result: {!r}'
            print(msg.format(future, res))
            results.append(res)

    return len(list(res))  # 如果有线程抛出异常，异常会在这里抛出。这与隐式调用next()函数从迭代器中获取相应的返回值一样


if __name__ == "__main__":
    main(download_many)
