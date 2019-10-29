class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n < 1:
            return []
        row_size, col_size = n, n
        visited = [[False] * n for i in range(n)]
        answer = [[0] * n for i in range(n)]
        
        i, j = 0, 0
        ri, rj = 0, 0
        
        row_col_flag = 0
        row_change = [0, 1, 0, -1]
        col_change = [1, 0, -1, 0]
        
        for k in range(1, (n * n) + 1):
            answer[i][j] = k
            visited[i][j] = True
            
            ri = ri + row_change[row_col_flag]
            rj = rj + col_change[row_col_flag]
            
            if 0 <= ri < row_size and 0 <= rj < col_size and not visited[ri][rj]:
                i, j = ri, rj
            else:
                row_col_flag += 1
                row_col_flag %= 4
                
                ri = i + row_change[row_col_flag]
                rj = j + col_change[row_col_flag]
                
                i, j = ri, rj

        return answer
