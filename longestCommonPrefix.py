# January 28th, 2020
# Python 3.8.1
"""
14. Longest Common Prefix
	Write a function to find the longest common prefix string amongst an array of strings.
	If there is no prefix, return an empty string ''.
	Note:
		All given inputs are in lowercase letters a-z.
"""
class Solution:
	def longestCommonPrefix(self, strs):
		"""Original Attempt"""
		lcp = str()
		for i in range(len(min(strs, default=lcp)) + 1):
			if len(set(x[:i] for x in strs])) == 1:
				lcp = strs[0][:i]
				continue
			else:
				break
		
		return lcp
