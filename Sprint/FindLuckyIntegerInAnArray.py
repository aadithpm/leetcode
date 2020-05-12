class Solution:
    def findLucky(self, arr: List[int]) -> int:
        return max([v for k, v in collections.Counter(arr).items() if k == v], default=-1)
