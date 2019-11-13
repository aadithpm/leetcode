# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def merge_sort(head):
            if not head or not head.next:
                return head
            
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            fast = slow.next
            slow.next = None
            
            slow = merge_sort(head)
            fast = merge_sort(fast)
            return merge(slow, fast)
        
        def merge(l, r):
            if not l or not r:
                return l or r
            if l.val > r.val:
                l, r = r, l
            head = pre = l
            l = l.next
            while l and r:
                if l.val < r.val:
                    pre.next = l
                    l = l.next
                else:
                    pre.next = r
                    r = r.next
                pre = pre.next
            pre.next = l or r
            return head
        
        return merge_sort(head)
        
