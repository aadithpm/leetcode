class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        for k in range(len(nums)):
            tmp = i
            i = nums[k] + j
            j = max(tmp, j)
        return max(i, j)