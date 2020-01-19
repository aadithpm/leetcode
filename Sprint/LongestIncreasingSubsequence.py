class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        max_length = [1] * len(nums)
        max_so_far = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    max_length[i] = max(max_length[i], max_length[j] + 1)
            max_so_far = max(max_so_far, max_length[i])
        return max_so_far
