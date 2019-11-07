class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        l, r = 0, len(A) - 1
        while l < r:
            m1 = (l + r) // 2
            m2 = m1 + 1
            if A[m1] < A[m2]:
                l = m1 + 1
            else:
                r = m1
        return l
