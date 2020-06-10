class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 or not word2:
            return max(len(word1), len(word2))

        dp = [[0 for i in range(len(word1) + 1)] for j in range(len(word2) + 1)]
        for i in range(len(word1) + 1):
            dp[0][i] = i
        for j in range(len(word2) + 1):
            dp[j][0] = j
        
        for i in range(1, len(word2) + 1):
            for j in range(1, len(word1) + 1):
                if word1[j - 1] == word2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
        
        return dp[i][j]
