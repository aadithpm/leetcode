class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(subsets, temp, nums):
            if len(temp) == len(nums):
                subsets.append(temp[:])
            for i in range(0, len(nums)):
                if nums[i] not in temp:
                    temp.append(nums[i])
                    backtrack(subsets, temp, nums)
                    temp.pop()

        subsets = []
        backtrack(subsets, [], nums)
        return subsets
