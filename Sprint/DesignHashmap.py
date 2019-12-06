class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.next = None
        
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = [None] * 1000

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        idx = key % 1000
        if self.head[idx] is None:
            self.head[idx] = ListNode(key, value)
        else:
            cur = self.head[idx]
            while True:
                if cur.key == key:
                    cur.key, cur.value = key, value
                    return
                if cur.next == None:
                    break
                cur = cur.next
            cur.next = ListNode(key, value)        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        idx = key % 1000
        cur = self.head[idx]
        while cur:
            if cur.key == key:
                return cur.value
            else:
                cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        idx = key % 1000
        cur = prev = self.head[idx]
        if not cur:
            return
        if cur.key == key:
            self.head[idx] = cur.next
        else:
            cur = cur.next
            while cur:
                if cur.key == key:
                    prev.next = cur.next
                    break
                else:
                    cur, prev = cur.next, prev.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
