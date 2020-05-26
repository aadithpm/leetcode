class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        l, r = 0, 0
        res = len(nums) + 1
        total = 0
        while l < len(nums) and r < len(nums):
            while total < s and r < len(nums):
                total += nums[r]
                r += 1
            res = min(res, r - l + 1)
            while total >= s and l < len(nums):
                total -= nums[l]
                l += 1
                res = min(res, r - l + 1)
        return 0 if res > len(nums) else res
