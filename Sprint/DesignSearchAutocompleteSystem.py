class TrieNode():
    def __init__(self):
        self.letters = {}
        self.end = False
        self.data = None
        self.rank = 0

class Trie():
    def __init__(self, sentences, times):
        self.root = TrieNode()
        for idx, sentence in enumerate(sentences):
            self.add(sentence, times[idx])

    def add(self, sentence, count):
        temp = self.root
        for char in sentence:
            if char not in temp.letters:
                temp.letters[char] = TrieNode()
            temp = temp.letters[char]
        temp.end = True
        temp.data = sentence
        temp.rank -= count
    
    def dfs(self, root):
        ret = []
        if root:
            if root.end:
                ret.append((root.rank, root.data))
            for letter in root.letters:
                ret.extend(self.dfs(root.letters[letter]))
        return ret
    
    def search(self, sentence):
        temp = self.root
        for char in sentence:
            if char not in temp.letters:
                return []
            temp = temp.letters[char]
        return self.dfs(temp)

class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.trie = Trie(sentences, times)
        self.keyword = ''
        
    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        results = []
        if c != '#':
            self.keyword += c
            results = self.trie.search(self.keyword)
        else:
            self.trie.add(self.keyword, 1)
            self.keyword = ''
        return [item[1] for item in sorted(results)[:3]]


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
