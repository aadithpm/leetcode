"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        copy = collections.defaultdict(lambda: Node(0, 0, 0))
        copy[None] = None
        temp = head
        while temp:
            copy[temp].val = temp.val
            copy[temp].next = copy[temp.next]
            copy[temp].random = copy[temp.random]
            temp = temp.next
        return copy[head]
