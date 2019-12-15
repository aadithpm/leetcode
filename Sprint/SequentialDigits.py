class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        for digit in range(1, 9):
            num = next = digit
            while num <= high and next < 10:
                if num >= low:
                    ans.append(num)
                next += 1
                num = num * 10 + next
        return sorted(ans)
