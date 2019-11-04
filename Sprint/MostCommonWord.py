class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        paragraph = re.sub(r'[^A-Za-z\s]', ' ', paragraph)
        words = {}
        for word in paragraph.split():
            word = word.lower()
            if word not in banned:
                words[word] = words.get(word, 0) + 1
        return max(words.items(), key = lambda x: x[1])[0]
