#!env/bin/python
# -*- coding: utf-8 -*-

from time_decrator import time_counter

@time_counter
def string_to_int(s):
    """
    请你来实现一个 atoi 函数，使其能将字符串转换成整数。

    首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。

    当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。

    该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。

    注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。

    在任何情况下，若函数不能进行有效的转换时，请返回 0。

    说明：

        假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231, 231 − 1]。如果数值超过这个范围，qing返回 INT_MAX (231 − 1) 或 INT_MIN (−231) 。

    :param s: string
    :return: int
    """
    source_str = s.strip()

    int_string = []

    if not source_str: return 0
    if source_str[0] not in ['-', '+'] and not source_str.isdigit():
        return 0
    else:
        int_string.append(source_str[0])

    for c in source_str[1:]:
        if not c.isdigit():
            break
        else:
            int_string.append(c)

    num = int(''.join(int_string)) if int_string[0].isdigit() and len(int_string) >= 2 or len(int_string)>=1 and  int_string[0] not in ['-', '+'] else 0
    if num >= -2**31 and num <= 2 ** 31 -1:
        return num
    elif num < -2**31:
        return -2**31
    else:
        return 2 ** 31 -1



if __name__ == '__main__':
    s1 = ' -fer4ce3'
    s2 = '4gth6hj'
    s3 = '-3467843654765787dtrgt'
    s4 = '53575862432453647bgfnb'
    res1 = string_to_int(s1)

    res2 = string_to_int(s2)

    res3 = string_to_int(s3)
    res4 = string_to_int(s4)
    print(res1, res2, res3, res4)


