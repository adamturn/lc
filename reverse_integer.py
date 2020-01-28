# January 27th, 2020
# Python 3.8.1
"""
7. Reverse Integer
	Given a 32-bit signed integer, reverse digits of an integer.
	Note:
		Assume we are dealing with an environment which could only store
		integers within the 32-bit signed integer range [-2**31, 2**31 - 1].
		For the purpose of this problem, assume that your function returns
		0 when the reverse integer overflows.
"""
class Solution:
	def reverse(self, x: int) -> int:
		"""Original Attempt"""
		rx = str()
		if x >= 0:
			for char in str(x):
			rx = char + rx
		else:
			for char in str(x)[1:]:
			rx = char + rx
			rx = '-' + rx
		if -2**31 <= int(rx) <= (2**31 - 1):
			return int(rx)
		else:
			return 0

	def compact_rvs(self, x: int) -> int:
		"""Walrus Time!"""
		(rx := str(x)[::-1]) if x >= 0 else (rx := str(x)[0] + str(x)[1:][::-1])
		if -2**31 <= int(rx) <= 2**31 - 1:
			return int(rx)
		else:
			return 0
		
