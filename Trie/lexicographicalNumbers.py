

class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.isEnd = False
    
    def insert(self, word):
        node = self
        for char in word:
            node = node.children[char]
        node.isEnd = True

    def dfsReturnAll(self, arr, node, stringSoFar):
        if node.isEnd: arr.append(int(stringSoFar))
        for char in node.children:
            self.dfsReturnAll(arr, node.children[char], stringSoFar+char)
        return arr
        



class Solution:
    def lexicalOrder(self, n: int):
        trie = Trie()
        for i in range(1, n+1): trie.insert(str(i))
        return trie.dfsReturnAll([], trie, "")