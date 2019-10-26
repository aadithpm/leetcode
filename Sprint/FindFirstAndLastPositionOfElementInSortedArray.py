class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binary_search(nums, target, left):
            l, h = 0, len(nums)
            
            while l < h:
                mid = (l + h) // 2
                if nums[mid] > target or (left and target == nums[mid]):
                    h = mid
                else:
                    l = mid + 1
                    
            return l
        
        l = binary_search(nums, target, True)
        if l == len(nums) or nums[l] != target:
            return [-1, -1]
        r = binary_search(nums, target, False) - 1
        return [l, r]
