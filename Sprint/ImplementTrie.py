class TrieNode:
    def __init__(self):
        self.contains = collections.defaultdict(TrieNode)
        self.end = False
        
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        r = self.root
        for char in word:
            r = r.contains[char]
        r.end = True
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        r = self.root
        for letter in word:
            if letter not in r.contains:
                return False
            r = r.contains[letter]
        return r.end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        r = self.root
        for letter in prefix:
            if letter not in r.contains:
                return False
            r = r.contains[letter]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
