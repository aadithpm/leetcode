class TrieNode:
    def __init__(self):
        self.contains = collections.defaultdict(TrieNode)
        self.end = False
        
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return str(self.contains.items())

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, words):
        for word in words:
            self._add(word)

    def _add(self, word):
        r = self.root
        for char in word:
            r = r.contains[char]
        r.end = True
    
    def prune(self, word):
        r = self.root
        pruned = ''
        for letter in word:
            if letter not in r.contains or r.end:
                break
            r = r.contains[letter]
            pruned += letter
        if r.end:
            return pruned
        else:
            return word

class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        trie = Trie()
        trie.add(dict)
        root_sentence = []
        for word in sentence.split():
            root_sentence.append(trie.prune(word))
        return ' '.join(root_sentence)
