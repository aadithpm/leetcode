from collections import Counter
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        stones = Counter(S)
        total_jewels = 0
        for jewel in J:
            total_jewels += stones.get(jewel, 0)
        return total_jewels
