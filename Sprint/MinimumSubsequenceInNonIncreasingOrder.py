class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        res = []
        while True:
            res.append(nums.pop())
            if sum(res) > sum(nums):
                return res
