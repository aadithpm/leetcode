class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Newton's method
        root = x
        while root * root > x:
            root = (root + x /root ) / 2
        return root