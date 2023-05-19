# TLE
# class Trie:
#     def __init__(self):
#         self.children = defaultdict(Trie)
#         self.isEnd = False
#         self.maxXorSeen = 0

#     def insert(self, num):
#         node = self
#         while num:
#             node = node.children[num&1]
#             num >>= 1
#         node.isEnd = True

#     def getMaxXor(self, node, index, currentXor):
#         if node.isEnd: 
#             self.maxXorSeen = max(self.maxXorSeen, currentXor)
#         for char in node.children:
#             if (char<<index) ^ (currentXor & (1<<index)): 
#                 self.getMaxXor(node.children[char], index+1, currentXor | 1<<index)
#             else: 
#                 self.getMaxXor(node.children[char], index+1, currentXor & ~(1<<index))

# class Solution:
#     def findMaximumXOR(self, nums) -> int:
#         trie = Trie()
#         for num in nums: 
#             # binaryString = str(bin(num))[::-1][:-2]
#             trie.getMaxXor(trie, 0, num)
#             trie.insert(num)   
#         return trie.maxXorSeen
    
#TLE
class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)

    def insert(self, num):
        node, mask = self, 1<<31
        while mask:
            bitVal = min(1, num & mask)
            node = node.children[bitVal]
            mask >>= 1
        
    def getMaxXor(self, num):
        node, xorVal, mask = self, 0, 1<<31
        while mask:
            bitVal = min(1, num & mask)
            if 1-bitVal in node.children:
                xorVal |= mask
                node = node.children[1-bitVal]
            else:
                node = node.children[bitVal]
            mask >>= 1
        return xorVal
    
class Solution:
    def findMaximumXOR(self, nums) -> int:
        trie, maxVal = Trie(), 0
        for num in nums: 
            maxVal = max(maxVal, trie.getMaxXor(num))
            trie.insert(num)       
        return maxVal

    
class Solution:
    def findMaximumXOR(self, nums) -> int:
        answer = 0
        for index in range(31, -1, -1):
            prefixes = set(num>>index for num in nums)
            answer <<= 1
            answer += any(answer^1^prefix in prefixes for prefix in prefixes)
        return answer
