class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        if n > m:
            return self.isOneEditDistance(t, s)
        if m - n > 1:
            return False
        
        for i in range(n):
            if s[i] != t[i]:
                if n == m:
                    return s[i + 1:] == t[i + 1:]
                else:
                    return s[i:] == t[i + 1:]
        
        return n + 1 == m
