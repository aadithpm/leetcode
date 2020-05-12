class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return [i for i, count in collections.Counter(nums).items() if count == 1][0]
