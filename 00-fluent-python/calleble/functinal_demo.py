#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from collections import namedtuple
if __name__ == "__main__":
    from functools import reduce
    from operator import mul

    def fact(n):
        # return reduce(lambda a, b: a*b, range(1, n+1))
        return reduce(mul, range(1, n+1))

    metro_data = [
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
        ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
        ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
        ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
    ]

    from operator import itemgetter
    # itemgetter(1) 的作用与 lambda fields: fields[1] 一样：创建一个接受集合的函数，返回索引位 1 上的元素。
    for city in sorted(metro_data, key=itemgetter(1)):
        print(city)

    cc_name = itemgetter(1, 0)
    for city in metro_data:
        print(cc_name(city))

    LatLong = namedtuple('LatLong', 'lat long')
    Metropolis = namedtuple('Metropolis', 'name cc pop coord')
    metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long))
                   for name, cc, pop, (lat, long) in metro_data]
    print(metro_areas[0])
    Metropolis(name='Tokyo', cc='JP', pop=36.933, coord=LatLong(lat=35.689722,
                                                                long=139.691667))
    print(metro_areas[0].coord.lat)
    from operator import attrgetter
    name_lat = attrgetter('name', 'coord.lat')
    for city in sorted(metro_areas, key=attrgetter('coord.lat')):
        print(name_lat(city))

    from operator import methodcaller
    s = 'The time has come'
    upcase = methodcaller('upper')
    print(upcase(s))  # str.upper(s)
    # methodcaller 还可以冻结某些参数，也就是部分应用（partial application）
    hiphenate = methodcaller('replace', ' ', '-')
    print(hiphenate(s))

    from operator import mul
    from functools import partial
    triple = partial(mul, 3)
    print(triple(7))
    print(list(map(triple, range(1, 10))))
