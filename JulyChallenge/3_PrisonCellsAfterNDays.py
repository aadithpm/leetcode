class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        seen = {}
        skip = False
        
        while N > 0:
            if not skip:
                state = tuple(cells)
                if state in seen:
                    N %= seen[state] - N
                    skip = True
                else:
                    seen[state] = N
            
            if N > 0:
                N -= 1
                next_state = self.nextState(cells)
                cells = next_state
        
        return cells
    
    
    def nextState(self, cells: List[int]):
        start = [0]
        for i in range(1, len(cells) - 1):
            start.append(int(cells[i - 1] == cells[i + 1]))
        start.append(0)
        return start
