class ListNode:
    def __init__(self, val):
        self.val = val
        self.busy = False
        self.next = None

    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        return "Value: {}, Next: {}, Busy: {}".format(self.val, self.next, self.busy)

class LinkedList:
    def __init__(self):
        self.head = ListNode(0)

    def add(self, val):
        temp = self.head
        while temp and temp.next:
            temp = temp.next
        child = ListNode(val)
        temp.next = child

    def check(self, val):
        temp = self.head
        while temp and temp.val != val:
            temp = temp.next
        if temp:
            return not temp.busy

    def get(self):
        temp = self.head
        while temp and temp.busy:
            temp = temp.next
        if temp:
            temp.busy = True
            return temp.val
        return -1
    
    def release(self, val):
        temp = self.head
        while temp and temp.val != val:
            temp = temp.next
        if temp:
            temp.busy = False
            
class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        """
        self.list = LinkedList()
        for i in range(1, maxNumbers):
            self.list.add(i)
        
    def get(self) -> int:
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        """
        return self.list.get()

    def check(self, number: int) -> bool:
        """
        Check if a number is available or not.
        """
        return self.list.check(number)

    def release(self, number: int) -> None:
        """
        Recycle or release a number.
        """
        self.list.release(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
