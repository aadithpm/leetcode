class BrowserHistory:

    def __init__(self, homepage: str):
        self.queue = [homepage]
        self.curr, self.limit = 0, 0

    def visit(self, url: str) -> None:
        self.curr += 1
        if self.curr == len(self.queue):
            self.queue.append(url)
        else:
            self.queue[self.curr] = url
        self.limit = self.curr
        
    def reset(self, steps: int) -> str:
        self.curr = steps
        return self.queue[self.curr]

    def back(self, steps: int) -> str:
        return self.reset(max(self.curr - steps, 0))

    def forward(self, steps: int) -> str:
        return self.reset(min(self.curr + steps, self.limit))


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
