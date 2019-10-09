from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        l = len(senate)
        R = deque([i for i in range(l) if senate[i] == 'R'])
        D = deque([i for i in range(l) if senate[i] == 'D'])
        
        while D and R:
            if D[0] > R[0]:
                R.append(R[0] + l)
            else:
                D.append(D[0] + l)
            
            D.popleft()
            R.popleft()
            
        return "Dire" if D else "Radiant"
