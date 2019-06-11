# 一种优雅的写法,不使用中间变量交换两个变量的值
a = 1
b = 2
b, a = a, b
print(a, b)

# *符号可以把一个迭代对象拆分作为函数的参数
# divmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)
result = divmod(20, 8)
print(result)

t = (20, 8)
result1 = divmod(*t)
print(result1)

q, r = divmod(*t)
print(q, r)

# 用*来处理剩下的元素
# 平行赋值
a, b, *rest = range(5)
print(a, b, rest)

a, b, *rest = range(3)
print(a, b, rest)

a, b, *rest = range(2)
print(a, b, rest)

# 在平行赋值中,*前缀只能用在一个变量名前面,但是这个变量名可以出现在赋值表达式的任意位置
a, *rest, b, c = range(5)
print(a, rest, b)

*rest, a, b, c = range(5)
print(rest, a, b)
