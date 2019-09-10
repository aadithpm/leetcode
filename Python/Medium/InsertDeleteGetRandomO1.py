import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []
        self.map = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.map.keys():
            self.list.append(val)
            self.map[val] = len(self.list) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.map.keys():
            self.list[self.map[val]] = self.list[-1]
            self.map[self.list[-1]] = self.map[val]
            self.list[-1] = val
            self.list.pop()
            self.map.pop(val)
            return True
        return False
    
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if self.list:
            return self.list[random.randint(0, len(self.list) - 1)]
