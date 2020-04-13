#!env/bin/python
# -*- coding: utf-8 -*-

from time_decrator import time_counter


@time_counter
def most_water(*args):
    """
    给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
    :param args: list[int]
    :return: tuple
    """

    max = 0
    nums = ()

    for i, y1 in enumerate(args):
        for j in range(i + 1, len(args)):
            y2 = args[j]
            res = (j - i) * min(y1, y2)
            if res > max:
                max = res
                nums = (i, j)

    return (nums, max)


@time_counter
def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    start = 0
    end = len(height) - 1
    max_val = 0
    while start < end:
        max_val = max(max_val, (end - start) * min(height[start], height[end]))
        if height[start] > height[end]:
            end -= 1
        else:
            start += 1
    return max_val


if __name__ == '__main__':
    test1 = (3, 1, 21, 9, 54, 33)
    test2 = (18, 23, 11, 13, 45, 32)
    test3 = (1, 8, 6, 2, 5, 4, 8, 3, 7)

    res1 = most_water(*test1)
    res2 = most_water(*test2)
    res3 = most_water(*test3)

    res4 = maxArea(test1)
    res5 = maxArea(test2)
    res6 = maxArea(test3)

    print(res1, res2, res3, res4, res5, res6)
