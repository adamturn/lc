# February 5th, 2020
# Python 3.7.4
"""
13. Roman to Integer
    Given a roman numeral, convert it to an integer.
    Input is guaranteed to be within the range from 1 t0 3999.
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        r2i = {
            'I': 1, 'IV': 4,
            'V': 5, 'IX': 9,
            'X': 10, 'XL': 40,
            'L': 50, 'XC': 90,
            'C': 100, 'CD': 400,
            'D': 500, 'CM': 900,
            'M': 1000
        }
        mem = s[0]
        total = 0
        for i in range(len(s)):
            if mem+s[i] in r2i:
                total += r2i[mem+s[i]] - r2i[mem]
                mem = s[i]
            else:
                total += r2i[s[i]]
                mem = s[i]
        return total
