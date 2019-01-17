# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        linked_list = []
        while head:
            linked_list.append(head.val)
            head = head.next
        return linked_list == linked_list[::-1]
        