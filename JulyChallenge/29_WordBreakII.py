class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if set(collections.Counter(s).keys()) > set(collections.Counter("".join(wordDict)).keys()):
            return []

        word_set = set(wordDict)
        
        dp = [[]] * (len(s) + 1)
        dp[0] = [""]
        
        for idx in range(1, len(s) + 1):
            res = []
            for start_idx in range(0, idx):
                word = s[start_idx:idx]
                if word in word_set:
                    for sentence in dp[start_idx]:
                        res.append((sentence + ' ' + word).strip())
            
            dp[idx] = res
        
        return dp[len(s)]
