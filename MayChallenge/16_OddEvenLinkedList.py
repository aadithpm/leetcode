# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return
        old_head, old_head_second = head, head.next
        while head.next and head.next.next:
            old_next = head.next
            head.next = head.next.next
            old_next.next = head.next.next
            head = head.next
        head.next = old_head_second
        return old_head
