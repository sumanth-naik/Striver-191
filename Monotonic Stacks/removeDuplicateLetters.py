class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        charToIndicesMap = defaultdict(list)
        for index, char in enumerate(s):
            charToIndicesMap[char].append(index)
        
        output, searchStartIndex, sortedChars = [], 0, sorted(charToIndicesMap.keys())
        for outputIndex in range(len(charToIndicesMap)):
            for char in sortedChars:
                possibleStartIndex = bisect.bisect_left(charToIndicesMap[char], searchStartIndex)
                if possibleStartIndex!=len(charToIndicesMap[char]) \
                    and (all(char==otherChar or (bisect.bisect_left(charToIndicesMap[otherChar], charToIndicesMap[char][possibleStartIndex])!=len(charToIndicesMap[otherChar])) for otherChar in sortedChars)):
                        output.append(char)
                        sortedChars.remove(char)
                        searchStartIndex = charToIndicesMap[char][possibleStartIndex]+1
                        break
        return ''.join(output)

from sortedcontainers import SortedSet
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        charToIndicesMap = defaultdict(list)
        for index, char in enumerate(s):
            charToIndicesMap[char].append(index)
        
        output, searchStartIndex, sortedChars = [], 0, SortedSet(charToIndicesMap.keys())
        for outputIndex in range(len(charToIndicesMap)):
            for char in sortedChars:
                possibleStartIndex = bisect.bisect_left(charToIndicesMap[char], searchStartIndex)
                if possibleStartIndex!=len(charToIndicesMap[char]) \
                    and (all(charToIndicesMap[otherChar][-1]>=charToIndicesMap[char][possibleStartIndex] for otherChar in sortedChars)):
                        output.append(char)
                        sortedChars.remove(char)
                        searchStartIndex = charToIndicesMap[char][possibleStartIndex]+1
                        break
        return ''.join(output)


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        charToLastIndexMap = defaultdict(int)
        for index, char in enumerate(s):
            charToLastIndexMap[char] = index

        stack, visited = [], set()
        for index, char in enumerate(s):
            if char not in visited:
                while stack and stack[-1]>char and charToLastIndexMap[stack[-1]]>index: # if it can be added later, add later
                    visited.remove(stack.pop())
                stack.append(char)
                visited.add(char)
        return ''.join(stack)