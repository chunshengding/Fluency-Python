import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'


def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * '  |'
        print(ROW_FMT.format(needle, position, offset))


if __name__ == '__main__':

    # bisect 模块，用于维护有序列表。bisect模块实现了一个算法用于插入元素到有序列表。在一些情况下，
    # 这比反复排序列表或构造一个大的列表再排序的效率更高。Bisect 是二分法的意思，这里使用二分法来排序，
    # 它会将一个元素插入到一个有序列表的合适位置，这使得不需要每次调用sort的方式维护有序列表。
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

    print("Demo:", bisect_fn.__name__)
    print("haystack ->", ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)
