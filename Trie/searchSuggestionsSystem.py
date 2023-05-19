from typing import List

class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.isEnd = False

    def insert(self, word):
        node = self
        for char in word:
            node = node.children[char]
        node.isEnd = True

    def getSuffixes(self, node, stringSoFar, suffixesArr):
        if node.isEnd:
            suffixesArr.append(stringSoFar)
            if len(suffixesArr)==3: 
                return True
        for char in sorted(node.children):
            if self.getSuffixes(node.children[char], stringSoFar+char, suffixesArr): 
                return True

    def getSearchSuggestionsForIndex(self, node, word, index):
        if node and word[index] in node.children:
            suffixesArr = []
            self.getSuffixes(node.children[word[index]], "", suffixesArr)
            if suffixesArr:
                return node.children[word[index]], [word[:index+1]+suffix for suffix in suffixesArr]
        return None, []

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for word in products: 
            trie.insert(word)

        node, suggestionsList = trie, []
        for index in range(len(searchWord)):
            node, suggestions = trie.getSearchSuggestionsForIndex(node, searchWord, index)
            suggestionsList.append(suggestions)
        
        return suggestionsList



# Binary search
import bisect
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        prefix, searchStartIndex, searchEndIndex = "", 0, len(products)
        suggestionsList = []
        for char in searchWord:
            prefix += char
            searchStartIndex = lowerBoundIndex = bisect.bisect_left(products, prefix, searchStartIndex, searchEndIndex)
            suggestionsList.append([products[index] for index in range(lowerBoundIndex, min(3+lowerBoundIndex, searchEndIndex)) if products[index].startswith(prefix)])
        return suggestionsList
    

# Two pointer
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        suggestionsList, left, right, n = [], 0, len(products)-1, len(products)
        for index, char in enumerate(searchWord):
            while left<=right and (index>=len(products[left]) or products[left][index]<char): left+=1
            while left<=right and (index>=len(products[right]) or products[right][index]>char): right-=1
            suggestionsList.append([products[i] for i in range(left, min(left+3, n, right+1))])
        return suggestionsList