class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if not self.head or index < 0:
            return -1
        i = 0
        temp = self.head
        while i < index and temp:
            temp = temp.next
            i = i + 1
        return temp.val if temp else -1
        
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_head = Node(val, self.head)
        self.head = new_head

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        temp = self.head
        while temp.next:
            temp = temp.next
        new_tail = Node(val)
        temp.next = new_tail
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 1:
            self.addAtHead(val)
        else:
            i = 0
            temp = self.head
            while i < index - 1 and temp:
                temp = temp.next
                i = i + 1
            if temp and not temp.next:
                self.addAtTail(val)
            elif temp and temp.next:
                new_node = Node(val, temp.next)
                temp.next = new_node

                
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if self.head:
            if index == 0:
                self.head = self.head.next
            elif index > 0:
                i = 0
                temp = self.head
                while i < index - 1:
                    temp = temp.next
                    i = i + 1
                if temp.next:
                    temp.next = temp.next.next



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
