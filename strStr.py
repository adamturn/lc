# February 6th, 2020
# Python 3.7.4
# adam note:
#   runtime results for my submission had high standard deviation
#   best result: 16 ms, faster than 99.66%
"""
13. Implement strStr()
    Return the index of the first occurrence of needle in the haystack,
    or -1 if needle is not part of the haystack.
    Clarification:
        For the purpose of this problem, we will return 0 when needle
        is an empty string.
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        elif needle in haystack:
            for i in range(len(haystack)):
                if needle[0] == haystack[i]:
                    mem, j = i, 0
                    while needle[j] == haystack[i]:
                        if j == len(needle)-1:
                            return mem
                        i += 1
                        j += 1
        else:
            return -1


# test
t1 = ['hello', 'll']  # 2
t2 = ['aaaaa', 'bba']  # -1
t3 = ['a', 'a']  # 0
t4 = ['aaa', 'a']  # 0
ts = [t1, t2, t3, t4]

for t in ts:
    print(Solution().strStr(t[0], t[1]))

print('--fin.')
