# Key Idea 1: Think each s1 as blocks. Match with s2. 
# Key Idea 2: After completion of each block note s2Index and number of times s2 has been circled
# Key Idea 3: If s2Index at a block has been seen before, then there is a repitition(a pattern)
# Key Idea 4: There will be count from beforePattern, during all the cyclic pattern, afterPattern
# Key Idea 5: Create numBlocksAfterPatternStarted, numBlocksInEachPattern to make life easier

# Note: There will be cyclic pattern thanks to PIE in len(s1) * len(s2) iterations.
class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        s2Indices, counts = [], []
        s2Index = count = 0
        
        for _ in range(n1):
            for char in s1:
                if char==s2[s2Index]:
                    s2Index += 1
                    if s2Index==len(s2):
                        count += 1
                        s2Index=0
            
            if s2Index in s2Indices:
                patternStartIndex = s2Indices.index(s2Index)
                beforePatternCount = counts[patternStartIndex]
                numBlocksAfterPatternStarted, numBlocksInEachPattern = n1 - 1 - patternStartIndex, len(s2Indices) - patternStartIndex 
                patternCount = (count - counts[patternStartIndex]) * (numBlocksAfterPatternStarted//numBlocksInEachPattern)
                afterPatternCount = counts[patternStartIndex + (numBlocksAfterPatternStarted%numBlocksInEachPattern)] - counts[patternStartIndex] 
                return (beforePatternCount + patternCount + afterPatternCount)//n2
            
            s2Indices.append(s2Index)
            counts.append(count)
        
        return count//n2
