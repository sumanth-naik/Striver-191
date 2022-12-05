


arr = [2,3,4,2,2]
n = len(arr)

minElem = 0
minElemCount = 0
for num in arr:
    if minElemCount == 0:
        minElem = num
        minELemCOunt = 1
    if(minElem==num):
        minElemCount += 1
    else:
        minElemCount -= 1

count = 0
for num in arr:
    if minElem==num: count+=1
    
if count> n//2:
    print(minElem)
else:
    print(-1)