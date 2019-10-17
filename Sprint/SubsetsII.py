class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(subsets, temp, start, nums):
            subsets.append(temp[:])
            for i in range(start, len(nums)):
                if i == start or nums[i] != nums[i - 1]:
                    temp.append(nums[i])
                    backtrack(subsets, temp, i + 1, nums)
                    temp.pop()

        subsets = []
        backtrack(subsets, [], 0, sorted(nums))
        return subsets
