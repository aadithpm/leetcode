# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 0, n
        while l < r:
            mid = (l + r) // 2
            if guess(mid) == -1:
                r = mid
            elif guess(mid) == 1:
                l = mid + 1
            elif guess(mid) == 0:
                return mid
        return l
