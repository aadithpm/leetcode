class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {val: idx for idx, val in enumerate(nums2)}
        res = [-1] * len(nums1)
        for i in range(len(nums1)):
            for j in range(dic[nums1[i]], len(nums2)):
                if nums1[i] < nums2[j]:
                    res[i] = nums2[j]
                    break
        return res
        
