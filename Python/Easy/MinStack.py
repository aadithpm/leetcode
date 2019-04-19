class MinStack(object):

    def __init__(self):
        self.stack = []
        

    def push(self, x):
        cur_min = self.getMin()
        if cur_min is None or x < cur_min:
            cur_min = x
        self.stack.append((x, cur_min))

    def pop(self):
        return self.stack.pop()
        
    def peek(self, val):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[len(self.stack) - 1][val]
        
    def top(self):
        return self.peek(0)

    def getMin(self):
        return self.peek(1)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()