class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest_substr = 0
        substr_chars = set()
        i, j = 0, 0
        n = len(s)
        while i < n and j < n:
            if s[j] not in substr_chars:
                substr_chars.add(s[j])
                j += 1
                longest_substr = max(longest_substr, j - i)
            else:
                substr_chars.remove(s[i])
                i += 1
        return longest_substr
