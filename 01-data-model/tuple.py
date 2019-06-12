#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


# 元组作为记录用
def tuple1():
    """
    >>> lax_coordinates = (33.9425, -118.408056)
    >>> city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
    >>> traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
    >>> for passport in sorted(traveler_ids):
    ...     print('%s/%s' % passport)
    ... 
    BRA/CE342567
    ESP/XDA205856
    USA/31195855

    # 元组拆包

    >>> for country, _ in traveler_ids:
    ...     print(country)
    ... 
    USA
    BRA
    ESP

    >>> lax_coordinates = (33.9425, -118.408056)
    >>> latitude, longitude = lax_coordinates 

    >>> a, b = 1, 2
    >>> b, a = a, b
    >>> print('%d %d' % (a, b))
    2 1

    >>> divmod(20, 8)
    (2, 4)
    >>> t = (20, 8)
    >>> divmod(*t)
    (2, 4)
    >>> quotient, remainder = divmod(*t)
    >>> quotient, remainder
    (2, 4)

    # *args 平行赋值
    >>> a, b, *rest = range(5)
    >>> a, b, rest
    (0, 1, [2, 3, 4])
    >>> a, *body, c, d = range(5)
    >>> a, body, c, d 
    (0, [1, 2], 3, 4)

    # 嵌套元组拆包 (a, b, (c, d))
    >>> metro_areas = [('Tokey', 'JP', 1, (11, 111)), ('Delhi NCR', 'IN', 2, (22, 222))]
    >>> print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
                    |   lat.    |   long.  
    >>> fmt = '{:15} | {:9.4f} | {:9.4f}'
    >>> for name, cc, pop, (latitude, longitude) in metro_areas:
    ...     if longitude <= 0:
    ...             print(fmt.format(name, latitude, longitude))


    # 给tuple命名namedtuple
    >>> from collections import namedtuple
    >>> City = namedtuple('City', 'name country population coordinates')
    >>> tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
    >>> tokyo
    City(name='Tokyo', country='JP', population=36.933, coordinates=(35.689722, 139.691667))
    >>> tokyo.coordinates
    (35.689722, 139.691667)
    >>> tokyo[1]
    'JP'

    >>> City._fields
    ('name', 'country', 'population', 'coordinates')
    >>> LatLong = namedtuple('LatLong', 'lat long')
    >>> delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28, 77))
    >>> delhi = City._make(delhi_data)
    >>> delhi._asdict()
    OrderedDict([('name', 'Delhi NCR'), ('country', 'IN'), ('population', 21.935), ('coordinates', LatLong(lat=28, long=77))])
    >>> for key, value in delhi._asdict().items():
    ...     print(key + ':', value)
    ... 
    name: Delhi NCR
    country: IN
    population: 21.935
    coordinates: LatLong(lat=28, long=77)

    """