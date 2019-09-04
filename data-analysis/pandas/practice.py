#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


# %%


# %%


# %%


d = {"A": ["a", "b", "c", "d"],
     "B": ["z", "z", "z", "z"]}
df = pd.DataFrame(d, index=[('a', 'z'), ('b', 'z'), ('c', 'z'), ('d', 'z')])

uni = [tuple(r) for r in zip(df.A, df.B)]
# print(df.A.count())

# print(df.loc[('a','z')])
print(df[df.index.isin(uni).any()])
# df["C"] = df.apply(lambda x: 1 if x.index.isin(uni).any() else 0, axis = 1)
print(df)
# print(1 if df.loc[('a', 'z')].index.isin(uni).any() else 0)

# %%

d = {"A": ["a", "b", "b", "a"],
     "B": ["z", "z", "z", "z"],
     "C": [1, 2, 3, 4]}
df = pd.DataFrame(d)
df = df.drop_duplicates(["A", "B", "C"][:-1])
print(df)

# %%

d = {"A": ["a", "b", "b", "a"],
     "B": ["z", "z", "z", "z"],
     "C": [1, 2, 3, 4]}
df = pd.DataFrame(d)
print(list(zip(df.iloc[0, :], df.iloc[1, :], df.iloc[2, :])))

# %%

# head = [['x', 1, 1, 1], ['y', 1, 1, 1], ['z', 1, 2, 3]]
# df = pd.DataFrame(head)
# col = df[0]
# df.drop(0, axis=1, inplace=True)
# head = pd.DataFrame(df.values.T, index=df.columns, columns=col)


# body = [['a', 'V', '', ''], ['b', '', '', 'V'], ['c', '', '', '']]
# body = pd.DataFrame(body)
# col = df[0]
# df.drop(0, axis=1, inplace=True)
# body = pd.DataFrame(df.values.T, index=df.columns, columns=col)

axisX = [['x', 1, 1, 1, 1], ['y', 1, 1, 1, 1], ['z', 1, 2, 3, 4]]
axisX = pd.DataFrame(axisX)
col = axisX.columns
axisX.drop(0, axis=1, inplace=True)
axisX.columns = col[:-1]
# print(axisX)

df = [['a', 'V', 'V', '', ''], ['b', '', '', '', ''], ['c', '', '', '', 'V']]
df = pd.DataFrame(df)
axisY = df[0]
# print(axisY)
col = df.columns
df.drop(0, axis=1, inplace=True)
df.columns = col[:-1]
# print(df)
point = np.column_stack(np.where(df))
# print(point)

pointY = point[:, :1].ravel()
pointX = point[:, 1:].ravel()
# print(pointX)
# print(pointY)

xyz = [axisX[i].ravel() for i in pointX]
print(*xyz[0])
print([axisY[j] for j in pointY])


# print(axisY)
# print(df)

# df.drop(0, axis=1, inplace=True)
# point = np.column_stack(np.where(df[1:]))
# print(point)

# pointX = point[:,:1].ravel()
# pointY = point[:,1:].ravel()

# print([axisX[i] for i in pointX])
# print([axisY[j] for j in pointY])

# index = ['a', 'b', 'c']
# body = [['V', '', ''], ['', '', 'V'], ['', '', '']]
# value = np.column_stack(np.where(body))
# x = value[:,:1].ravel()
# y = value[:,1:].ravel()
# print([xyz[i] for i in y])
# print([index[j] for j in x])

# sc.stop()
# sc = SparkContext()
# sqlContext = HiveContext(sc)

# h = sqlContext.createDataFrame(head)
# b = sqlContext.createDataFrame(body)

# df = h.crossJoin(b)
# df.show()
# sc.stop()

# df = df3.\
#      join(df1, (df3.c1 == df1.c1) & (df3.c2 == df1.c2) & (df3.c3 == df1.c3), "inner").\
#      join(df2, (df3.p4 == df2.p4), "inner").\
#      select(lit(0).alias('id'), df3.c1, df3.c2, df3.c3, df3.p4, df1.id.alias("d1_id"), df2.id.alias("d2_id")).\
#      filter((df1.id > 0) & (df2.id > 0))
# df = df.withColumn("id", row_number().over(Window.partitionBy("id").orderBy("id")))

# print(df)
# col = df[0]
# df.drop(0, axis=1, inplace=True)
# dfT = pd.DataFrame(df.values.T, index=df.columns, columns=col)
# print(dfT)
# head = dfT.iloc[:,:3]
# body = df[3:]
# print(head)
# print(body)
# print(dfT.groupby(dfT.iloc[:,:3]).apply())
# print(dfT.iloc[:,3:])

# %%


# %%

d = [[1, 2, 3], [4, 5, 6]]
dd = pd.DataFrame(d)
print(dd)

# %%
