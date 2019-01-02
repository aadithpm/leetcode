from collections import Counter
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = Counter(s)
        unique = {}
        
        for i in counts:
            if counts[i] == 1:
                unique[i] = 1
        idx = [s.index(i) for i in unique]
        
        return min(idx) if len(idx) > 0 else -1