class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return '[val: ' + str(self.val) + ', ' + 'next: ' + str(self.next) + ']'
    
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = [None] * 1000

    def add(self, key: int) -> None:
        idx = key % 1000
        if self.head[idx] is None:
            self.head[idx] = ListNode(key)
            return
        elif self.head[idx].val == key:
            return
        
        cur = self.head[idx]
        while cur:
            if cur.val == key:
                return
            if not cur.next:
                cur.next = ListNode(key)
                return
            if cur.next:
                cur = cur.next
        return
    
    def remove(self, key: int) -> None:
        idx = key % 1000
        cur = self.head[idx]
        if not cur:
            return
        if cur.val == key:
            self.head[idx] = cur.next
        while cur.next:
            if cur.next.val == key:
                cur.next = cur.next.next
                return
            cur = cur.next
        return

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        idx = key % 1000
        cur = self.head[idx]
        while cur:
            if cur.val == key:
                return True
            cur = cur.next
        return False
    
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
