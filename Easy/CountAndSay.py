import itertools
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for i in range(n - 1):
            s = ''.join(str(len(list(y))) + x for x, y in itertools.groupby(s))
        return s