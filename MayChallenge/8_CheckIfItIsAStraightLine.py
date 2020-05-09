class Solution:
    def collinear(self, a, b, c):
        first_term = (b[1] - c[1]) * (a[0] - b[0])
        second_term = (a[1] - b[1]) * (b[0] - c[0])
        return first_term - second_term == 0

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) < 3:
            return True
        for i in range(len(coordinates) - 2):
            a, b, c = coordinates[i], coordinates[i + 1], coordinates[i + 2]
            if not self.collinear(a, b, c):
                return False
        return True
