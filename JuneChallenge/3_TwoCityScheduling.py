class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs = sorted(costs, key=lambda x: x[0] - x[1])
        n = len(costs)
        A = sum(i[0] for i in costs[:n//2])
        B = sum(i[1] for i in costs[n//2:])
        return A + B
