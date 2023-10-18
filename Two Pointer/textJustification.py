class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        def getJustifiedString(selectedWords):
            if len(selectedWords)==1:
                return selectedWords[0] + "".join([" "]*(maxWidth - len(selectedWords[0])))
            
            numSpaces, numGaps = maxWidth - sum(map(len, selectedWords)), len(selectedWords)-1
            spacedWords = []

            for word in selectedWords:
                spacesToAdd = ceil(numSpaces/numGaps) if numGaps!=0 else 0
                numSpaces -= spacesToAdd
                numGaps -= 1
                spacedWords.append(word + "".join([" "]*(spacesToAdd)))

            return "".join(spacedWords)


        justifiedStrings = []
        left, right, n = 0, 0, len(words)
        while True:
            currWidth = len(words[left])
            while right+1<n and len(words[right+1])+1+currWidth<=maxWidth:
                currWidth += (len(words[right+1])+1)
                right += 1
            if right!=n-1:
                justifiedStrings.append(getJustifiedString(words[left:right+1]))
                left = right = right + 1
            else:
                justifiedStrings.append(getJustifiedString([" ".join(words[left:right+1])]))
                break
    
        return justifiedStrings

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        currWords, currLength, justifiedStrings = [], 0, []
        for word in words:
            if len(word) + len(currWords) + currLength > maxWidth: # if this word cant be added to existing group
                for i in range(maxWidth - currLength):
                    currWords[i%(len(currWords)-1 or 1)] += " "
                justifiedStrings.append(''.join(currWords))
                currWords, currLength = [], 0
            currWords.append(word)
            currLength += len(word)

        return justifiedStrings + [' '.join(currWords).ljust(maxWidth)]