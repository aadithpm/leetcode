from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = Counter(s)
        res = ''
        for char, times in sorted(count.items(), key = lambda x: x[1], reverse = True):
            res += char * times
        return res
