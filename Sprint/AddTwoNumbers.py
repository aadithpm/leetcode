# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = ListNode(0)
        l3 = temp
        carry = 0
        while l1 is not None or l2 is not None:
            add = 0
            add += l1.val if l1 is not None else 0
            add += l2.val if l2 is not None else 0
            add += carry
            carry = add // 10
            
            l3.next = ListNode(add % 10)
            l3 = l3.next
            
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        
        if carry > 0:
            l3.next = ListNode(carry)

        return temp.next
