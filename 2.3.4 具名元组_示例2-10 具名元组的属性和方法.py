from collections import namedtuple

# 第一个参数是类名,第二个参数是类的各个字段的名字,可以是由数个字符串组成的可迭代对象,也可以是由空格分隔的字段名组成的字符串
City = namedtuple("City1", "name country population coordinates")
tokyo = City("Tokyo", "JP", 36.933, (35.689722, 139.691667))
print(tokyo)
# 可以通过字段名或位置获取字段信息
print(tokyo.population, tokyo.coordinates, tokyo[1])

print("-" * 50)
LatLong = namedtuple("LatLong", "lat long")
delhi_data = ("Delhi NCR", "IN", 21.953, LatLong(28.613889, 77.2088789))
# _make 通过接受一个可以迭代对象来生成这个类的一个实例,它的作用和City(*delhi_data)是一样的
delhi = City._make(delhi_data)
# _asdict() 可以把具名元组以OrderedDict的形式返回,我们可以利用他把元组里面的信息友好的显示出来
print(delhi._asdict())

delhi1 = City(*delhi_data)
print(delhi1._asdict())

print("-" * 50)
for key, value in delhi._asdict().items():
    print(key + " : ", value)
