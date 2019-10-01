from collections import Counter
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return any(i > 1 for i in Counter(nums).values())
