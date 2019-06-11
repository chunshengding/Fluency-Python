from collections import namedtuple
# 第一个参数是类名,第二个参数是类的各个字段的名字,可以是由数个字符串组成的可迭代对象,也可以是由空格分隔的字段名组成的字符串
City=namedtuple("City1","name country population coordinates")
tokyo=City("Tokyo","JP",36.933, (35.689722, 139.691667))
print(tokyo)
# 可以通过字段名或位置获取字段信息
print(tokyo.population,tokyo.coordinates,tokyo[1])