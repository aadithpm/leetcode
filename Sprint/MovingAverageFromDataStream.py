from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.avg = 0
        self.numbers = deque([])
        self.length = 0
        self.limit = size

    def next(self, val: int) -> float:
        if self.length == self.limit:
            self.numbers.popleft()
            self.length -= 1
        self.numbers.append(val)
        self.length += 1
        self.avg = sum(self.numbers) / self.length
        return self.avg
