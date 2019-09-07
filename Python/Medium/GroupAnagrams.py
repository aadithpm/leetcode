class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_counts = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            char_counts[tuple(count)].append(s)
        return char_counts.values()
        