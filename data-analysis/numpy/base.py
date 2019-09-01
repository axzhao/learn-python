#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
NumPy: a multidimensional array object

ndarray: n-dimensional arrays of homogeneous data types
-- fixed size at creation
-- same data type

attributes of an ndarray object are:
-- ndarray.ndim：the number of axes (dimensions) of the array.
-- ndarray.shape：the dimensions of the array. 
-- ndarray.size：the total number of elements of the array. 
-- ndarray.dtype：an object describing the type of the elements in the array. 
-- ndarray.itemsize：the size in bytes of each element of the array. 
-- ndarray.data：the buffer containing the actual elements of the array. 


np.set_printoptions(threshold=sys.maxsize)


python3 -c "import numpy; numpy.info(numpy.add)"


array creation 
-- array, zeros, ones, empty, eye
-- arange, linespace, 
-- random

print("%d bytes" % (Z.size * Z.itemsize))

x[1,2,...] is equivalent to x[1,2,:,:,:],
x[...,3] to x[:,:,:,:,3] and
x[4,...,5,:] to x[4,:,:,5,:].

"""

#%%
""" numpy """


import numpy as np

print(np.version)
# print(np.__version__)
np.show_config()

print(0 * np.nan)
print(np.nan == np.nan)
print(np.inf > np.nan)
print(np.nan - np.nan)
print(np.nan in set([np.nan]))
print(0.3 == 3 * 0.1)

# python3 -c "import numpy; numpy.info(numpy.random.gamma)"


a = np.arange(1,10).reshape(3,3)
m = [[1,2,3],[4,5,6],[7,8,9]]
print(a[1][1] == m[1][1])
print(np.diag(a) == [m[i][i] for i in [0,1,2]])
print(np.sum(a, axis=1) == [sum(row) for row in m])

#%%
""" 生成函数 """

import numpy as np
# array, asarray
a = np.array([1,2,3], dtype=np.int) 
b = np.asarray(a) 
print(id(a) == id(b))
# ones, zeros, empty : num or ndarray
print(np.ones(2), np.ones_like(a))
print(np.zeros(2), np.zeros_like(b))
print(np.empty(2), np.empty_like(b)) # 未初始化
# eye, idnetity
print(np.eye(2))
print(np.identity(2))
# arange
print(np.arange(3), np.arange(0,3), np.arange(0,3,1))
# mershgrid
print(np.meshgrid(np.arange(3), np.arange(3,6)))
# where
print(np.where([[True, False], [True, True]],[[1, 2], [3, 4]],[[9, 8], [7, 6]]))
# in1e
print(np.in1d(np.arange(4), [1]))
# arange, linespace
print(np.arange(10, 30, 5))  # array([10, 15, 20, 25])
print(np.linspace(10, 30, 5))  # array([10., 15., 20., 25., 30.])
print(np.linspace(0, 2*np.pi, 100))
# fromfunction
b = np.fromfunction(lambda x,y: 10*x+y, (5, 4), dtype=int)
print(b[2, 3], b[0:5, 1], b[:, 1], b[1:3, :], b[-1])

# resize
a = np.arange(12).reshape(3,4)
print(a.reshape(2,6))
print(a)
a.reshape(3,4)
a.resize(2,6)
print(a)

#%%
""" 矩阵函数 """

print(np.diag(np.arange(9).reshape(3,3), k=-1)) # k为对角线上下移动参数
print(np.diag([1,2,3])) # 将一维数组转化为方阵（非对角线元素为0）
print(np.dot([2j, 3j], [2j, 3j])) # 点乘
print(np.trace(np.arange(6).reshape(2,3))) # 计算对角线元素的和


#%%
""" 排序, 集合函数 """

a = np.arange(3)
b = np.sort(a) # 返回副本
print(id(a) == id(b))
print(np.unique([1,1,2]))
a = np.array([1,3,4])
b = np.array([3,4,5])
print(np.intersect1d(a, b), np.union1d(a, b), np.setdiff1d(a,b), np.setxor1d(a,b))


#%%
""" 一元计算函数 """

# axis = i 按轴计算

l = [1,2,3,4,5]
print(np.abs([1j, 1,-1]), np.fabs([1,-1])) # fabs 计算绝对值非复数
print(np.mean(l), np.sum(l), np.cumsum(l), np.cumprod(l)) # 平均值，和，累加，累乘
print(np.std(l), np.var(l), np.max(l), np.min(l)) # 方差，标准差，最大，最小
print(np.argmax(l), np.argmin(l), np.any(l), np.all(l)) # 最大值索引，最小值索引，any，all
print(np.sqrt(l))  # 计算x^0.5
print(np.square(l)) # 计算x^2
print(np.exp(l)) # 计算e^x
print(np.log(np.e), np.log10(10), np.log2(4), np.log1p(np.e)) # 自然对数、底为10的log、底为2的log、底为(1+x)的log
print(np.sign(l)) # 符号
print(np.ceil([1.4,1.5,1.6]), np.floor([1.4,1.5,1.6]), np.rint([1.4,1.5,1.6])) 
print(np.modf([1.4, 1.5,1.6]))
print(np.isnan([np.nan, 1]))
print(np.isfinite([np.inf, np.nan, 1]), np.isinf([np.inf, np.nan, 1]))
print(np.cos([0, np.pi]), np.cosh([1, -1])) # sin, sinh, tan, tanh
print(np.arccos([1, -1]), np.arccosh([np.e])) # arcsin, arcsinh, arctan, arctanh
print(np.logical_not(np.arange(5) < 3))


#%%
""" 多元计算函数 """

print(np.add(np.arange(3), np.arange(3))) 
print(np.subtract(np.arange(3), np.arange(3)))
print(np.multiply(np.arange(3), np.arange(3)))
print(np.divide(np.arange(3), 2))
print(np.floor_divide(np.arange(3), 2))
print(np.power(np.arange(3), 2))
print(np.mod(np.arange(3), 2))
# fmax, fmin 忽略NaN
print(np.maximum(np.arange(3), np.array([np.nan, 1, 2])), np.fmax(np.arange(3), np.array([np.nan, 1, 2])))
print(np.minimum(np.arange(3), np.array([np.nan, 1, 2])), np.fmin(np.arange(3), np.array([np.nan, 1, 2])))
print(np.copysign(np.arange(3), [1,-1,1])) # 将参数2中的符号赋予参数1
print(np.greater(np.arange(3), 1)) # greater_equal, less, less_equal, equal, not_equal 
print(np.logical_and(np.arange(3), 1)) # logical_or, logical_xor
print(np.dot(np.ones((5,3)), np.ones((3,2))))

# ix_ 生成一个索引器，用于Fancy indexing(花式索引)
# ``a[np.ix_([1,3],[2,5])]`` returns the array``[[a[1,2] a[1,5]], [a[3,2] a[3,5]]]``
a = np.arange(10).reshape(2, 5)
ixgrid = np.ix_([0, 1], [2, 4])
print(a[ixgrid])

a = np.arange(12).reshape(3,4)
b1 = np.array([False,True,True])             # first dim selection
b2 = np.array([True,False,True,False])       # second dim selection
a[b1,:]                                   # selecting rows
a[b1]                                     # same thing
a[:,b2]                                   # selecting columns
a[b1,b2]                                  # a weird thing to do
a = np.array([2,3,4,5])
b = np.array([8,5,4])
c = np.array([5,4,6,8,3])
ax,bx,cx = np.ix_(a,b,c)
ax.shape, bx.shape, cx.shape
result = ax+bx*cx
result[3,2,4]
a[3]+b[2]*c[4]
def ufunc_reduce(ufct, *vectors):
   vs = np.ix_(*vectors)
   r = ufct.identity
   for v in vs:
       r = ufct(r,v)
   return r
ufunc_reduce(np.add,a,b,c)

#%%
""" 文件读写 

