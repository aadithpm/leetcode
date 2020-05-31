class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Levenshtein distance
        n, m = len(word1), len(word2)
        if n == 0 or m == 0:
            return n + m
        
        matrix = [[0] * (m + 1) for i in range(n + 1)]
        for i in range(n + 1):
            matrix[i][0] = i
        for j in range(m + 1):
            matrix[0][j] = j
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                l = matrix[i - 1][j] + 1
                d = matrix[i][j - 1] + 1
                l_d = matrix[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    l_d += 1
                matrix[i][j] = min(l, d, l_d)
        
        return matrix[n][m]
