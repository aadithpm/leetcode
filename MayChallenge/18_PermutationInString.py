from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        window = len(s1)
        for i in range(len(s2) - window + 1):
            if Counter(s2[i:i+window]) == s1_count:
                return True
        return False
        
