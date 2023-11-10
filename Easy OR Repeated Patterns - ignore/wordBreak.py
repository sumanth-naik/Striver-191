
#max len of word in dict is 16

s = 'godisnowherenowhere'
dictionary = ['god', 'is', 'now', 'no', 'where', 'here']
dictionary = set(dictionary)


def wordBreak(s, n, currIndex, dictionary, answersArr, currentAns):
    if(currIndex == n):
        answersArr.append(currentAns.strip())
        return True
    
    for lenWord in range(1, 17):
        if( lenWord + currIndex - 1 < n and s[currIndex:currIndex+lenWord] in dictionary):
            wordBreak(s, n, currIndex+lenWord, dictionary, answersArr,  currentAns+ " " + s[currIndex:currIndex+lenWord])
    
    
n = len(s)
currIndex = 0
answersArr = []
currentAns = ""

wordBreak(s, n, currIndex, dictionary, answersArr, currentAns)
        
print(answersArr)
        