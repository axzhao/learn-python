#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import numpy as np
import pandas as pd

""" DataFrame

a 2-dimensional lableled data structure with columns of potentially different types.

input data type:
Dict of 1D ndarrays, lists, dicts, or Series
2-D numpy.ndarray
Structured or record ndarray
A Series
Another DataFrame

index - row labels, columns - column labels
if pass an index and/or columns, a dict of Series plus a specific index will discard all data not matching up to the passed index.
if axis labels are not passed, the will be constructed from the input data based on common sense rules.

"""

""" From dict of Series or dicts """

d = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
     'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
pd.DataFrame(d, index=['d', 'b', 'a'])
pd.DataFrame(d, index=['d', 'b', 'a'], columns=['two', 'three'])
df.index
df.columns

""" From dict of ndarrays / list """

# The ndarrays must all be the same length.
d = {'one': [1., 2., 3., 4.],
     'two': [4., 3., 2., 1.]}
pd.DataFrame(d)
pd.DataFrame(d, index=['a', 'b', 'c', 'd'])

""" From structured or record array """

data = np.zeros((2, ), dtype=[('A', 'i4'), ('B', 'f4'), ('C', 'a10')])
data[:] = [(1, 2., 'Hello'), (2, 3., "World")]
pd.DataFrame(data)
pd.DataFrame(data, index=['first', 'second'])
pd.DataFrame(data, columns=['C', 'A', 'B'])

""" From a list of dicts """

data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
pd.DataFrame(data2)
pd.DataFrame(data2, index=['first', 'second'])
pd.DataFrame(data2, columns=['a', 'b'])

""" From a dict of tuples """

pd.DataFrame({('a', 'b'): {('A', 'B'): 1, ('A', 'C'): 2},
              ('a', 'a'): {('A', 'C'): 3, ('A', 'B'): 4},
              ('a', 'c'): {('A', 'B'): 5, ('A', 'C'): 6},
              ('b', 'a'): {('A', 'C'): 7, ('A', 'B'): 8},
              ('b', 'b'): {('A', 'D'): 9, ('A', 'B'): 10}})

""" From a Series """

df = pd.DataFrame(np.random.randn(5, 3),
                  index=['a', 'c', 'e', 'f', 'h'],
                  columns=['one', 'two', 'three'])

""" Alternate constructors """

# columns by default
pd.DataFrame.from_dict(dict([('A', [1, 2, 3]), ('B', [4, 5, 6])]))
pd.DataFrame.from_dict(dict([('A', [1, 2, 3]), ('B', [4, 5, 6])]),
                       orient='index', columns=['one', 'two', 'three'])

pd.DataFrame.from_records(data, index='C')

""" column selection, additon, deletion """

df['one']
df['three'] = df['one'] * df['two']
df['flag'] = df['one'] > 2
del df['two']
three = df.pop('three')
df['foo'] = 'bar'
df['one_trunc'] = df['one'][:2]
df.insert(1, 'bar', df['one'])

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

""" indexing / selection """

df.loc['b']
df.iloc[2]

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
