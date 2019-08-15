#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from collections import abc

import keyword


class FrozenJSON:
    """一个只读接口，使用属性表示法访问JSON类对象
    
    使用__new__代替 build方法
    """
    
    def __new__(cls, arg):
        if isinstance(arg, abc.Mapping):
            return super().__new__(cls)
        elif isinstance(arg, abc.MutableSequence):  # 数据源是JSON格式，而在JSON中，只有字典和列表是集合类型
            return [cls(item) for item in arg]
        else:
            return arg

    def __init__(self, mapping):
        # way 1: 没有为Python关键字的属性做特殊处理。
        # self.__data = dict(mapping)  # 副本
        # way 2
        self.__data = {}
        for key, value in mapping.items():
            if keyword.iskeyword(key):
                key += '_'
            if key.isidentifier():
                pass
            self.__data[key] = value

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            # self.__data[name] 可能抛出KeyError异常，应该处理
            # return FrozenJSON.build(self.__data[name])
            return FrozenJSON(self.__data[name])



    # @classmethod
    # def build(cls, obj):
    #     if isinstance(obj, abc.Mapping):
    #         return cls(obj)
    #     elif isinstance(obj, abc.MutableSequence):  # 数据源是JSON格式，而在JSON中，只有字典和列表是集合类型
    #         return [cls.build(item) for item in obj]
    #     else:
    #         return obj
