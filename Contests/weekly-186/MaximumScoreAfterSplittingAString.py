class Solution:
    def maxScore(self, s: str) -> int:
        score = 0
        for i in range(1, len(s)):
            l_score = s[:i].count('0')
            r_score = s[i:].count('1')
            score = max(l_score + r_score, score)
        return score
