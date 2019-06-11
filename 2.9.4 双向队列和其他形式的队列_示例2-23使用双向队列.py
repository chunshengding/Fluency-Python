from collections import deque

# 创建一个10个元素的队列,设置队列大小,代表容纳多少个元素,这个数量一旦设定,不能修改
dq = deque(range(10), maxlen=10)
print(dq)  # deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
# 队列的旋转操作,接受一个参数n,当 n > 0 时,队列的最右边的n个元素会被移动到最左边,
# 当 n < 0 时,队列的最左边的n个元素会被移动到最右边
dq.rotate(3)
print(dq)  # deque([7, 8, 9, 0, 1, 2, 3, 4, 5, 6], maxlen=10)

dq.rotate(-4)
print(dq)  # deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], maxlen=10)

# 当试图对一个已满的队列,在头部做添加操作时,它尾部的元素会被删除
dq.appendleft(-1)
print(dq)  # deque([-1, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)

# 在尾部添加元素,会挤掉-1,1,2
dq.extend([11, 22, 33])
print(dq)  # deque([3, 4, 5, 6, 7, 8, 9, 11, 22, 33], maxlen=10)

# 把迭代器里面的元素逐个添加到双向列表的最左边
dq.extendleft([10, 20, 30, 40])
print(dq)  # deque([40, 30, 20, 10, 3, 4, 5, 6, 7, 8], maxlen=10)
