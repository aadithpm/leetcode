class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def get_live_neighbors(a, b):
            count = 0
            for i in range(a - 1, a + 2):
                for j in range(b - 1, b + 2):
                    if (i, j) in alive:
                        count += 1 
            
            if board[a][b] == 1:
                count -= 1
            return count
        
        alive = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 1:
                    alive.add((i, j))
        
        next_state = board[:]
        for i in range(len(board)):
            for j in range(len(board[0])):
                neighbors = get_live_neighbors(i, j)
                if board[i][j] == 0 and neighbors == 3:
                    next_state[i][j] = 1
                elif board[i][j] == 1 and (neighbors > 3 or neighbors < 2):
                    next_state[i][j] = 0
        return next_state
