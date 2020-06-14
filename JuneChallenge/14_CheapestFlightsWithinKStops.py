class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for source, dest, cost in flights:
            graph[source].append((cost, dest))
            
        heap = []
        heapq.heappush(heap, (0, src, -1))
        while heap:
            new_cost, new_dest, curr = heapq.heappop(heap)
            if curr > K:
                continue
            if new_dest == dst:
                return new_cost
            
            for nc, nd in graph[new_dest]:
                heapq.heappush(heap, (nc + new_cost, nd, curr + 1))
        
        return -1
