#!env/bin/python
# -*- coding: utf-8 -*-

from time_decrator import time_counter

@time_counter
def get_nums(num=0, num_list=[]):
    """
    给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

    你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
    :param num: int
    :param num_list: list
    :return:
    """
    filtered_nums = list(filter(lambda i: i <= num, num_list))
    filtered_nums.sort()
    for index, number in enumerate(filtered_nums):
        if num - number in filtered_nums[index:]:
            print(num_list.index(number), num_list.index(num - number))



if __name__ == '__main__':
    m, n = 9, [2, 7, 11, 15]
    get_nums(m, n)
    
