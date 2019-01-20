class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if not haystack:
            return -1
        for i in range(len(needle)):
            substrs = [haystack[j:j + len(needle)] for j in range(i, len(haystack), len(needle))]
            if needle in substrs:
                return haystack.index(substrs[substrs.index(needle)])
        return -1