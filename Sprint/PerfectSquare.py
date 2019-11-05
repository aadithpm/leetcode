class Solution:
    def numSquares(self, n: int) -> int:
        if n < 2:
            return n
        
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1
    
        squares_count, node = 0, {n}
        while node:
            squares_count += 1
            temp = set()
            for num in node:
                for square in squares:
                    if num == square:
                        return squares_count
                    if num < square:
                        break
                    temp.add(num - square)
            node = temp
        
        return squares_count
