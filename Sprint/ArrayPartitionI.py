class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # return sum(min(i, j) for i, j in zip(sorted(nums)[0::2], sorted(nums)[1::2]))
        return sum(sorted(nums)[::2])
