#!env/bin/python
# -*- coding: utf-8 -*-

from time_decrator import time_counter

@time_counter
def palin_int(num):
    """
    判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
    :param num: int
    :return: bool
    """
    num_str = str(num)
    # if len(num_str) // 2 == 1:
    #     num_pair =
    for i in range(len(num_str) // 2):
        if num_str[i] != num_str[0 - i - 1]:
            return False

    return True

if __name__ == '__main__':
    n1 = -23432
    n2 = 2345432
    res1 = palin_int(n1)
    res2 = palin_int(n2)
    print(res1, res2)