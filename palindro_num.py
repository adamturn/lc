# Februrary 4th, 2020
# Python 3.7.4
# adam note:
#   runtime was 68 ms, faster than 42.25% of online submissions
"""
9. Palindrome Number
    Determine whether an integer is a palindrome. An integer is a palindrome
    when it reads the same backward as forward.
    Follow Up:
        Could you solve it without converting the integer to a string?
"""
class Solution:
    def is_Palindrome(self, x: int) -> bool:
        """
        Easiest way is to coerce int -> str -> list
        Then loop through len // 2
        Walk --> <--
        """
        s = list(str(x))
        for i in range(len(s) // 2):
            if s[i] != s[-(i+1)]:
                return False
        return True

    def no_Conversion(self, x: int) -> bool:
        """
        Trying to do this without int -> str
        """
        if (x < 0 or (x != 0 and x % 10 == 0)):
            return False, 'Base Case'
        j = x
        j_len = 1
        while j >= 10:
            j = j // 10
            j_len += 1
        c = 0
        i = 1
        keep = 0
        while i < j_len // 2 + 1:
            keep += c * 10**(j_len-1)
            print("keep: ", keep)
            j = x - keep
            while j >= 10:
                j = j // 10
            c = x % 10**i // 10**(i-1)
            print("c: ", c, "| j: ", j)
            if c != j:
                return False, 'Fail Case'
            i += 1
        return True

    def clean(self, x: int) -> bool:
        if (x < 0 or (x % 10 == 0 and x != 0)):
            return False

        revert = 0
        while x > revert:
            revert = revert * 10 + x % 10
            x /= 10

        return (x == revert or x == revert // 10)



# test
t1 = 121  # True
t2 = -121  # False
t3 = 10  # False
t4 = 54145  # True
t5 = 51325  # False
t6 = 1001  # True
t7 = 2112  # True
ts = [t1, t2, t3, t4, t5, t6, t7]

for t in ts:
    print(Solution().good_version(t))
print('fin.')
