class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 0 if n < 1 else n / 5 + self.trailingZeroes(n / 5)