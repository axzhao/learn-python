#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

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

    # 框架和 IDE 等工具可以使用这些信息验证代码。Python 3 的另一个特性——函数注解——增进了这些信息的用途
    import inspect
    sig = inspect.signature(tag)
    my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
              'src': 'sunset.jpg', 'cls': 'framed'}
    bound_args = sig.bind(**my_tag)
    print(bound_args)
    for name, value in bound_args.arguments.items():
        print(name, '=', value)
    attrs = {'title': 'Sunset Boulevard', 'src': 'sunset.jpg'}
    del my_tag['name']
    bound_args = sig.bind(**my_tag)

    # 函数注解
    def clip(text: str, max_len: 'int > 0' = 80) -> str:
        """在max_len前面或后面的第一个空格处截断文本
        """
        end = None
        if len(text) > max_len:
            space_before = text.rfind(' ', 0, max_len)
            if space_before >= 0:
                end = space_before
            else:
                space_after = text.rfind(' ', max_len)
                if space_after >= 0:
                    end = space_after
        if end is None:
            end = len(text)
        return text[:end].rstrip()

    print(clip.__annotations__)
    from inspect import signature
    sig = signature(clip)
    print(sig.return_annotation)
    for param in sig.parameters.values():
        note = repr(param.annotation).ljust(13)
        print(note, ':', param.name, '=', param.default)
