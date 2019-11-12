class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes, ones, twos = 0, 0, 0
        for i in nums:
            if i == 0:
                zeroes += 1
            elif i == 1:
                ones += 1
            elif i == 2:
                twos += 1
        i = 0
        for i in range(zeroes):
            nums[i] = 0
            i += 1
        for i in range(0, ones):
            nums[zeroes + i] = 1
            i += 1
        for i in range(0, twos):
            nums[zeroes + ones + i] = 2
            i += 1
