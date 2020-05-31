class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse=True)
        prod = (nums[0] - 1) * (nums[1] - 1)
        return prod
