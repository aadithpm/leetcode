class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        outp = []
        p = 1
        n_size = len(nums)
        
        for i in range(0, n_size):
            outp.append(p)
            p = p * nums[i]
        
        p = 1
        for i in range(n_size - 1, -1, -1):
            outp[i] = outp[i] * p
            p = p * nums[i]
        
        return outp