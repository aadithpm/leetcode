from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique_chars = {key: value for key, value in Counter(s).items() if value == 1}
        return min([s.index(i) for i in unique_chars.keys()]) if len(unique_chars) > 0 else -1

