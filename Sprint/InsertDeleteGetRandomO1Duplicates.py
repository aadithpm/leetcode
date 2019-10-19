from collections import defaultdict
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.items = []
        self.map = defaultdict(set)
        self.length = 0
        
    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.map[val].add(self.length)
        self.items.append(val)
        self.length += 1
        return len(self.map[val]) == 1

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if self.map[val]:
            rem, last = self.map[val].pop(), self.items[-1]
            self.items[rem] = last
            self.map[last].add(rem)
            
            self.map[last].discard(self.length - 1)
            self.items.pop()
            
            self.length -= 1
            
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if self.items:
            return random.choice(self.items)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
