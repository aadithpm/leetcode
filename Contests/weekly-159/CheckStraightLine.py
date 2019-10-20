class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        if len(coordinates) < 2:
            return False
        if len(coordinates) < 3:
            return (coordinates[1][0] - coordinates[0][0]) - (coordinates[1][1] - coordinates[1][1]) == 0
        
        for i, j, k in zip(coordinates[:len(coordinates) - 2], coordinates[1:len(coordinates) - 1], coordinates[2:]):
            # (a, b), (n, m), (x, y)
            # (n−b)(x−m)=(y−n)(m−a)
            # 
            if ((j[1] - k[1]) * (i[0] - j[0])) - ((j[0] - k[0]) * (i[1] - j[1])) != 0:
                return False
        return True
