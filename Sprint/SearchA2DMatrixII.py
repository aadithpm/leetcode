class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or len(matrix) < 1 or len(matrix[0]) < 1:
            return False
        r, c = 0, len(matrix[0]) - 1
        
        while c > -1 and r < len(matrix):
            if target == matrix[r][c]:
                return True
            elif target < matrix[r][c]:
                c -= 1
            elif target > matrix[r][c]:
                r += 1
        
        return False
