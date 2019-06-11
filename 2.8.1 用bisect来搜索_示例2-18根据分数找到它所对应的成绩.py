import bisect


def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    # bisect(breakpoints, score),在breakpoints里面搜索score的位置
    # bisect.bisect是查找该数值将会插入的位置并返回，而不会插入
    # 插入的结果是不会影响原有的排序
    # 还有一个用法,将1插入到data=[0,2,6,8],结果是不会影响原有的排序 bisect.insort(data,1)
    i = bisect.bisect(breakpoints, score)
    print(i,end=",")
    return grades[i]

r = [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
print()
print(r)
