from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = Counter(arr)
        unique = set()
        for count in counts.values():
            if count not in unique:
                unique.add(count)
            else:
                return False
        return True
