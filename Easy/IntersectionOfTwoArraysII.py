def make_intersect(small, large):
    temp = []
    for i in small:
        if i in large:
            temp.append(i)
            large.remove(i)
    return temp

class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) >  len(nums2):
            return make_intersect(nums2, nums1)
        
        return make_intersect(nums1, nums2)