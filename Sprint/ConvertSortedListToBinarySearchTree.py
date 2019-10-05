# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def to_bst(self, head: ListNode, tail: ListNode) -> TreeNode:
        slow = fast = head
        
        if head == tail:
            return None
        
        while fast != tail and fast.next != tail:
            fast = fast.next.next
            slow = slow.next
        
        temp_head = TreeNode(slow.val)
        temp_head.left = self.to_bst(head, slow)
        temp_head.right = self.to_bst(slow.next, tail)
        
        return temp_head
        
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head is None:
            return None
        return self.to_bst(head, None)
