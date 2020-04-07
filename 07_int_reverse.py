#!env/bin/python
# -*- coding: utf-8 -*-

from time_decrator import time_counter


@time_counter
def int_reverse(num):
    """
        给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
    :param num: int
    :return: int
    """
    res = []
    str_of_num = str(num)
    for index, s in enumerate(str_of_num[::-1]):
        if index == 0 and s == "0":
            pass
        elif index == len(str_of_num) - 1 and s == "-":
            res = ["-"] + res
        else:
            res += s

    print(res)
    return int(''.join(res))


class Solution(object):
    @time_counter
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1 if x > 0 else -1
        x = abs(x)

        stack = []
        while x >= 1:
            stack.append(x % 10)
            x = x / 10
        res = 0
        i = 0

        while stack:
            res += stack.pop() * 10 ** i
            i += 1
        return res * sign * (res < 2 ** 31)
    
if __name__ == '__main__':
    int1 = 123
    int2 = -123
    int3 = 120
    s = Solution()
    res1 = int_reverse(int1)
    res4 = s.reverse(int1)
    res2 = int_reverse(int2)
    res5 = s.reverse(int2)
    res3 = int_reverse(int3)
    res6 = s.reverse(int3)
    print(res1, res2, res3)
    print(res4, res5, res6)
