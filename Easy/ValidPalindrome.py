import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        s = re.sub(r'[^A-Za-z0-9]', '', s.lower())
        return s == s[::-1]