#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


print(id(globals()), id(locals()), id(vars()), end='\n')
varLocals = locals()
varLocals['HAHA'] = "haha"
print(globals()['HAHA'], vars()['HAHA'])


class C:
    def func(self):
        self.var = "var"
        print(id(globals()), globals(),   end='\n')
        print(id(locals()), locals(),  end='\n')
        print(id(vars()), vars(),   end='\n')
        print(vars(self), end='\n')


if __name__ == "__main__":

    c = C()
    c.func()

    var = "var"
    # 返回当前全局符号表，是其所在模块, 而不是调用模块.
    print(id(globals()), globals(),  end='\n')
    # 局部符号表， locals() 字典不应该被修改; 在解释器中对修改行为可能对 local 值或者自由变量无效.
    print(id(locals()), locals(),  end='\n')
    # 返回 __dict__ 属性, 比如模块, 类, 实例, 或者其他 带有 __dict__ 属性的 object.
    # vars() 如果不传参数, 那么作用与 locals() 一样
    print(id(vars()), vars(),   end='\n')
    print(id(vars(c)), vars(c),   end='\n')
