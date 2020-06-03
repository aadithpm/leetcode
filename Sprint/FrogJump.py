class Solution:
    def canCross(self, stones: List[int]) -> bool:
        map = {}
        for stone in stones:
            map[stone] = set()
        map[0].add(0)
        for i in range(len(stones)):
            for j in map[stones[i]]:
                for k in range(j - 1, j + 2):
                    if k > 0 and stones[i] + k in map:
                        map[stones[i] + k].add(k)
        
        return len(map[stones[-1]])
