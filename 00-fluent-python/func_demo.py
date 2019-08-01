#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

if __name__ == "__main__":

    # map, filter, reduce 替代
    print(list(map(lambda x: x**2, range(3))))
    print([x ** 2 for x in range(3)])
    print(list(filter(lambda x: x % 2 == 0, range(3))))
    print([x for x in range(3) if x % 2 == 0])
    from functools import reduce
    print(reduce(lambda x, y: x + y, range(3)))
    print(sum(range(3)))

    # 内省
    class C:
        pass
    obj = C()
    def func(): pass
    print(sorted(set(dir(func)) - set(dir(obj))))

    # 参数
    def tag(name, *content, cls=None, **attrs):
        if cls is not None:
            attrs['class'] = cls
        if attrs:
            attr_str = ''.join(' %s="%s"' % (attr, value)
                               for attr, value in sorted(attrs.items()))
        else:
            attr_str = ''
        if content:
            return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, c, name) for c in content)
        else:
            return '<%s%s />' % (name, attr_str)

    print(tag('br'))
    print(tag('p', 'hello'))
    print(tag('p', 'hello', 'world'))
    print(tag('p', 'hello', id=33))
    print(tag('p', 'hello', cls='sidebar'))
    print(tag(content='testing', name="img"))
    my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
              'src': 'sunset.jpg', 'cls': 'framed'}
    print(tag(**my_tag))

    # 参数信息
    print(tag.__defaults__)
    print(tag.__code__)
    print(tag.__code__.co_varnames)
    print(tag.__code__.co_argcount)
    from inspect import signature
    sig = signature(tag)
    print(sig)
    for name, param in sig.parameters.items():
        print(param.kind, ':', name, '=', param.default)
