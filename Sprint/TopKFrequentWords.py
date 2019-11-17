from collections import Counter
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        if not words:
            return []
        counts = Counter(words)
        counts = sorted(counts.items(), key = lambda x: x[0])
        return [word for word, count in sorted(counts, key = lambda x: x[1], reverse = True)][:k]
