# from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        # HashMap
        
        nums1_dict = Counter(nums1)
        nums2_dict = Counter(nums2)
    
        res = []
        
        for num in nums2:
            if num in nums1_dict.keys() and nums1_dict[num] > 0:
                res.append(num)
                nums1_dict[num] -= 1
        
        return res
        """
        
        # Two Pointers
        
        nums1, nums2, i, j, res = sorted(nums1), sorted(nums2), 0, 0, []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res.append(nums1[i])
                i, j = i + 1, j + 1
        return res
        
