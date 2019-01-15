class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        tmp = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[tmp]:
                tmp += 1
                nums[tmp] = nums[i]
        return tmp + 1