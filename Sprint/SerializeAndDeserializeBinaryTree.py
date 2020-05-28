# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        string = []
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                string.append('None')
                continue
            else:
                string.append(str(node.val))
                queue.extend([node.left, node.right])
        return ','.join(string)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not len(data):
            return None
        data = collections.deque(data.split(','))
        root = TreeNode(int(data.popleft()))
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node:
                l, r = data.popleft(), data.popleft()
                node.left = TreeNode(int(l)) if l != 'None' else None
                node.right = TreeNode(int(r)) if r != 'None' else None
                queue.extend([node.left, node.right])
        return root
            


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
