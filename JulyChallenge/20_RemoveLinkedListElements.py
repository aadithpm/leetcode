# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        new_head = ListNode(0)
        temp = new_head
        while head:
            if head.val != val:
                temp.next = ListNode(head.val)
                temp = temp.next
            head = head.next
        return new_head.next
