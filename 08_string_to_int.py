#!env/bin/python
# -*- coding: utf-8 -*-

from time_decrator import time_counter

@time_counter
def string_to_int(s):
    source_str = s.strip()

    int_string = []
    num_string = [str(i) for i in range(10)]

    if not source_str: return None
    if source_str[0] not in ['-', '+'] + num_string:
        return None
    else:
        int_string.append(source_str[0])

    int_string += list(filter(lambda c: c in num_string, source_str[1:]))

    num = int(''.join(int_string))

    if num >= -231 and num <= 230:
        return num
    elif num < -231:
        return -231
    else:
        return 230


if __name__ == '__main__':
    s1 = ' -fer4ce3'
    s2 = '4gth6hj'
    res1 = string_to_int(s1)
    res2 = string_to_int(s2)
    print(res1, res2)


