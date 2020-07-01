class Solution:
    def arrangeCoins(self, n: int) -> int:
        i, count = 1, 0
        while n > 0:
            n -= i
            i += 1
            if n >= 0:
                count += 1
        return count
