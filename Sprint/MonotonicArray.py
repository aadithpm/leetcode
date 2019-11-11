class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) < 3:
            return True
        
        i = 0
        while A[i] == A[0]:
            if i == len(A) - 1:
                return True
            i += 1

        inc = -1 if A[0] > A[i] else 1
        i, j = 0, 1
        while j < len(A):
            if (A[j] - A[i]) * inc < 0:
                return False
            i, j = i + 1, j + 1
        return True
