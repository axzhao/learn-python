#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


import numpy as np
import pandas as pd

# %%

""" groupby 对象： apply/ agg/ transform 

transform是为了保持结果的记录的行数与原始数据一致
transform会将一个函数应用到各个分组，然后将结果放置到合适的位置上。
如果各分组产生的是一个标量值，则该值就会被广播（broadcast）出去。

apply会将待处理的对象拆分成多个片段，然后对各片段调用传入的函数，
最后尝试将各片段组合到一起。

"""

df = pd.DataFrame({'A': 'a a b'.split(), 'B': [1, 2, 3], 'C': [4, 6, 5]})
df.groupby('A').apply(lambda x: x/x.sum())
df.groupby('A').apply(lambda x: x.max() - x.min())
df.groupby('A').transform(lambda x: x.max()-x.min())
df.groupby('A').apply(lambda x: x.C.max() - x.B.min())

df = pd.DataFrame(
    {'A': [1, 1, 2, 2], 'B': [1, 2, 3, 4], 'C': np.random.randn(4)})
df.groupby('A').agg('min')
df.groupby('A').agg(['min', 'max'])
df.groupby('A').B.agg(['min', 'max'])
df.groupby('A').agg({'B': ['min', 'max'], 'C': 'sum'})

df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar'],
                   'B': ['one', 'one', 'two', 'three', 'two', 'two'],
                   'C': [1, 5, 5, 2, 5, 5],
                   'D': [2.0, 5, 8, 1, 2, 9]})
df.groupby('A').transform(lambda x: ((x-x.mean())/x.std()))
df.groupby('A').transform(lambda x: x.max()-x.min())


df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar'],
                   'B': ['one', 'one', 'two', 'three', 'two', 'two'],
                   'C': [1, 5, 5, 2, 5, 5],
                   'D': [2.0, 5, 8, 1, 2, 9]})

a_means = df.groupby('A').mean().add_prefix('mean_')
pd.merge(df, a_means, left_on='A', right_index=True)
df.groupby('A').transform(np.mean)

# %%

""" series, dataframe 对象： map/ apply """

x = pd.Series([1, 2, 3], index=['one', 'two', 'three'])
y = pd.Series(['foo', 'bar', 'baz'], index=[1, 2, 3])
z = {1: 'A', 2: 'B', 3: 'C'}
x.map(y)
x.map(z)
s = pd.Series([1, 2, 3, np.nan])
s.map('this is a string {}'.format, na_action=None)
s.map('this is a string {}'.format, na_action='ignore')
x.map(lambda x: 2*x+1)
x.apply(lambda x: 2*x+1)

df = pd.DataFrame({'A': 'a a b'.split(), 'B': [1, 2, 3], 'C': [4, 6, 5]})
df.A.apply(lambda x: x+"haha")
