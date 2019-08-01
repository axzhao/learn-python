#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

if __name__ == "__main__":
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
