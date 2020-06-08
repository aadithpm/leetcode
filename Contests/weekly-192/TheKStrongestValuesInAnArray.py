class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr = sorted(arr)
        median = arr[(len(arr) - 1) // 2]
        def strongest_cmp(x: int, y: int) -> int:
            a = abs(x - median)
            b = abs(y - median)
            if a == b:
                return 1 if x > y else -1
            if a > b:
                return 1
            return -1
        strongest = sorted(arr, key=functools.cmp_to_key(strongest_cmp), reverse=True)
        return strongest[:k]
