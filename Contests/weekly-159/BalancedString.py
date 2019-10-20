from collections import Counter
class Solution(object):
    def balancedString(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = Counter(s)
        res = n = len(s)
        i = 0
        for idx, letter in enumerate(s):
            counts[letter] -= 1
            while i < n and all(n / 4 >= counts[letter] for letter in 'QWER'):
                res = min(res, idx - i  + 1)
                counts[s[i]] += 1
                i += 1
                
        return res
