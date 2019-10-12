class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = set()

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: None
        """
        self.words = set()
        for word in dict:
            self.words.add(word)

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        count = 0
        for dict_word in self.words:
            if len(word) == len(dict_word):
                for i, j in zip(word, dict_word):
                    if count > 1:
                        break
                    if i != j:
                        count += 1
            if count == 1:
                break
            else:
                count = 0
        return count == 1

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
