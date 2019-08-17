#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


class C:
    """doc"""

    data = 'the class data'

    def __init__(self, instanceData):
        self.instanceData = instanceData

    def f(self):
        return 'the func data'

    @property
    def prop(self):
        return 'the property data'


if __name__ == "__main__":
    c = C("instanceData")
    print(C.__dict__)
    print(c.__dict__)  # vars(c)

    print(C.prop)
    print(c.prop)
    try:
        c.prop = 'foo'
    except AttributeError:
        print('AttributeError')
    c.__dict__['prop'] = 'foo'
    print(vars(c))
    print(c.prop)
    C.prop = 'baz'  # 覆盖特性，销毁特性对象
    print(c.prop)  # 现在获取的就是实例属性了，因为C.prop已经不是特性是，因此不会再覆盖obj.prop

    print(c.data)
    print(C.data)
    C.data = property(lambda self: 'the "data" prop value')  # 添加特性
    print(c.data)  # 特性
    del C.data  # 删除特性
    try:
        print(c.data)  # 恢复原样
    except AttributeError:
        print('AttributeError')
