class Solution:
    def insertion(self, nums, target, left):
        l = 0
        h = len(nums)
        
        while l < h:
            m = (l + h) // 2
            if nums[m] > target or (left and target == nums[m]):
                h = m
            else:
                l = m + 1
        
        return l
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        li = self.insertion(nums, target, True)
        
        if li == len(nums) or nums[li] != target:
            return [-1, -1]
        
        return [li, self.insertion(nums, target, False) - 1]
