bank =["011001","000000","010100","001000"]
totalLasers = 0
prevRowLaserPointers = 0
for row in bank:
    numLaserPointersInRow = 0
    for char in row:
        if char=="1":
            numLaserPointersInRow += 1
    if(numLaserPointersInRow!=0):
        totalLasers = totalLasers + prevRowLaserPointers*numLaserPointersInRow
        prevRowLaserPointers = numLaserPointersInRow
        

print(totalLasers)   
    