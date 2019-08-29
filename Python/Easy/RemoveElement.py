class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        nums_length = len(nums)
        while i < nums_length:
            if nums[i] == val:
                nums[i] = nums[nums_length - 1]
                nums_length = nums_length - 1
            else:
                i = i + 1
        return nums_length