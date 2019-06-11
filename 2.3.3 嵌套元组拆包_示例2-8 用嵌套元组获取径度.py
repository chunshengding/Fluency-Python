metro_areas = [
    ("Tokyo", "JP", 36.933, (35.689722, 139.691667)),
    ("Delhi NCR", "IN", 21.953, (28.613889, 77.2088789)),
    ("Mexico City", "MX", 36.933, (19.689722, -99.13333)),
    ("Sao Paulo", "BR", 16.649, (-23.547778, -46.635883))
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
# 把元组的最后一个元素拆包到由变量构成的元组里,获取了坐标
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))
