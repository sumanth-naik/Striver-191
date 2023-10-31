# Key Idea: Create all nAry Trees and see
class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        
        n = len(stones)
        if (n-1)%(k-1)!=0: return -1

        lengthsArr = list(range(1, n+1, k-1))

        def getAllValidCombinations(index, totalLengthLeft, picksLeft, validCombinations, currCombination):
            if picksLeft==0:
                if totalLengthLeft==0:
                    validCombinations.append(currCombination[:])
                return
            if totalLengthLeft<picksLeft*lengthsArr[index]: return
            for pickIndex in range(index, len(lengthsArr)):
                if totalLengthLeft>=lengthsArr[pickIndex]:
                    currCombination.append(lengthsArr[pickIndex])
                    getAllValidCombinations(pickIndex, totalLengthLeft-lengthsArr[pickIndex], picksLeft-1, validCombinations, currCombination)
                    currCombination.pop()
                else:
                    break


        def permute(counter, perms, currPerm):
            if sum(counter.values())==0:
                perms.add(tuple(currPerm))
            else:
                for key in counter.keys():
                    if counter[key]>0:
                        currPerm.append(key)
                        counter[key] -= 1
                        permute(counter, perms, currPerm)
                        counter[key] += 1
                        currPerm.pop()

        @lru_cache(None)
        def getPermutations(size):
            validCombinations = []
            getAllValidCombinations(0, size, k, validCombinations, [])
            perms = set()
            for validCombination in validCombinations:
                permute(Counter(validCombination), perms, [])
            return perms


        @lru_cache(None)
        def nAryTree(i, j, level):
            if i==j: 
                return stones[i]*level
            perms, minCost = getPermutations(j-i+1), 1e9
            for perm in perms:
                cost, start = 0, i
                for length in perm:
                    cost += nAryTree(start, start+length-1, level+1)
                    start += length
                minCost = min(cost, minCost)
            return minCost

        return nAryTree(0, n-1, 0)


# Key Idea 1: Dont try to create valid trees, let dp figure it out(by returning 1e9)
# Key Idea 2: Add cost when merging the pile(literally stating the qn) and never else. 
#             If an index is part of 4 merges, it will be added to total 4 times.

# Optimization 1: (size - piles) should not leave any piles where size = j-i+1
# Optimization 2: adding k-1 as increment will make TC from n^3 to n^3/(k-1)
class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        
        n = len(stones)
        if (n-1)%(k-1)!=0: return -1

        prefixSum = [0]
        for num in stones:
            prefixSum.append(num+prefixSum[-1])

        @lru_cache(None)
        def dp(i, j, piles):
            if i==j:
                return 1e9 if piles!=1 else 0
            if piles==1:
                return dp(i, j, k) + prefixSum[j+1] - prefixSum[i]
            if (j-i+1 - piles)%(k-1)!=0: # Optimization 1 
                return 1e9 
            return min(dp(i, mid, 1) + dp(mid+1, j, piles-1) for mid in range(i, j, k-1)) # Optimization 2

        return dp(0, n-1, 1)
