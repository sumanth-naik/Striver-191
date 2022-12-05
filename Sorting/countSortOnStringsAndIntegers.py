S = "edsaa"

countArr = [0 for i in range(26)]
#frequency
for char in S:
    countArr[ord(char)-ord('a')] += 1
#cumulative frequency
for i in range(1, len(countArr)):
    countArr[i] = countArr[i] + countArr[i-1]
#ans arr
sortedArr = ["" for i in range(len(S))]
#put each char at cumFreq-1 th index and decrease cumFreq
for i in range(len(S)):
    sortedArr[countArr[ord(S[i])-ord('a')] -1] = S[i]
    countArr[ord(S[i])-ord('a')] -= 1

print(''.join(sortedArr))
    

arr = [-2,1,2,-1]

minElem = 1e9
maxElem = -1e9
for num in arr:
    if minElem>num: minElem = num
    if maxElem<num: maxElem = num

countArr = [0 for i in range(maxElem - minElem + 1)]
#frequency
for num in arr:
    countArr[num-minElem] += 1
print(countArr)

#cumulative frequency
for i in range(1, len(countArr)):
    countArr[i] = countArr[i] + countArr[i-1]
print(countArr)

#ans arr
sortedArr = [-1 for i in range(len(arr))]
#put each char at cumFreq-1 th index and decrease cumFreq
for num in arr:
    sortedArr[countArr[num-minElem]-1] = num
    countArr[num-minElem] -= 1

print(sortedArr)