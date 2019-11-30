import re
class ListNode():
    def __init__(self, letter, count):
        self.letter = letter
        self.count = count
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add(self, string):
        matches = re.findall(r'([a-zA-z]{1}\d*)', string)
        for pair in matches:
            self.add_node(pair)
    
    def add_node(self, pair):
        letter, count = pair[0], int(pair[1:])
        if self.head is None and self.tail is None:
            self.head = ListNode(letter, count)
            self.tail = self.head
        else:
            node = ListNode(letter, count)
            self.tail.next = node
            self.tail = node
            
class StringIterator(object):

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.ll = LinkedList()
        self.ll.add(compressedString)
        self.pointer = self.ll.head
        
    def next(self):
        """
        :rtype: str
        """
        if self.pointer.count < 1:
            if not self.hasNext():
                return ' '
            self.pointer = self.pointer.next
        self.pointer.count -= 1
        return self.pointer.letter
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return False if self.pointer.next is None and self.pointer.count == 0 else True


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
