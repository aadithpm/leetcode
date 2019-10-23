class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_size = -1
        for i in range(0, len(nums)):
            idx = i
            this_size = 0
            while True:
                if nums[idx] == -1:
                    max_size = max(max_size, this_size)
                    break
                else:
                    old_idx = idx
                    idx = nums[idx]
                    nums[old_idx] = -1
                    this_size += 1
        return max_size
