class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        chars = {}
        longest, i, j = 0, 0, 0
        while j < n:
            if s[j] in chars:
                i = max(chars[s[j]], i)
            longest = max(longest, j - i + 1)
            chars[s[j]] = j + 1
            j += 1
        return longest
