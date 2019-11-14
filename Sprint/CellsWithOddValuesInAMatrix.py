from collections import Counter
class Solution:
    def neighbors(self, n: int, m: int, indices: List[List[int]]) -> int:
        tuples = []
        for pair in indices:
            for i in range(0, n):
                tuples.append((i, pair[1]))
            for i in range(0, m):
                tuples.append((pair[0], i))
        return tuples

    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        indices = self.neighbors(n, m, indices)
        return len(list(filter(lambda x: x % 2 != 0, Counter(indices).values())))
