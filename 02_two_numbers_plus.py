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


class ListNode(object):
    """
        链表
    """
    def __init__(self):
        self.__value = 0
        self.__next = None

    def get_value(self):
        return self.__value

    def get_next(self):
        return self.__next

    def set_value(self, n):
        self.__value = n

    def set_next(self, ln):
        self.__next = ln


@time_counter
def number_plus_listnode(ln1, ln2):
    """
    给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

    如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

    您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
    :param ln1: ListNode
    :param ln2: ListNode
    :return: ListNode
    """
    tmp = 0
    last_ln = None
    head_ln = None
    while True:
        ln = ListNode()
        
        l1_val = ln1.get_value() if ln1 else 0
        l2_val = ln2.get_value() if ln2 else 0
        current_val = l1_val + l2_val
        res = current_val + tmp
        r = res - 10 if res >= 10 else res
        ln.set_value(r)
        if last_ln:
            last_ln.set_next(ln)
        else:
            head_ln = ln
        last_ln = ln
        tmp = res // 10
        ln1 = ln1.get_next() if ln1 else None
        ln2 = ln2.get_next() if ln2 else None

        if not ln1 and not ln2:
            break
    
    return head_ln

if __name__ == '__main__':
    # l1 = [1, 2, 4]
    # l2 = [3, 9, 6, 5]
    # res = two_num_plus(l1, l2)
    # print(res)
    ln1_1 = ListNode()
    ln1_1.set_value(1)
    ln1_2 = ListNode()
    ln1_2.set_value(2)
    ln1_1.set_next(ln1_2)
    ln1_3 = ListNode()
    ln1_3.set_value(4)
    ln1_2.set_next(ln1_3)

    ln2_1 = ListNode()
    ln2_1.set_value(3)
    ln2_2 = ListNode()
    ln2_2.set_value(9)
    ln2_1.set_next(ln2_2)
    ln2_3 = ListNode()
    ln2_3.set_value(6)
    ln2_2.set_next(ln2_3)
    ln2_4 = ListNode()
    ln2_4.set_value(5)
    ln2_3.set_next(ln2_4)
    
    head_ln = number_plus_listnode(ln1_1, ln2_1)
    ln = head_ln
    while True:
        if ln:
            value = ln.get_value()
            print("Value {}".format(value))
            ln = ln.get_next()
        else:
            break
    
