#!env/bin/python
# -*- coding: utf-8 -*-

from time_decrator import time_counter

@time_counter
def two_num_plus(list1, list2):
    """
    给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

    如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

    您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
    :param list1: list
    :param list2: list
    :return: list or None
    """
    list1_lenth = len(list1)
    list2_lenth = len(list2)
    max_lenth = list1_lenth if list1_lenth >= list2_lenth else list2_lenth

    result = []
    tmp = 0
    for i in range(max_lenth):
        if i + 1 > list1_lenth:
            current_num = list2[i]
        elif i + 1 > list2_lenth:
            current_num = list1[i]
        else:
            current_num = list1[i] + list2[i]
        res = current_num + tmp
        r = res - 10 if res >= 10 else res
        result.append(r)
        tmp = res // 10
    
    return result


if __name__ == '__main__':
    l1 = [1, 2, 4]
    l2 = [3, 9, 6, 5]
    res = two_num_plus(l1, l2)
    print(res)
    
