class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        return [i for i in [max(i) for i in zip(*matrix)] if i in [min(i) for i in matrix]]
