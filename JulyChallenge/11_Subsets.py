class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        def backtrack(subsets, temp, nums, start):
            subsets.append(temp[:])
            for i in range(start, len(nums)):
                temp.append(nums[i])
                backtrack(subsets, temp, nums, i + 1)
                temp.pop()
        
        subsets = []
        backtrack(subsets, [], nums, 0)
        return subsets
