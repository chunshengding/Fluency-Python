import numpy

# 新建一维数组,0-11的整数
a = numpy.arange(12)
print(a)
type(a)
# 查看数组的维度,这里是一维的
print(a.shape)
# 把数组变成二维的
a.shape=3,4
print(a)
# 查看第二行
print(a[2])
# 查看第二行,第一列
print(a[2,1])

# 打印第一列
print(a[:,1])
# 把行和列交换
print(a.transpose())