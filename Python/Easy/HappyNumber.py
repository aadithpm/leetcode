class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        digits = set()
        while n != 1:
            n = sum(int(i) ** 2 for i in str(n))
            if n in digits:
                return False
            else:
                digits.add(n)
        return True