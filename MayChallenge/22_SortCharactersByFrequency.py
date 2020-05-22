class Solution:
    def frequencySort(self, s: str) -> str:
        counts = {}
        # O(n)
        for letter in s:
            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 1
        
        res = ''
        #O(nlogn)
        sorted_counts = sorted([(k, v) for k, v in counts.items()], key=lambda x: x[1], reverse=True)
        for pair in sorted_counts:
            res += pair[0] * pair[1]

        return res
