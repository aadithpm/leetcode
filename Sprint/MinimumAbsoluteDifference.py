class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        a = sorted(arr)
        diff = min(a[i] - a[i - 1] for i in range(1, len(a)))
        return [[a[i - 1], a[i]] for i in range(1, len(a)) if a[i] - a[i - 1] == diff]
