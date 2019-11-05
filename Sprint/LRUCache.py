class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next, self.prev = None, None
        
class DoublyLinkedList:
    def __init__(self):
        self.dummy = ListNode(0, 0)
        self.tail = self.dummy
        self.size = 0
    
    def add(self, node):
        node.prev = self.dummy
        node.next = self.dummy.next
        self.dummy.next = node
        if node.next:
            node.next.prev = node
        if self.tail == self.dummy:
            self.tail = self.tail.next
        self.size += 1
    
    def delete(self, node):
        if not node:
            return
        if node is self.tail:
            self.tail = self.tail.prev
        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        self.size -= 1
        
class LRUCache:

    def __init__(self, capacity: int):
        self.dll = DoublyLinkedList()
        self.lookup = {}
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key in self.lookup:
            node = self.lookup[key]
            self.dll.delete(node)
            self.dll.add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.lookup and self.dll.size == self.capacity:
            del_node = self.dll.tail
            self.dll.delete(del_node)
            self.lookup.pop(del_node.key, None)
        
        self.dll.delete(self.lookup.pop(key, None))
        self.dll.add(ListNode(key, value))
        self.lookup[key] = self.dll.dummy.next

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
