#!env/bin/python
# -*- coding: utf-8 -*-

from time_decrator import time_counter


@time_counter
def middle_num(list1, list2):
    """
    给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

    请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

    你可以假设 nums1 和 nums2 不会同时为空。

    :param list1: list
    :param list2: list
    :return: float
    """
    l1_lenth = len(list1)
    l2_lenth = len(list2)

    if (l1_lenth + l2_lenth) % 2 == 1:
        return find_middle(list1, list2, (l1_lenth + l2_lenth) / 2)
    else:
        return (find_middle(list1, list2, (l1_lenth + l2_lenth) // 2) + find_middle(list1, list2, (l1_lenth + l2_lenth) // 2 + 1) ) / 2

def find_middle(l1, l2, num):
    if not l1:
        return l2[num]
    if not l2:
        return l1[num]
    m1_index = len(l1) // 2
    m2_index = len(l2) // 2

    m1_num = l1[m1_index]
    m2_num = l2[m2_index]

    if m1_index + m2_index < num:
        if m1_num > m2_num:
            return find_middle(l1, l2[m2_index + 1:], num - m2_index -1)
        else:
            return find_middle(l1[m1_index + 1 :], l2, num - m1_index - 1)
    else:
        if m1_num > m2_num:
            return find_middle(l1[:m1_index], l2, num)
        else:
            return find_middle(l1, l2[:m2_index], num)


if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [3, 4]
    res = middle_num(nums1, nums2)
    print(res)

    nums3 = [1, 3]
    nums4 = [2]
    res1 = middle_num(nums3, nums4)
    print(res1)
