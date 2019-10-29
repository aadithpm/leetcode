class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) < 1:
            return []
        row_size, col_size = len(matrix), len(matrix[0])
        visited = [[False] * col_size for i in range(row_size)]
        
        i, j = 0, 0
        ri, rj = 0, 0
        
        row_col_flag = 0
        row_change = [0, 1, 0, -1]
        col_change = [1, 0, -1, 0]
        
        spiral = []
        
        for k in range(row_size * col_size):
            spiral.append(matrix[i][j])
            visited[ri][rj] = True
            
            ri = i + row_change[row_col_flag]
            rj = j + col_change[row_col_flag]
            
            if ri < row_size and ri >= 0 and rj < col_size and rj >= 0 and not visited[ri][rj]:
                i, j = ri, rj
            else:
                row_col_flag += 1
                row_col_flag %= 4
                ri = i + row_change[row_col_flag]
                rj = j + col_change[row_col_flag]
                i, j = ri, rj

        return spiral
