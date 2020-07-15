class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        for word in s.split():
            stack.append(word)
        return ' '.join(stack[::-1])
