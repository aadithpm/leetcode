# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:
from functools import lru_cache

class Solution:
    @lru_cache(maxsize=None)
    def cached_knows(self, a, b):
        return knows(a, b)

    def findCelebrity(self, n: int) -> int:
        self.n, candidate = n, 0
        for i in range(1, self.n):
            if knows(candidate, i):
                candidate = i

        if self.is_celebrity(candidate):
            return candidate
        
        return -1
    
    def is_celebrity(self, i):
        for j in range(self.n):
            if i == j:
                continue
            if self.cached_knows(i, j) or not self.cached_knows(j, i):
                return False
        return True
