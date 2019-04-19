class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Faster than 100% kappa
        max_int = 2147483647
        min_int = -1 * max_int - 1
        rev = int(str(x)[::-1]) if x > 0 else int('-' + (str(x)[::-1].replace('-', '')))
        return rev if rev < max_int and rev > min_int else 0