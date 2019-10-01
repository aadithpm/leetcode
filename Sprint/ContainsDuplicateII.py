class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numbers = {}
        for idx, num in enumerate(nums):
            if num in numbers and abs(idx - numbers[num]) <= k:
                return True
            numbers[num] = idx
        return False
