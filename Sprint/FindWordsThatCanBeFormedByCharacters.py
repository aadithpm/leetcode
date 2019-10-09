from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)
        s_lengths = 0
        for word in words: 
            word_count = Counter(word)
            letters = [(k in chars_count and chars_count[k] >= v) for k, v in word_count.items()]
            if all(letters):
                s_lengths += len(word)
        return s_lengths
