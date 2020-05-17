from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window = len(p)
        substr = Counter(p)
        mainstr = Counter()
        res = []
        for i in range(len(s)):
            mainstr[s[i]] += 1
            if i >= window:
                if mainstr[s[i - window]] == 1:
                    del mainstr[s[i - window]]
                else:
                    mainstr[s[i - window]] -= 1
            
            if substr == mainstr:
                res.append(i - window + 1)
        return res
