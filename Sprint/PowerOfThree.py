class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        max_three = 3 ** 19
        return n > 0 and max_three % n == 0
