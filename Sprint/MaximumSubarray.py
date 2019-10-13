class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = nums[0]
        max_so_far = nums[0]
        for n in nums[1:]:
            temp = max(n, temp + n)
            max_so_far = max(temp, max_so_far)
        return max_so_far
            
