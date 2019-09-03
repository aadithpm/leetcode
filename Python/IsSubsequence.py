class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = list(s)
        for value in reversed(t):
            if s == []:
                return True
            if value == s[-1]:
                s.pop()
        return len(s) == 0