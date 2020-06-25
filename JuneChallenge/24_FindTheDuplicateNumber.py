class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        x = y = nums[0]
        while True:
            x = nums[x]
            y = nums[nums[y]]
            if x == y:
                break
        
        x = nums[0]
        while x != y:
            x = nums[x]
            y = nums[y]
        
        return y
