#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

if __name__ == "__main__":

    # unpacking
    lax_coordinates = (33.9425, -118.408056)
    latitude, longitude = lax_coordinates # 元组拆包
    city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
    traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

    for passport in sorted(traveler_ids):
        print('%s/%s' % passport) # 拆包
        
    for country, _ in traveler_ids:
        print(country)

    a, b = 1, 2   
    b, a = a, b # 拆包
    print(b, a)

    divmod(20, 8)
    t = (20, 8)
    divmod(*t)
    quotient, remainder = divmod(*t)
    quotient, remainder

    a, b, *rest = range(5)
    a, b, *rest = range(2)
    a, *body, c, d = range(5)
    *head, b, c, d = range(5)

    metro_areas = [
        ('Tokyo','JP',36.933,(35.689722,139.691667)), 
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
        ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
        ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
        ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
    ]
    print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
    fmt = '{:15} | {:9.4f} | {:9.4f}'
    for name, cc, pop, (latitude, longitude) in metro_areas: 
        if longitude <= 0: 
            print(fmt.format(name, latitude, longitude))

    # namedtuple
    from collections import namedtuple
    City = namedtuple('City', 'name country population coordinates') 
    tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667)) 
    print(tokyo)
    print(tokyo.population)
    print(tokyo[1])
    print(City._fields) # _fields

    LatLong = namedtuple('LatLong', 'lat long')
    delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
    delhi = City._make(delhi_data) # _make
    delhi._asdict()
    for key, value in delhi._asdict().items(): # _asdict
        print(key + ':', value)