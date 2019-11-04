class TrieNode:
    def __init__(self):
        self.contains = collections.defaultdict(TrieNode)
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        r = self.root
        for char in word:
            r = r.contains[char]
        r.end = True
    
    def check(self, queries, pattern):
        table = collections.defaultdict(lambda: False)
        
        def find(node, pattern_index, pattern, word, table):
            # Word is over
            if pattern_index >= len(pattern):
                if node.end:
                    key = ''.join(word)
                    table[key] = True
                for child in node.contains:
                    if child.islower():
                        find(node.contains[child], pattern_index, pattern, word + [child], table)
            else:
                for child in node.contains:
                    if child == pattern[pattern_index]:
                        find(node.contains[child], pattern_index + 1, pattern, word + [child], table)
                    elif child.islower():
                        find(node.contains[child], pattern_index, pattern, word + [child], table)
        
        find(self.root, 0, pattern, [], table)
        return [table[q] for q in queries]
                        
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        trie = Trie()
        for query in queries:
            trie.add(query)
        return trie.check(queries, pattern)
