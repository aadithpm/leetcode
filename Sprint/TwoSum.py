class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in complements.keys():
                return [complements[complement], idx]
            complements[num] = idx
        return []
