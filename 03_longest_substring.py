#!env/bin/python
# -*- coding: utf-8 -*-

from time_decrator import time_counter


@time_counter
def longest_substring(str):
    """
    给定一个字符串，找出不含有重复字符的最长子串的长度。
    :param str: string
    :return: None
    """
    res = {}

    for index, value in enumerate(str):
        tmp = value
        for j, v in enumerate(str[index+1:]):
            if v not in tmp:
                tmp += v
            elif tmp:
                res[tmp] = len(tmp)
                tmp = v
            else:
                pass
            if j == len(str[index+1:]) - 1 and tmp:
                res[tmp] = len(tmp)

    str_info = [(s, s.__len__()) for s in res]

    sort_str_info = sorted(str_info, key=lambda item:item[1], reverse=True)

    result = filter(lambda str_info: str_info[1] == sort_str_info[0][1], sort_str_info)

    print(map(lambda str_info: str_info[0], result))


class Solution1(object):
    @time_counter
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: dict
        """
        record_place = {}
        max_len = 0
        mid_max_len = 0
        for (i, ch) in enumerate(s):
            if ch not in record_place:
                mid_max_len += 1
                if max_len < mid_max_len:
                    max_len = mid_max_len
            else:
                if i - record_place[ch] > mid_max_len:
                    mid_max_len += 1
                    if mid_max_len > max_len:
                        max_len = mid_max_len
                else:
                    mid_max_len = i - record_place[ch]

            record_place[ch] = i
        return record_place

if __name__ == '__main__':
    test_str = 'SunnyWalden'
    longest_substring(test_str)
    s1 = Solution1()
    res = s1.lengthOfLongestSubstring(test_str)
    print(res)

