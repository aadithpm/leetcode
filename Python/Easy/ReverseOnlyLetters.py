class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        letters = [c for c in S if c.isalpha()]
        return "".join(c if not c.isalpha() else letters.pop() for c in S)
