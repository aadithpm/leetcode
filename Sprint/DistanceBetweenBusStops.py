class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        front = min(start, destination)
        back = max(start, destination)
        return min(sum(distance[front:back]), sum(distance) - sum(distance[front:back]))
