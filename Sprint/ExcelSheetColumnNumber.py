class Solution:
    def titleToNumber(self, s: str) -> int:
        return sum((ord(val) - 64) * (26 ** idx) for idx, val in enumerate(s[::-1]))
