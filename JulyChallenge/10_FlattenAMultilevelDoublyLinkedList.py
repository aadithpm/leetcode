class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return
        
        stack = [head]
        prev = Node(0)
        
        while stack:
            root = stack.pop()
            root.prev = prev
            prev.next = root
            prev = root

            if root.next:
                stack.append(root.next)

            if root.child:
                stack.append(root.child)
                root.child = None

            prev = root        
            
        
        head.prev = None
        return head
