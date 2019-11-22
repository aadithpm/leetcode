class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False
        
        def dfs(i, j, word):
            if len(word) == 0:
                return True
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or word[0] != board[i][j]:
                return False
            
            letter = board[i][j]
            board[i][j] = '-'
            res = dfs(i + 1, j, word[1:]) or dfs(i - 1, j, word[1:]) or dfs(i, j + 1, word[1:]) or dfs(i, j - 1, word[1:])
            board[i][j] = letter
            return res
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, word):
                    return True
        return False

                        
