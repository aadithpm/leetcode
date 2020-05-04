from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        mag = Counter(magazine)
        for letter in ransomNote:
            if mag[letter] <= 0:
                return False
            mag[letter] -= 1

        return True
