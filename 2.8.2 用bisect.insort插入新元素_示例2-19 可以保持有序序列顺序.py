import bisect
import random

SIZE = 7
# seed() 方法改变随机数生成器的种子，可以在调用其他随机模块函数之前调用此函数
# 当我们设置相同的seed 种子值时，每次生成的随机数也相同，
# 如果不设置seed种子值时，在默认情况下随机种子来自系统时钟,则每次生成的随机数都会不一样
random.seed(1729)
my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE * 2)
    bisect.insort(my_list, new_item)
    print("%2d ->" % new_item, my_list)


# --------------------------------------------------
# bisect.bisect和bisect.insort示例

# data=[4,2,9,7]
# data.sort()
# print(data)
# # 插入的结果是不会影响原有的排序
# # bisect.insort(data,3)
# # print(data)
# # [2, 3, 4, 7, 9]
#
# # 查找该数值将会插入的位置并返回，而不会插入
# i=bisect.bisect(data,3)
# print(data)
# print(i)
