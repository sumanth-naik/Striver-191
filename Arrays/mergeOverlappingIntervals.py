
intervals = [[1,3],[2,6],[8,10],[15,18]]


intervals.sort()

mergedList = [intervals[0]]
for index in range(1, len(intervals)):
    if(intervals[index][0]<=mergedList[len(mergedList)-1][1]):
        lastMerge = mergedList.pop()
        mergedList.append([lastMerge[0],max(intervals[index][1],lastMerge[1])])
    else:
        mergedList.append(intervals[index])
        
print(mergedList)