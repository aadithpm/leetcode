class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:            
        if len(trust) < N - 1:
            return -1
        
        score = [0] * (N + 1)
        
        for a, b in trust:
            score[a] -= 1
            score[b] += 1
        
        for idx, score in enumerate(score[1:], 1):
            if score == N - 1:
                return idx
        return -1
        
