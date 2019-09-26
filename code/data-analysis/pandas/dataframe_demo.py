#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import numpy as np
import pandas as pd

""" DataFrame

a 2-dimensional lableled data structure with columns of potentially different types.
index - row labels
columns - column labels

"""

""" 创建 """

d = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
     'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
pd.DataFrame(d, index=['d', 'b', 'a'])
pd.DataFrame(d, index=['d', 'b', 'a'], columns=['two', 'three'])
df.index
df.columns

# The ndarrays must all be the same length.
d = {'one': [1., 2., 3., 4.],
     'two': [4., 3., 2., 1.]}
pd.DataFrame(d)
pd.DataFrame(d, index=['a', 'b', 'c', 'd'])

data = np.zeros((2, ), dtype=[('A', 'i4'), ('B', 'f4'), ('C', 'a10')])
data[:] = [(1, 2., 'Hello'), (2, 3., "World")]
pd.DataFrame(data)
pd.DataFrame(data, index=['first', 'second'])
pd.DataFrame(data, columns=['C', 'A', 'B'])

data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
pd.DataFrame(data2)
pd.DataFrame(data2, index=['first', 'second'])
pd.DataFrame(data2, columns=['a', 'b'])

pd.DataFrame({('a', 'b'): {('A', 'B'): 1, ('A', 'C'): 2},
              ('a', 'a'): {('A', 'C'): 3, ('A', 'B'): 4},
              ('a', 'c'): {('A', 'B'): 5, ('A', 'C'): 6},
              ('b', 'a'): {('A', 'C'): 7, ('A', 'B'): 8},
              ('b', 'b'): {('A', 'D'): 9, ('A', 'B'): 10}})

pd.DataFrame(np.random.randn(5, 3),
             index=['a', 'c', 'e', 'f', 'h'],
             columns=['one', 'two', 'three'])

""" 结构 """

pd.DataFrame.from_dict(dict([('A', [1, 2, 3]), ('B', [4, 5, 6])]))
pd.DataFrame.from_dict(dict([('A', [1, 2, 3]), ('B', [4, 5, 6])]),
                       orient='index', columns=['one', 'two', 'three'])
pd.DataFrame.from_records(data, index='C')

df['one']
df['three'] = df['one'] * df['two']
df['flag'] = df['one'] > 2
del df['two']
three = df.pop('three')
df['foo'] = 'bar'
df['one_trunc'] = df['one'][:2]
df.insert(1, 'bar', df['one'])

df.loc['b']
df.iloc[2]

""" assigning new columns in method chains """

# assign always returns a copy of the data, leaving the original DataFrame untouched.
iris = pd.read_csv('data/iris.data')
iris.head()
(iris.assign(sepal_ratio=iris['SepalWidth'] / iris['SepalLength']).head())
iris.assign(sepal_ratio=lambda x: (x['SepalWidth'] / x['SepalLength'])).head()
(iris.query('SepalLength > 5').assign(
    SepalRatio=lambda x: x.SepalWidth / x.SepalLength,
    PetalRatio=lambda x: x.PetalWidth / x.PetalLength
).plot(kind='scatter', x='SepalRatio', y='PetalRatio'))

dfa = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
dfa.assign(C=lambda x: x['A'] + x['B'], D=lambda x: x['A'] + x['C'])

dependent = pd.DataFrame({"A": [1, 1, 1]})
(dependent.assign(A=lambda x: x['A'] + 1).assign(B=lambda x: x['A'] + 2))


""" data alignment and artihmetic """

# Data alignment between DataFrame objects automatically align on both the columns and the index (row labels).
# Again, the resulting object will have the union of the column and row labels.
df = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])
df2 = pd.DataFrame(np.random.randn(7, 3), columns=['A', 'B', 'C'])
df + df2
# When doing an operation between DataFrame and Series, the default behavior is to align the Series index on the DataFrame columns, thus broadcasting row-wise.
df - df.iloc[0]
# In the special case of working with time series data, if the DataFrame index contains dates, the broadcasting will be column-wise:
index = pd.date_range('1/1/2000', periods=8)
df = pd.DataFrame(np.random.randn(8, 3), index=index, columns=list('ABC'))
type(df['A'])
df - df['A']  # deprecated, use df.sub(df['A'], axis=0)
df.sub(df['A'], axis=0)

df * 5 + 2
1 / df
df ** 4


df1 = pd.DataFrame({'a': [1, 0, 1], 'b': [0, 1, 1]}, dtype=bool)
df2 = pd.DataFrame({'a': [0, 1, 1], 'b': [1, 1, 0]}, dtype=bool)
df1 & df2
df1 | df2
df1 ^ df2
-df1

""" Transposing """

df[:5].T

""" DataFrame interoperability with NumPy functions """

np.exp(df)
np.asarray(df)

ser1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
ser2 = pd.Series([1, 3, 5], index=['b', 'a', 'c'])
ser3 = pd.Series([2, 4, 6], index=['b', 'c', 'd'])
np.remainder(ser1, ser2)  # ser1 % ser2
np.remainder(ser1, ser3)


""" viewing data """

df.head()
df.tail(3)
df.index
df.columns
df.to_numpy()
df.describe()
df.T
df.sort_index(axis=1, ascending=False)
df.sort_values(by='B')

baseball = pd.read_csv('data/baseball.csv')
print(baseball)
baseball.info()
print(baseball.iloc[-20:, :12].to_string())
pd.DataFrame(np.random.randn(3, 12))
pd.set_option('display.width', 40)  # default is 80
pd.DataFrame(np.random.randn(3, 12))

datafile = {'filename': ['filename_01', 'filename_02'],
            'path': ["media/user_name/storage/folder_01/filename_01",
                     "media/user_name/storage/folder_02/filename_02"]}

pd.set_option('display.max_colwidth', 30)
pd.DataFrame(datafile)
pd.set_option('display.max_colwidth', 100)
pd.DataFrame(datafile)



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
