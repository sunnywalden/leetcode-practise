#!env/bin/python
# -*- coding: utf-8 -*-

from time_decrator import time_counter

@time_counter
def string_to_int(s):
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


