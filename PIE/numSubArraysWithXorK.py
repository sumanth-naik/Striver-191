from collections import defaultdict
def subarrayXor(arr, n, m):
    HashTable=defaultdict(int)
    HashTable[0]=1
    count=0
    curSum=0
    for i in arr:
        curSum^=i
        if HashTable[curSum^m]:
            count+=HashTable[curSum^m]
        HashTable[curSum]+=1
    return(count)


def numSubArrayWithXorK(arr, x):
    xorMap = {0:1}
    total = 0
    cumXor = 0
    for num in arr:
        cumXor ^= num 
        if cumXor^x in xorMap:
            total += xorMap[cumXor^x]
        if cumXor in xorMap:
            xorMap[cumXor] = xorMap[cumXor] + 1
        else:
            xorMap[cumXor] = 1
    return total

arr = [4, 2, 2, 6, 4]
x = 6
print(numSubArrayWithXorK(arr, x))