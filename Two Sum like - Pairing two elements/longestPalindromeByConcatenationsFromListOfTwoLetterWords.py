
from collections import Counter
words = ["ab","ty","yt","lc","cl","ab"]

counter = Counter(words)
print(counter)
countDiff = 0
countSame = 0
foundAMid = False
for word in counter:
    rev = word[::-1]
    if(word[0]!= word[1] and rev in words):
        countDiff += 4* min(counter[word], counter[rev])
    elif(word[0]==word[1]):
        if(counter[word]%2==1):
            foundAMid = True
        countSame += (counter[word]//2) * 4
if(foundAMid):
    countSame+=2
print(countDiff//2+countSame)
        


count = 0
midCount = 0
wordMap = {}
for word in words:
    if word not in wordMap:
        wordMap[word] = 1
    else:
        wordMap[word] = wordMap[word] + 1
    if(word[0]!=word[1] and word[::-1] in wordMap):
        count = count + min(wordMap[word], wordMap[word[::-1]]) * 4 - min(wordMap[word]-1, wordMap[word[::-1]]) * 4
    elif(word[0]==word[1]):
        if wordMap[word]%2 == 1:
            midCount += 1
        else:
            midCount -= 1
        count = count + (wordMap[word]//2)*4 - ((wordMap[word]-1)//2)*4
if(midCount>0): count+=2
print(count)


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        pairs, sym, nonPaired = 0, 0, Counter()
        for w in words:
            if nonPaired[w[:: -1]] > 0:
                pairs += 1
                nonPaired[w[:: -1]] -= 1
                sym -= 1 if w[0] == w[1] else 0
            else:
                nonPaired[w] += 1    
                sym += 1 if w[0] == w[1] else 0
        return pairs * 4 + (2 if sym > 0 else 0)