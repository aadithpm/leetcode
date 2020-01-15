class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        res = -1
        l, r = 0, len(A) - 1
        while l <= r:
            mid = (l + r) // 2
            if A[mid] >= mid:
                if A[mid] == mid:
                    res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
