class Solution:
    def isHappy(self, n: int) -> bool:
        numbers = set()
        prod = sum(int(i) ** 2 for i in str(n))
        while prod != 1:
            if prod in numbers:
                return False
            numbers.add(prod)
            prod = sum(int(i) ** 2 for i in str(prod))
        return True
