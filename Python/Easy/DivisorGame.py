class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        dp = [False for i in range(N + 1)]
        dp[0], dp[1] = False, False
        for i in range(2, N + 1):
            for j in range(1, i):
                if i % j == 0 and not dp[i - j]:
                    dp[i] = True
                    break
        return dp[-1]