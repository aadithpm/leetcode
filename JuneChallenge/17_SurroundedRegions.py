class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        queue = collections.deque([])
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i in [0, len(board) - 1] or j in [0, len(board[0]) - 1]) and board[i][j] == 'O':
                    queue.append((i, j))
        
        while queue:
            r, c = queue.popleft()
            if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == 'O':
                board[r][c] = 'E'
                queue.append((r - 1, c))
                queue.append((r + 1, c))
                queue.append((r, c - 1))
                queue.append((r, c + 1))
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'E':
                    board[i][j] = 'O'
        
        
