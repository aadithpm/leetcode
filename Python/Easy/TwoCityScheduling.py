class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        costs_length = len(costs)
        costs_A = sum(cost[0] for cost in costs[:costs_length // 2])
        costs_B = sum(cost[1] for cost in costs[costs_length // 2:])
        return costs_A + costs_B