np.save(string, ndarray) 将ndarray保存到文件名为 [string].npy 的文件中（无压缩）
np.savez(string, ndarray1, ndarray2, ...) 将所有的ndarray压缩保存到文件名为[string].npy的文件中
np.savetxt(sring, ndarray, fmt, newline='\n') 将ndarray写入文件，格式为fmt
np.load(string) 读取文件名string的文件内容并转化为ndarray对象（或字典对象）
np.loadtxt(string, delimiter) 读取文件名string的文件内容，以delimiter为分隔符转化为ndarray

"""

#%%
""" 索引 切片 迭代 """

l = np.arange(12).reshape(3,4)
print(l[0], l[1:2], l[:], l[1:], l[:3])
print(l[l>2]) # ndarray[bool_ndarray]
print(l[l < 11], l < 11)
print(l[[1,2,0,0]], l[1,1], l[1][1]) # 选取

# ...
c = np.array([[[0,  1,  2], [10, 12, 13]],[[100, 101, 102],[110, 112, 113]]]) # (2, 2, 3)
print(c[1, ...]) # same as c[1,:,:] or c[1]
print(c[..., 2]) # same as c[:,:,2]

print([row for row in c])
print([row for row in c.ravel()])
print([row for row in c.flat])

#%%

""" Stacking And Aplit """

a = np.floor(10*np.random.random((2, 2)))
b = np.floor(10*np.random.random((2, 2)))
np.vstack((a, b))  # 垂直
np.hstack((a, b))  # 水平
np.column_stack((a, b))  # 水平
a[:, newaxis]  # 列增加一个维度
np.column_stack((a[:, newaxis], b[:, newaxis]))
np.hstack((a[:, newaxis], b[:, newaxis]))

np.r_[1:4, 0, 4]  # np.r_是按列连接矩阵，矩阵上下相加，要求列数相等，类似于pandas中的concat()
np.c_[1:4, 4:7, 7:10]  # np.c_是按行连接矩阵，矩阵左右相加，要求行数相等，类似于pandas中的merge()

a = np.floor(10*np.random.random((2, 12)))
np.hsplit(a, 3)         # Split a into 3
np.hsplit(a, (3, 4))    # Split a after the third and the fourth column


#%%

""" copies and views """

a = np.arange(12)
b = a            # no new object is created
b is a           # a and b are two names for the same ndarray object
b.shape = 3, 4    # changes the shape of a
a.shape
id(a)                           # id is a unique identifier of an object


c = a.view()
c is a
c.base is a                        # c is a view of the data owned by a
c.flags.owndata
c.shape = 2, 6                      # a's shape doesn't change
a.shape
c[0, 4] = 1234                      # a's data changes

s = a[:, 1:3]     # spaces added for clarity; could also be written "s = a[:,1:3]"
s[:] = 10           # s[:] is a view of s. Note the difference between s=10 and s[:]=10


d = a.copy()                          # a new array object with new data is created
d is a
d.base is a                           # d doesn't share anything with a
d[0, 0] = 9999

a = np.arange(int(1e8))
b = a[:100].copy()
del a  # the memory of ``a`` can be released.

#%%
""" random 常用函数 """

l = np.arange(5)
print(np.random.random((3,3,3)))
print(np.random.permutation(5))
print(np.random.shuffle(l), l)
print(np.random.rand(5)) # 产生int个均匀分布的样本值， 从给定的begin和end随机选取num个整数
print(np.random.randn(2,4)) # 生成一个N*M*...的正态分布（平均值为0，标准差为1）
print(np.random.normal(3, 2.5, size=(2, 4))) # 生成一个N*M*...的正态（高斯）分布的ndarray 
# print(np.random.beta()) # 产生beta分布的样本值，参数必须大于0 
# print(np.chisquare()) # 产生卡方分布的样本值
shape, scale = 2., 2.  # mean=4, std=2*sqrt(2)
print(np.random.gamma(shape, scale, 10))
print(np.random.uniform(-10,+10,10))


#%%
""" 时间 """

import numpy as np
# np.timedelta64
yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
today     = np.datetime64('today', 'D')
tomorrow  = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
print(np.arange('2016-07', '2016-08', dtype='datetime64[D]'))


#%%

""" index tricks """

a = np.arange(12)**2                       
i = np.array( [ 1,1,3,8,5 ] )              
a[i]                                      

j = np.array( [ [ 3, 4], [ 9, 7 ] ] )     
a[j]                                      

palette = np.array( [ [0,0,0],                # black
                      [255,0,0],              # red
                      [0,255,0],              # green
                      [0,0,255],              # blue
                      [255,255,255] ] )       # white
image = np.array( [ [ 0, 1, 2, 0 ],           # each value corresponds to a color in the palette
                    [ 0, 3, 4, 0 ]  ] )
palette[image]                                 # the (2,4,3) color image


a = np.arange(12).reshape(3,4)
i = np.array( [ [0,1], [1,2] ] )
j = np.array( [ [2,1], [3,3] ] )
a[i,j]                                          # i and j must have equal shape
a[i,2]
a[:,j]                                          # i.e., a[ : , j]
l = [i,j]
a[l]                                            # equivalent to a[i,j]
s = np.array( [i,j] )
a[s]                                       # not what we want
a[tuple(s)]                                # same as a[i,j]


time = np.linspace(20, 145, 5)                 # time scale
data = np.sin(np.arange(20)).reshape(5,4)      # 4 time-dependent series
ind = data.argmax(axis=0)                  # index of the maxima for each series
time_max = time[ind]                       # times corresponding to the maxima
data_max = data[ind, range(data.shape[1])] # => data[ind[0],0], data[ind[1],1]...
np.all(data_max == data.max(axis=0))
a = np.arange(5)
a[[1,3,4]] = 0
a = np.arange(5)
a[[0,0,2]]=[1,2,3]
a = np.arange(5)
a[[0,0,2]]+=1

#%%

import numpy as np
import matplotlib.pyplot as plt
def mandelbrot( h,w, maxit=20 ):
    """Returns an image of the Mandelbrot fractal of size (h,w)."""
    y,x = np.ogrid[ -1.4:1.4:h*1j, -2:0.8:w*1j ]
    c = x+y*1j
    z = c
    divtime = maxit + np.zeros(z.shape, dtype=int)

    for i in range(maxit):
        z = z**2 + c
        diverge = z*np.conj(z) > 2**2            # who is diverging
        div_now = diverge & (divtime==maxit)  # who is diverging now
        divtime[div_now] = i                  # note when
        z[diverge] = 2                        # avoid diverging too much

    return divtime
plt.imshow(mandelbrot(400,400))
plt.show()


#%%
""" Linear Algebra """

a = np.array([[1.0, 2.0], [3.0, 4.0]])
a.transpose()
np.linalg.inv(a)
u = np.eye(2) 
j = np.array([[0.0, -1.0], [1.0, 0.0]])
j @ j        # matrix product
np.trace(u)  # trace
y = np.array([[5.], [7.]])
np.linalg.solve(a, y)
np.linalg.eig(j)

#%%
""" hist and histogram """

# Build a vector of 10000 normal deviates with variance 0.5^2 and mean 2
loc , scale = 2, 0.5
v = np.random.normal(loc, scale, 10000)
plt.hist(v, bins=50, density=1)       
plt.show()

(n, bins) = np.histogram(v, bins=50, density=True)  
plt.plot(.5*(bins[1:]+bins[:-1]), n)
plt.show()

#%%
""" numpy - 100 """

# Create a 2d array with 1 on the border and 0 inside
Z = np.ones((10,10))
Z[1:-1,1:-1] = 0
print(Z)


# How to add a border (filled with 0's) around an existing array
Z = np.ones((5,5))
Z = np.pad(Z, pad_width=1, mode='constant', constant_values=0)
print(Z)

# Create a 5x5 matrix with values 1,2,3,4 just below the diagonal
Z = np.diag(1+np.arange(4),k=-1)
print(Z)

# Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element?
print(np.unravel_index(99,(6,7,8)))

# Normalize a 5x5 random matrix
Z = np.random.random((5,5))
Z = (Z - np.mean (Z)) / (np.std (Z))
print(Z)

# Create a custom dtype that describes a color as four unsigned bytes (RGBA)
color = np.dtype([("r", np.ubyte, 1), ("g", np.ubyte, 1), ("b", np.ubyte, 1), ("a", np.ubyte, 1)])

# Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)
Z = np.dot(np.ones((5,3)), np.ones((3,2))) # Z = np.ones((5,3)) @ np.ones((3,2))
print(Z)
A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 4]])
print(A * B)                       # elementwise product
print(A @ B)                       # matrix product, same A.dot(B)

# How to round away from zero a float array ? 
Z = np.random.uniform(-10,+10,10)
print (np.copysign(np.ceil(np.abs(Z)), Z))

# How to find common values between two arrays?
Z1 = np.random.randint(0,10,10)
Z2 = np.random.randint(0,10,10)
print(np.intersect1d(Z1,Z2))

# How to ignore all numpy warnings (not recommended)
with np.errstate(divide='ignore'):
    Z = np.ones(1) / 0


print(np.sqrt(-1), np.emath.sqrt(-1)) # nan, 1j




