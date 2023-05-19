from typing import List

class Trie:
    def __init__(self) -> None:
        self.children = defaultdict(Trie)

    def insertWithCount(self, nums):
        node, count = self, 0
        for num in nums:
            if num not in node.children: count+=1
            node = node.children[num]
        return count


class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:   
        n, right, trie, distinctCount = len(nums), -1, Trie(), 0
        for left in range(n):
            # check and step on entering
            while right+1<n and not(nums[right+1]%p==0 and k==0):
                if nums[right+1]%p==0: 
                    k-=1
                right += 1
            distinctCount += trie.insertWithCount(nums[left:right+1])
            # book keep on leaving
            if nums[left]%p==0: 
                k+=1
        return distinctCount
    

# Rabin karp - Rolling Hash
class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:   
        n, count, hashesMap = len(nums), 0, defaultdict(list)
        for left in range(n):
            hash, d, q = 0, 26, 1e9+7
            right, numDivs = left-1, k
            while right+1<n and not(nums[right+1]%p==0 and numDivs==0):
                if nums[right+1]%p==0: 
                    numDivs -= 1
                right += 1
                hash = (hash*d + nums[right])%q
                hashCollision = False
                if hash in hashesMap:
                    # there can be multiple arrays pointing to same hash, so need a hashmap of hashes, not a set
                    for leftPrev, rightPrev in hashesMap[hash]:
                        if nums[leftPrev:rightPrev+1]==nums[left:right+1]: 
                            hashCollision = True
                            break
                if not hashCollision: count += 1
                hashesMap[hash].append((left, right))
        return count
                