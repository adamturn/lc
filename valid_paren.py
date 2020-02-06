# February 5th, 2020
# Python 3.7.4
"""
20. Valid Parentheses
    Given a string containing just characters
        '(' , ')' , '{' , '}' , '[' , ']'
    Determine if the string is valid.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        """
        Verbose but has the same runtime as 'optimal' solution
        with slightly less memory usage due to index loop
        instead of char loop, I think.
        """
        if len(s) == 0:
            return True
        elif len(s) % 2 != 0:
            return False
        parens = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        if s[0] in parens or s[-1] not in parens:
            return False
        else:
            stack = [s[0]]
        for i in range(1, len(s)):
            if s[i] not in parens:
                stack.append(s[i])
            elif stack.pop() != parens[s[i]]:
                return False
        return True

    def clean(self, s: str) -> bool:
        stack = []
        pmap = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for c in s:
            if c in pmap:
                top = stack.pop() if stack else ''
                if top != pmap[c]:
                    return False
            else:
                stack.append(c)
        return not stack
