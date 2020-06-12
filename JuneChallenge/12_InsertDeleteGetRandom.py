class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.items = []
        self.map = {}
        self.length = 0
        
    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.map:
            self.items.append(val)
            self.map[val] = self.length
            self.length += 1
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.map:
            self.items[self.map[val]] = self.items[-1]
            self.map[self.items[-1]] = self.map[val]
            self.items[-1] = val
            self.length -= 1
            self.items.pop()
            self.map.pop(val)
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if self.items:
            return self.items[random.randint(0, self.length - 1)]
