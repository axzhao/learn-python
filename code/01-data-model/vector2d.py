from math import hypot

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # __repr__ : 对象构造器的表达形式
    # __str__ : str()函数或print打印时调用，对用户更友好的表达形式
    # 如果一个对象没有__str__，解释器会使用__repr__代替
    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    # 自定义的实例总是被认为是真的，除非这个类实现了__bool__或者__len__
    # bool(x)先调用__bool__，如果不存在调用__len__，若返回0返回False，否则返回True
    def __bool__(self):
        return bool(abs(self))
        # 更加高效
        # return bool(self.x or self.y)

    # + 
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    # *
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

if __name__ == "__main__":
    v1 = Vector(2, 4)
    v2 = Vector(2, 1)
    print(v1+v2)

    v = Vector(3, 4)
    print(abs(v))
    print(v*3)
    print(abs(v*3))