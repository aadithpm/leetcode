from collections import Counter
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        moves = Counter(moves)
        return (moves.get('U', 0) - moves.get('D', 0)) == 0 and (moves.get('L', 0) - moves.get('R', 0)) == 0
