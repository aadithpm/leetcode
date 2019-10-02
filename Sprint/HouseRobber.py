class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        h1 = h2 = 0
        for num in nums:
            temp = h1
            h1 = max(num + h2, h1)
            h2 = temp
        return h1
