class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = list(sorted(nums))
        return nums[len(nums) - k]