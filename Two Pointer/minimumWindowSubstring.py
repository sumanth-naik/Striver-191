s = "ADOBECODEBANC"
t = "ABC"
from collections import Counter
def minimumWindowSubstring(s, t):
    minimumString = None
    tCounter, sCounter = Counter(t), {}
    left, right, moveLeft = 0, 0, False
    m, n = len(s), len(t)
    while right<m and left<m-n+1:
        if not moveLeft:
            if not s[right] in sCounter:
                sCounter[s[right]] = 0
            sCounter[s[right]] += 1
            if contains(sCounter,tCounter):
                if not minimumString or len(minimumString)>right-left+1:
                    minimumString = s[left:right+1]
                moveLeft = True
            else:
                right += 1
        else:
            sCounter[s[left]] -= 1
            if sCounter[s[left]] == 0:
                del sCounter[s[left]]
            left += 1
            if contains(sCounter,tCounter):
                if len(minimumString)>right-left+1:
                    minimumString = s[left:right+1]
            else:
                right += 1
                moveLeft = False
    return minimumString if minimumString is not None else ""

def contains(counter1, counter2):
    for char in counter2:
        if not char in counter1 or not counter1[char]>=counter2[char]:
            return False
    return True

print(minimumWindowSubstring(s, t))




def minimumWindowSubstringOptimal(s, t):
    requiredCharsCounter = Counter(t)
    left, right, minimumWindowSubstringLeft, minimumWindowSubstringRight = 0, 0, None, 0
    m, n, charsFound = len(s), len(t), 0
    while left<m and right<m:
        if s[right] in requiredCharsCounter:
            if requiredCharsCounter[s[right]]>0:
                charsFound += 1
            requiredCharsCounter[s[right]] -= 1
        
        if charsFound == n:
            while s[left] not in requiredCharsCounter or requiredCharsCounter[s[left]]<0:
                if requiredCharsCounter[s[left]]<0:
                    requiredCharsCounter[s[left]] += 1
                left += 1
            if minimumWindowSubstringLeft is None or minimumWindowSubstringRight - minimumWindowSubstringLeft > right - left:    
                print(minimumWindowSubstringLeft, minimumWindowSubstringRight, left, right)
                minimumWindowSubstringLeft = left
                minimumWindowSubstringRight = right
        
        right += 1
    return s[minimumWindowSubstringLeft:minimumWindowSubstringRight+1] if minimumWindowSubstringLeft is not None else ""
s = "ab"
t = "a"
print(minimumWindowSubstringOptimal(s,t))




