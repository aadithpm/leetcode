class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0 if len(nums) == 0 else nums[0]
        
        l = len(nums)
        h1 = [0] * (l + 1)
        h2 = [0] * (l + 1)
        
        h1[1] = nums[0]
        
        for i in range(2, l + 1):
            h1[i] = max(h1[i - 1], h1[i - 2] + nums[i - 1])
            h2[i] = max(h2[i - 1], h2[i - 2] + nums[i - 1])
            
        return max(h1[l - 1], h2[l])
