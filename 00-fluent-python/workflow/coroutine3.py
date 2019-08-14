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
        term = yield  # main函数中的客户代码发送的各个值绑定到这里term变量上
        if term is None:  # 如果没有，使用yield from 调用这个协程的生成器会永远阻塞
            break
        total += term
        count += 1
        average = total/count
        return Result(count, average)  # 返回的result会成为grouper函数中yield from表达式的值

# 委派生成器


def grouper(results, key):
    while True:  # 每次新建一个averager实例，每个实例都是作为协程使用的生成器对象
        # grouper发送的每个值都会经由 yield from 处理，通过管道传给averager实例
        results[key] = yield from averager()

# 客户端代码，即调用方


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
        group = grouper(results, key)
        next(group)  # 预激group协程
        for value in values:
            group.send(value)
        # 重要 把None传入grouper，导致当前的averager实例终止，也让grouper继续运行，再创建一个averager实例，处理下一组值
        group.send(None)
    # print(results) # 如果要调试，去掉注释
    report(results)

# 输出报告


def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print('{:2} {:5} averaging {:.2f}{}'.format(
            result.count, group, result.average, unit))


data = {
    'girls;kg': [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
    'girls;m': [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
    'boys;kg': [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
    'boys;m': [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
}

if __name__ == '__main__':
    main(data)
