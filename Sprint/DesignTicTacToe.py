class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.board = [['-'] * n for i in range(n)]
        self.size = n
        self.markers = {
            1: 'X',
            2: 'O'
        }
        
    def check(self, row: int, col: int, player: int) -> bool:
        if len(set(self.board[row])) == 1 or len(set([self.board[i][col] for i in range(0, self.size)])) == 1 or self.diag(player) or self.rev_diag(player):
            return player
        return 0
    
    def diag(self, player: int) -> bool:
        front = set()
        front.add(self.markers[player])
        for i in range(self.size):
            if self.board[i][i] not in front:
                return False
        return True
    
    def rev_diag(self, player: int) -> bool:
        back = set()
        back.add(self.markers[player])
        for i in range(self.size):
            if self.board[i][self.size - 1 - i] not in back:
                return False
        return True
        
    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        self.board[row][col] = self.markers[player]
        return self.check(row, col, player)


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
