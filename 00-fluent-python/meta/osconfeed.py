#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""

导入JSON数据

    >>> from osconfeed import *
    >>> feed = load()
    >>> sorted(feed['Schedule'].keys())
    ['conferences', 'events', 'speakers', 'venues']
    >>> for key, value in sorted(feed['Schedule'].items()):
    ...     print('{:3} {}'.format(len(value), key))
    ... 
    1 conferences
    1 events
    1 speakers
    1 venues
    >>> feed['Schedule']['speakers'][-1]['name']
    'Robert Lefkowitz'

使用obj.attr方式访问

    >>> from explore import *
    >>> feed = FrozenJSON(feed)
    >>> feed.Schedule
    <explore.FrozenJSON object at 0x10752e0f0>
    >>> feed.Schedule.speakers[-1].name
    'Robert Lefkowitz'
    
建立快速索引方式
    
    >>> import shelve
    >>> db = shelve.open(DB_NAME)
    >>> if CONFERENCE not in db: load_db(db)
    >>> DbRecord.set_db(db)  
    >>> event = DbRecord.fetch('event.33950')  
    >>> event  
    <Event 'There *Will* Be Bugs'>
    >>> event.venue 
    <DbRecord serial='venue.1449'>
    >>> event.venue.name  
    'Portland 251'
    >>> for spkr in event.speakers:  
    ...     print('{0.serial}: {0.name}'.format(spkr))
    ...
    speaker.3471: Anna Martelli Ravenscroft
    speaker.5199: Alex Martelli
    >>> db.close()


"""

import inspect
import osconfeed
import keyword
from collections import abc
from urllib.request import urlopen
import warnings
import os
import json

URL = 'http://www/oreilly.com/pub/sc/osconfeed'
JSON = 'osconfeed.json'


def load():
    """1. 加载JSON数据"""
    data_file = os.path.join(os.getcwd(), JSON)
    if not os.path.exists(data_file):
        msg = 'downloading {} to {}'.format(URL, JSON)
        warnings.warn(msg)
        with urlopen(URL) as remote, open(JSON, 'wb') as local:
            local.write(remote.read())
    with open(JSON) as fp:
        return json.load(fp)


class FrozenJSON:
    """2. 一个只读接口，使用属性表示法访问JSON类对象

    使用__new__代替 build方法

    一个近似字典的类常用：AttrDict，快速创建嵌套的映射：addict
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
            if keyword.iskeyword(key):  # 是否是python的关键字
                key += '_'
            if key.isidentifier():  # 是否是python的标识符
                pass
            self.__data[key] = value

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            # self.__data[name] 可能抛出KeyError异常，应该处理抛出AttributeError，因为这才是getattr应该抛出的异常种类
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


DB_NAME = 'schedule_db'
CONFERENCE = 'conference.115'


class Record:
    """3. shelve.Shelf建立快速访问

    FrozenJSON类要递归转换嵌套的映射和列表，而Record类不需要这样做，
    因为转换好的数据集中没有嵌套的映射和列表，记录中只有字符串整数字符串列表和整数列表

    Python标准库中 至少有两个与Record类似的类，其实例可以有任意哥属性，由传给构造方法的关键字构建
    multiprocessing.Namespace类
    argparse.Namespace类

    这里自己实现Record是为了说明一个重要的做法：在__init__方法中更新实例的__dict__属性
    """

    def __init__(self, **kwargs):
        # 对象的dunder-dict属性中存储着对象的属性，前提是类中没有声明dunder-slots属性
        self.__dict__.update(kwargs)

    def __eq__(self, other):
        if isinstance(other, Record):
            return self.__dict__ == other.__dict__
        else:
            return NotImplemented


class MissingDatabaseError(RuntimeError):
    """需要数据库但没有指定数据库时抛出。"""


class DbRecord(Record):
    """
    __db设为私有类属性，然后定义了普通的读值方法和设值方法，以防不小心覆盖__db属性的值。
    基于一个重要的原因，没有使用特性去管理__db属性，特性是用于管理实例属性的类属性。
    """

    __db = None

    @staticmethod
    def set_db(db):
        DbRecord.__db = db

    @staticmethod
    def get_db():
        return DbRecord.__db

    @classmethod
    def fetch(cls, ident):
        db = cls.get_db()
        try:
            return db[ident]
        except TypeError:
            if db is None:
                msg = "database not set; call '{}.set_db(my_db)'"
                raise MissingDatabaseError(msg.format(cls.__name__))
            else:
                raise  # 重新抛出TypeError异常

    def __repr__(self):
        if hasattr(self, 'serial'):
            cls_name = self.__class__.__name__
            return '<{} serial={!r}>'.format(cls_name, self.serial)
        else:
            return super().__repr__()


class Event(DbRecord):
    """4. 使用特性获取链接记录"""

    @property
    def venue(self):
        key = 'venue.{}'.format(self.venue_serial)
        return self.__class__.fetch(key)

    @property
    def speakers(self):
        if not hasattr(self, '_speaker_objs'):
            spkr_serials = self.__dict__['speakers']  # 使用__dict__防止无限递归
            # 为什么不实用self.fetch(key)呢。哪怕只有一个事件记录有名为fetch的键，那么在那个Event实例中，
            fetch = self.__class__.fetch
            # self.fetch获取的是fetch字段的值，而不是Event继承来自DbRecrod的fetch类方法
            self._speaker_objs = [fetch('speaker.{}'.format(key))
                                  for key in spkr_serials]
        return self._speaker_objs

    def __repr__(self):
        if hasattr(self, 'name'):
            cls_name = self.__class__.__name__
            return '<{} {!r}>'.format(cls_name, getattr(self, 'name'))
        else:
            return super().__repr__()


def load_db(db):
    raw_data = load()
    warnings.warn('loading ' + DB_NAME)
    for collection, rec_list in raw_data['Schedule'].items():
        record_type = collection[:-1]
        cls_name = record_type.capitalize()
        cls = globals().get(cls_name, DbRecord)
        if inspect.isclass(cls) and issubclass(cls, DbRecord):
            factory = cls
        else:
            factory = DbRecord
        for record in rec_list:
            key = '{}.{}'.format(record_type, record['serial'])
            record['serial'] = key
            db[key] = factory(**record)
