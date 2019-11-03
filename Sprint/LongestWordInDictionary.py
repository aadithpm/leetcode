class TrieNode:
    def __init__(self):
        self.end = False
        self.contains = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, words):
        for word in words:
            self._add(word)

    def _add(self, word):
        r = self.root
        for char in word:
            if char not in r.contains:
                r.contains[char] = TrieNode()
            r = r.contains[char]
        r.end = True
    
    def longest(self):
        def dfs(node, res):
            temp = res
            for char, child in node.contains.items():
                if child.end:
                    part = dfs(child, res + char)
                    if len(part) > len(temp):
                        temp = part
                    elif len(part) == len(temp) and part < temp:
                        temp = part
            return temp
        return dfs(self.root, '')
            
class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        trie.add(words)
        return trie.longest()
