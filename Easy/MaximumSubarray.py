class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Kadene's Algorithm
        max_1 = max_2 = nums[0]
        for i in nums[1:]:
            max_1 = max(i, max_1 + i)
            max_2 = max(max_1, max_2)
        return max_2