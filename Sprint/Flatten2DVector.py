from collections import deque
class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.items = deque()
        for item in v:
            if isinstance(item, int):
                self.items.append(item)
            else:
                for inner_item in item:
                    self.items.append(inner_item)

    def next(self) -> int:
        return self.items.popleft()

    def hasNext(self) -> bool:
        return True if self.items else False


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()
