class Solution:
    def moveZeroes(self, nums):
        nums.sort(key = bool, reverse = True)