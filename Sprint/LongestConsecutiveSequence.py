class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        window = 0
        for i in nums:
            if i - 1 not in nums:
                j = i + 1
                while j in nums:
                    j += 1
                window = max(window, j - i)
        return window
