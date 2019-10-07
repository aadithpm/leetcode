# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        temp = head.next.next
        head, head.next = head.next, head
        head.next.next = self.swapPairs(temp)
        return head
