#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from collections import namedtuple

Result = namedtuple('Result', 'count average')

# 子生成器


def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        # main 函数发送数据到这里
        print("in averager, before yield")
        term = yield
        if term is None:  # 终止条件
            break
        total += term
        count += 1
        average = total/count

    print("in averager, return result")
    return Result(count, average)  # 返回的Result 会成为grouper函数中yield from表达式的值


# 委派生成器
def grouper(results, key):
     # 这个循环每次都会新建一个averager 实例，每个实例都是作为协程使用的生成器对象
    while True:
        print("in grouper, before yield from averager, key is ", key)
        results[key] = yield from averager()
        print("in grouper, after yield from, key is ", key)

# 调用方


def main(data):
    """
    外层for循环每次迭代会新建一个grouper实例，赋值给group变量，group是委派生成器
    调用next，预激委派生成器grouper，此时进入while True 循环，调用子生成器averager后，在yield from表达式处暂停
    内层for循环调用send，直接把值传给子生成器averager，同时，当前的grouper实例group 在yield from 表达式处暂停
    内层循环结束后，group实例依旧在yield from表达式处暂停，因此，grouper函数定义体中为results[key]赋值的语句还没有执行。
    如果外层for循环的末尾没有group.send(None)，那么averager子生成器永远不会终止，委派生成器group永远不会再次激活，因此永远不会为results[k]赋值
    外层fro循环重新迭代时会新建一个grouper实例，然后绑定到group变量上。前一个grouper实例，以及它创建的尚未终止的averager子生成器实例被垃圾回收程序回收

    这个试验想表明的关键一点是，如果子生成器不终止，委派生成器会在yield from表达式处永远暂停。如果是这样，程序会向前执行，因为yield from与yield一样把控制权转交给客户代码，
    即委派生成器的调用方了。显然，肯定有任务无法完成。
    """
    results = {}
    for key, values in data.items():
        # group 是调用grouper函数得到的生成器对象
        group = grouper(results, key)
        print("\ncreate group: ", group)
        next(group)  # 预激 group 协程。
        print("pre active group ok")
        for value in values:
            # 把各个value传给grouper 传入的值最终到达averager函数中；
            # grouper并不知道传入的是什么，同时grouper实例在yield from处暂停
            print("send to %r value %f now" % (group, value))
            group.send(value)
        # 把None传入groupper，传入的值最终到达averager函数中，导致当前实例终止。然后继续创建下一个实例。
        # 如果没有group.send(None)，那么averager子生成器永远不会终止，委派生成器也永远不会在此激活，也就不会为result[key]赋值
        print("send to %r none" % group)
        group.send(None)
    print("report result: ")
    report(results)


# 输出报告
def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print('{:2} {:5} averaging {:.2f}{}'.format(
            result.count, group, result.average, unit))


data = {
    'girls;kg': [40, 41, 42, 43, 44, 54],
    'girls;m': [1.5, 1.6, 1.8, 1.5, 1.45, 1.6],
    'boys;kg': [50, 51, 62, 53, 54, 54],
    'boys;m': [1.6, 1.8, 1.8, 1.7, 1.55, 1.6],
}

if __name__ == '__main__':
    main(data)
