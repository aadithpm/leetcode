class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        heads = [matrix[i][0] for i in range(len(matrix))]
        target_row = 0
        
        for idx, i in enumerate(heads):
            if i > target:
                break
            target_row = idx
        
        for num in matrix[target_row]:
            if num == target:
                return True
        
        return False
