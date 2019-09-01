#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


from pyspark.storagelevel import StorageLevel
from pyspark import SparkConf, SparkContext
sc = SparkContext()

# %%

""" 转换运算 """

intRDD = sc.parallelize([3, 1, 2, 5, 5])
stringRDD = sc.parallelize(['Apple', 'Orange', 'Grape', 'Banana', 'Apple'])

print(intRDD.collect())
print(stringRDD.collect())
print(intRDD.map(lambda x: x+1).collect())
print(intRDD.filter(lambda x: x < 3).collect())
print(intRDD.distinct().collect())

subRDD = intRDD.randomSplit([0.4, 0.6])
print(len(subRDD))
print(subRDD[0].collect())
print(subRDD[1].collect())

groupByRDD = intRDD.groupBy(lambda x: x % 2)
print(sorted([(x, sorted(y)) for (x, y) in groupByRDD.collect()]))

intRDD1 = sc.parallelize([3, 1, 2, 5, 5])
intRDD2 = sc.parallelize([5, 6])
intRDD3 = sc.parallelize([2, 7])

print(intRDD1.union(intRDD2).union(intRDD3).collect())
print(intRDD1.intersection(intRDD2).collect())
print(intRDD1.subtract(intRDD2).collect())
print(intRDD1.cartesian(intRDD2).collect())

# 一个JOB
strRDD = sc.parallelize(["cat", "dog", "lion", "monkey", "mouse"])
# 第一个 Map 操作将 RDD 里的各个元素进行映射, RDD 的各个数据元素之间不存在依赖,可以在集群的各个内存中独立计算,也就是并行化
rdd1 = strRDD.map(lambda x: (x[0], x))
# 第二个 groupby 之后的 Map 操作,为了计算相同 key 下的元素个数,需要把相同 key 的元素聚集到同一个 partition 下,所以造成了数据在内存中的重新分布,即 shuffle 操作.
# shuffle 操作是 spark 中最耗时的操作,应尽量避免不必要的 shuffle.
rdd2 = rdd1.groupBy(lambda x: x[0]).map(lambda x: (x[0], len(x[1])))
print(rdd2.collect())


# %%

""" 动作运算 """

intRDD = sc.parallelize([3, 1, 2, 5, 5])
print(intRDD.first())
print(intRDD.take(2))
print(intRDD.takeOrdered(3))
print(intRDD.takeOrdered(3, lambda x: -x))


print(intRDD.stats())  # 统计
print(intRDD.min())
print(intRDD.max())
print(intRDD.stdev())  # 标准差
print(intRDD.count())
print(intRDD.sum())
print(intRDD.mean())  # 平均
# %%

""" Key-Value 转换运算 

虽然RDD中是以键值对形式存在，但是本质上还是一个二元组
"""

kvRDD1 = sc.parallelize([(3, 4), (3, 6), (5, 6), (1, 2)])
print(kvRDD1.keys().collect())
print(kvRDD1.values().collect())
print(kvRDD1.filter(lambda x: x[0] < 5).collect())
print(kvRDD1.filter(lambda x: x[1] < 5).collect())
print(kvRDD1.mapValues(lambda x: x**2).collect())
print(kvRDD1.sortByKey().collect())
print(kvRDD1.sortByKey(True).collect())
print(kvRDD1.sortByKey(False).collect())
print(kvRDD1.reduceByKey(lambda x, y: x+y).collect())  # 对具有相同key值的数据进行合并


kvRDD1 = sc.parallelize([(3, 4), (3, 6), (5, 6), (1, 2)])
kvRDD2 = sc.parallelize([(3, 8)])
print(kvRDD1.join(kvRDD2).collect())
print(kvRDD1.leftOuterJoin(kvRDD2).collect())
print(kvRDD1.rightOuterJoin(kvRDD2).collect())
print(kvRDD1.subtractByKey(kvRDD2).collect())


# %%

""" Key-Value 动作运算 """

kvRDD1 = sc.parallelize([(3, 4), (3, 6), (5, 6), (1, 2)])
kvRDD2 = sc.parallelize([(3, 8)])

print(kvRDD1.first())
print(kvRDD1.take(2))
print(kvRDD1.first()[0])
print(kvRDD1.first()[1])
print(kvRDD1.countByKey().collect())
print(kvRDD1.lookup(3))

# %%

""" 持久化操作 """

kvRDD1.persist()
kvRDD1.unpersist()
