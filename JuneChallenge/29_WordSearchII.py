class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        node.end = True

class Solution:
    def dfs(self, board, node, i, j, path, res):
            if node.end:
                res.append(path)
                node.end = False
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return
            tmp = board[i][j]
            node = node.children.get(tmp)
            if not node:
                return
            board[i][j] = '#'
            self.dfs(board, node, i + 1, j, path + tmp, res)
            self.dfs(board, node, i - 1, j, path + tmp, res)
            self.dfs(board, node, i, j + 1, path + tmp, res)
            self.dfs(board, node, i, j - 1, path + tmp, res)
            board[i][j] = tmp

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        trie = Trie()
        for word in words:
            trie.insert(word)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, trie.root, i, j, '', res)
        return res
