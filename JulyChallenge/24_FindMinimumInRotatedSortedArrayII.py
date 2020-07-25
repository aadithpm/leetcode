class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums) - 1
        while h > l:
            pivot = l + (h - l) // 2
            if nums[pivot] < nums[h]:
                h = pivot
            elif nums[pivot] > nums[h]:
                l = pivot + 1
            else:
                h -= 1
        return nums[l]
