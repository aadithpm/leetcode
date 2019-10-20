class Solution(object):
    def missingNumber(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # sn = n * (a + l) / 2
        return ((len(arr) + 1) * (arr[0] + arr[len(arr) - 1]) / 2) - sum(arr)
