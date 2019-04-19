class Solution:
    def missingNumber(self, nums):
        '''
        gauss = len(nums) * (len(nums) + 1) / 2
        ungauss = sum(nums)
        return int(gauss) - ungauss
        '''
        
        return int(len(nums) * (len(nums) + 1) / 2) - sum(nums)