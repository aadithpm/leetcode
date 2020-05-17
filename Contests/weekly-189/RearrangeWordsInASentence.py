class Solution:
        
    def arrangeWords(self, text: str) -> str:
        words = text.split()
        words[0] = words[0].lower()
        lengths = [len(i) for i in words]
        words = sorted(words, key=lambda x: len(x))
        words[0] = words[0].title()
        return ' '.join(words)
