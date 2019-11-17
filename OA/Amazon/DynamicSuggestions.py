import heapq

class Trie():
    def __init__(self):
        self.trie = {}
        self.end = '#'
    
    def add(self, word):
        sub = self.trie
        for char in word:
            if char not in sub:
                sub[char] = {}
            sub = sub[char]
        sub[self.end] = self.end
    
    def search(self, query):
        sub = self.trie
        for char in query:
            if char in sub:
                sub = sub[char]
        
        ans = []
        def dfs(trie, word):
            if self.end in trie:
                heapq.heappush(ans, word)
            for char in trie:
                if char != self.end:
                    dfs(trie[char], word + char)
        dfs(sub, query)
        
        return ans


def threeProductSuggestions(numProducts, repository, customerQuery):
    
    trie = Trie()
    for prod in repository:
        trie.add(prod.lower())
    
    suggestions = []
    query = customerQuery.lower()
    for i in range(len(query)):
        if i != 0:
            node = trie.search(query[:i+1])
            this_suggestions = []
            j = 0
            while node and j < 3:
                word = heapq.heappop(node)
                this_suggestions.append(word)
                j += 1
            
            suggestions.append(this_suggestions)
    
    return suggestions
    
