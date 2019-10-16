from collections import Counter
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        counts = Counter(arr1)
        ans = []
        for i in arr2:
            ans.extend([i] * counts[i])
            counts[i] = 0
        for i in range(1001):
            ans.extend([i] * counts[i])
        return ans
