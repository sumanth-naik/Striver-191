


nums = [0,0,1,1]
maxElem1 = 0
maxElem1Count = 0
maxElem2 = 1
maxElem2Count = 0

for num in nums:
    if maxElem1==num:
        maxElem1Count += 1
    elif maxElem2 == num:
        maxElem2Count += 1
    elif(maxElem1Count==0):
        maxElem1 = num
        maxElem1Count = 1
    elif maxElem2Count==0:
        maxElem2 = num
        maxElem2Count = 1
    else:
        maxElem1Count -= 1
        maxElem2Count -= 1
      
count1 = 0
count2 = 0
for num in nums:
    if num == maxElem1: count1 += 1
    if num == maxElem2: count2 += 1
count = [count1, count2]
ansList = []
if(count1>len(nums)//3):
    ansList.append(maxElem1)   
if(count2>len(nums)//3):
    ansList.append(maxElem2)   
print(ansList)


print([num for num,i in enumerate([maxElem1, maxElem2]) if count[i]>len(nums)//3])