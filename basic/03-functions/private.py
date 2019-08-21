#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

traceMe = False


def trace(*args):
    if traceMe:
        print('[' + ' '.join(map(str, args)) + ']')


# Private的参数在装饰发生前使用，并且作为一个封闭作用域引用保持，以用于onDecorator和onInstance中
# onDecorator的类参数在装饰时使用，并且作为一个封闭作用域引用保持，以便在实例构建时使用
# 包装的实例对象保存为onInstance中的一个实例属性，以便随后从类外部访问属性的时候使用。


# 带有slots的类不能把属性存储到一个dict中，然而，这里只是在onInstance层级依赖一个dict，而不是包装的实例中，
# 并且setattr和getattr应用于基于dict和slots的属性，所以装饰器应用于使用任何一种存储方案的类。
def Private(*privates):
    def onDecorator(aClass):
        class onInstance:
            def __init__(self, *args, **kwargs):
                self.wrapped = aClass(*args, **kwargs)

            def __getattr__(self, attr):
                trace('get', attr)
                if attr in privates:
                    raise TypeError('private attribute fetch: ' + attr)
                else:
                    return getattr(self.wrapped, attr)

            def __setattr__(self, attr, value):
                trace('set:', attr, value)
                if attr == 'wrapped':
                    self.__dict__[attr] = value  # avoid looping
                elif attr in privates:
                    raise TypeError('private attribute change: ' + attr)
                else:
                    setattr(self.wrapped, attr, value)

        return onInstance

    return onDecorator


if __name__ == "__main__":
    traceMe = True

    @Private('data', 'size')
    class Doubler:
        def __init__(self, label, start):
            self.label = label
            self.data = start

        def size(self):
            return len(self.data)

        def double(self):
            for i in range(self.size()):
                self.data[i] = self.data[i] * 2

        def display(self):
            print('%s => %s' % (self.label, self.data))

    x = Doubler('X is', [1, 2, 3])
    y = Doubler('Y is', [-10, -20, -30])
    print(x.label)
    x.display()
    x.double()
    x.display()
    print(y.label)
    y.display()
    y.label = 'Spam'
    y.double()
    y.display()

    # error
    """
    print(x.size())
    print(x.data)
    x.data = [1,1,1]
    x.size = lambda S:0
    print(y.data)
    print(y.size())
    """
