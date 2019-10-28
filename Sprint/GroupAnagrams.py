from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        grouped = []
        count = 0
        for word in strs:
            s = ''.join(sorted(word))
            if s in anagrams:
                grouped[anagrams[s]].append(word)
            else:
                anagrams[s] = count
                grouped.append([word])
                count += 1
        return grouped
