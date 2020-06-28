class Solution:
    def numSquares(self, n: int) -> int:
        if n < 2:
            return n
        sqs = []
        i = 1
        while i * i <= n:
            sqs.append(i * i)
            i += 1
        cnt, candidates = 0, {n}
        while candidates:
            cnt += 1
            temp = set()
            for candidate in candidates:
                for sq in sqs:
                    if candidate == sq:
                        return cnt
                    if candidate < sq:
                        break
                    temp.add(candidate - sq)
                candidates = temp
        return cnt
