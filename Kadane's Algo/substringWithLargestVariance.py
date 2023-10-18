from collections import Counter
class Solution:
    def largestVariance(self, s: str) -> int:
        globalMaxVariance, counter = 0, Counter(s)

        def modifiedKadanes(majorChar, minorChar):
            nonlocal globalMaxVariance
            minorCharCount, majorCharCount, minorCharCountLeft = 0, 0, counter[minorChar]

            for char in s:
                if char==majorChar: 
                    majorCharCount += 1
                elif char==minorChar:
                    minorCharCount += 1
                    minorCharCountLeft -= 1
                if minorCharCount>majorCharCount and minorCharCountLeft!=0:
                    majorCharCount = minorCharCount = 0
                if minorCharCount>0:
                    globalMaxVariance = max(globalMaxVariance, majorCharCount-minorCharCount)
            
        for majorChar in counter.keys():
            for minorChar in counter.keys():
                if majorChar!=minorChar:
                    modifiedKadanes(majorChar, minorChar)

        return globalMaxVariance

            
