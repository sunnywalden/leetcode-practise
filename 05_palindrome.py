#!env/bin/python
# -*- coding: utf-8 -*-

from time_decrator import time_counter

@time_counter
def longgest_palin(my_str):
    """
        给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
    :param s: str
    :return: str
    """
    res = {}

    for index, s in enumerate(my_str):
        tmp_palin = None
        tmp = s
        for i, c in enumerate(my_str[index + 1:]):
            tmp += c
            if is_palin(tmp):
                tmp_palin = tmp
                if index == len(my_str) - 1:
                    res[tmp_palin] = len(tmp_palin)
            else:
                if tmp_palin and tmp_palin in tmp:
                    res[tmp_palin] = len(tmp_palin)

    if res:
        palins = sorted(res.keys(), reverse=True, key=lambda s:len(s))
        return palins[0]
    else:
        return None


def is_palin(my_str):
    if len(my_str) < 2:
        return False
    for i in range(len(my_str) // 2):
        if my_str[i] != my_str[-i - 1]:
            return False

    return True


class Solution(object):
    @time_counter
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        def expand(s, left, right):

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        start = 0
        end = 0
        for i in range(len(s)):
            len1 = expand(s, i, i)
            len2 = expand(s, i, i + 1)
            max_len = max(len1, len2)

            # 大于历史值（最大长度）
            if max_len > end - start:
                start = i - (max_len - 1) / 2

                end = i + max_len / 2
        return s[start:end + 1]
    
if __name__ == '__main__':
    s1 = "babad"
    s2 = "cbbd"
    res1 = longgest_palin(s1)
    print(res1)
    
    s = Solution()
    res3 = s.longestPalindrome(s1)
    print(res3)
    
    res2 = longgest_palin(s2)
    print(res2)
    
    res4 = s.longestPalindrome(s2)
    print(res4)