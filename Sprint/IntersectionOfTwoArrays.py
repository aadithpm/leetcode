from collections import defaultdict
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        def inter(a, b):
            counts = defaultdict(int)
            visited = set()
            for num in b:
                if num not in visited:
                    visited.add(num)
            for num in a:
                if num in visited:
                    counts[num] += 1
            return counts
        return inter(nums1, nums2) if len(nums1) > len(nums2) else inter(nums2, nums1)
