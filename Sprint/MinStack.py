class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.length = 0
        self.min_index = -99
        self.data = []

    def is_empty(self):
        return self.length == 0

    def push(self, x: int) -> None:            
        if self.length != 0:
            self.min_index = self.length if self.data[self.min_index] > x else self.min_index
        else:
            self.min_index = 0
        self.data.append(x)
        self.length += 1

    def pop(self) -> None:
        if not self.is_empty():
            self.data.pop()
            self.length -= 1
            
            if self.min_index >= self.length and not self.is_empty():
                self.min_index = 0
                for i in range(1, self.length):
                    self.min_index = i if self.data[i] < self.data[self.min_index] else self.min_index

    def top(self) -> int:
        return self.data[self.length - 1]

    def getMin(self) -> int:
        if self.min_index > -99:
            return self.data[self.min_index]
