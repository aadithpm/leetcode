class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.flight_map = collections.defaultdict(list)
        
        for ticket in tickets:
            origin, dest = ticket[0], ticket[1]
            self.flight_map[origin].append(dest)
        
        for origin, itinerary in self.flight_map.items():
            itinerary.sort(reverse=True)
        
        self.res = []
        self.dfs('JFK')
        
        return self.res[::-1]

    def dfs(self, node):
        dest = self.flight_map[node]
        while dest:
            next_dest = dest.pop()
            self.dfs(next_dest)
        self.res.append(node)
