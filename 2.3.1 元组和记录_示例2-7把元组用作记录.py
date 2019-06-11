lax_coordinates = (33.9425, -188.408056)
# 这里是拆包赋值
city, year, pop, chg, area = ("Tokyo", 2003, 32450, 0.66, 8014)
traveler_ids = [("USA", '322989'), ("BRA", "CE34527"), ("ESP", 'XDA657878')]

for passport in traveler_ids:
    print("%s/%s" % passport)

# 这里进行拆包,第二个元素我们没有用,也可以用下面第二中方式
# for country, codes in traveler_ids:
#     print(country,codes)

# 这里进行拆包,第二个元素我们没有用,所以用 _ 下划线占位
for country, _ in traveler_ids:
    print(country)
