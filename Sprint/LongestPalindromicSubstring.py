class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 1:
            return ''
        
        def expand(s, left, right):
            l, r = left, right
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1
            
        
        start, end = 0, 0
        for i in range(len(s)):
            l1 = expand(s, i, i)
            l2 = expand(s, i, i + 1)
            l = max(l1, l2)
            if l > end - start:
                start = i - (l - 1) // 2
                end = i + l // 2
        return s[start:end + 1]
    
