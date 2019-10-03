class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum = 0
        while n > 0:
            sum += 1
            n &= (n - 1)
        return sum
