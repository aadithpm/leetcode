class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m1 = (l + r) // 2
            m2 = m1 + 1
            if nums[m1] > nums[m2]:
                r = m1
            else:
                l = m2
        return l
