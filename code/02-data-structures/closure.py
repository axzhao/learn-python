#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# 闭包
def f1():
    x = 88
    def f2():
        print(x)
    f2()

f1() # 88

# 工厂函数
def maker(n):
    def action(x):
        return x ** n # remember n
    return action

f = maker(2)
f(3)
f(4)

# 建议写法
def ff1():
    x = 99
    ff2(x)

def ff2(x):
    print(x)

ff1() # 88

# 嵌套作用域中的变量在嵌套的函数被调用时才进行查找，所以他们记录的是同样的值
def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x: i ** x)
        # acts.append(lambda x, i = i: i ** x) # remember current i
    return acts

acts = makeActions()
acts[0]
acts[0](2) # all are 4 ** 2


def tester(state):
    def nested(label):
        nonlocal state # 记住每一个tester的
        print(label, state) # remember state
        state += 1
    return nested

f = tester(0)
f('a')
f('b')


