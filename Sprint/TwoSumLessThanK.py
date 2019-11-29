class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A = sorted(A)
        l, r = 0, len(A) - 1
        ans = -1
        while l < r:
            if A[l] + A[r] < K:
                ans = max(ans, A[l] + A[r])
                l += 1
            else:
                r -= 1
        return ans
