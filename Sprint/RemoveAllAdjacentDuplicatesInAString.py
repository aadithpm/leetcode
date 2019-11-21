from collections import deque
class Solution:
    def removeDuplicates(self, S: str) -> str:
        if not S:
            return ''
        stack = []
        S = deque(S)
        i = 0
        while S:
            if not stack:
                stack.append(S.popleft())
            else:
                char = S.popleft()
                if char == stack[-1]:
                    stack.pop()
                else:
                    stack.append(char)
        return ''.join(stack)
