from collections import deque
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        # return sorted([i * i for i in A])
    
        pos, neg, res = deque([]), deque([]), []
        for num in A:
            if num < 0:
                neg.append(num * num)
            else:
                pos.append(num * num)

        while pos and neg:
            if pos[0] < neg[len(neg) - 1]:
                res.append(pos.popleft())
            else:
                res.append(neg.pop())
                
        while pos:
            res.append(pos.popleft())
        while neg:
            res.append(neg.pop())
        
        return res
