from math import hypot


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # 把对象用字符串的形式表达出来,以方便辨识,称为 字符串表示形式
    # __str__也可输出字符串表示形式,只想实现一个,那就实现__repr__,
    # 在python调用__str__时如果没有实现,解释器会去调用__repr__作为替代
    def __repr__(self):
        return "Vector(%r %r)" % (self.x, self.y)

    # 取模
    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        # 通过取模把他变为bool值
        return bool(abs(self))

    # 相加
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    # 相乘
    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)


v1=Vector(2,4)
v2=Vector(2,1)
print(v1+v2)
# Vector(4 5)

v=Vector(3,4)
print(abs(v))
# 5.0

print(v*3)
# Vector(9 12)
print(abs(v*3))
# 15.0

# 测试