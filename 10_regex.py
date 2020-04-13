#!env/bin/python
# -*- coding: utf-8 -*-

from time_decrator import time_counter

@time_counter
def regex_match(string, pattern):
    if '.' not in pattern and '*' not in pattern:
        if string != pattern:
            return False
    else:
        j = 0
        tmp = None
        for i, s in enumerate(pattern):
            if s == '.':
                tmp = '.'
                j += 1
            elif s == '*':
                if tmp == '.':
                    break
                else:
                    tmp = '*'
                    for count in range(j, len(string)):
                        if (i >= 1 and string[count] == pattern[i - 1]) or i < 1:
                            j += 1
                        else:
                            break

        return True


if __name__ == '__main__':
    s1 = "aa"
    p1 = "a"
    s2 = "aa"
    p2 = "a*"
    s3 = "ab"
    p3 = ".*"
    s4 = "aab"
    p4 = "c*a*b"

    res1 = regex_match(s1, p1)
    res2 = regex_match(s2, p2)
    res3 = regex_match(s3, p3)
    res4 = regex_match(s4, p4)
    print(res1, res2, res3, res4)