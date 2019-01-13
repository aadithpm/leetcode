class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        one_count = 0
        while n != 0:
            n &= n - 1
            one_count += 1
        return one_count