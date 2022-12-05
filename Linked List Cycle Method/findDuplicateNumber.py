def findDuplicate(arr):
    slow = arr[arr[0]]
    fast = arr[arr[arr[0]]]
    
    while(slow!=fast):
        slow = arr[slow]
        fast = arr[arr[fast]]
        
    slow2 = arr[0]
    
    while(slow!=slow2):
        slow = arr[slow]
        slow2 = arr[slow2] 
        
    return slow2

arr = [1,2,3,4,2,6,2]

print(findDuplicate(arr))

#if only one duplicate
# XOR method

arr2 = [1,7,2,3,4,5,6,2]

def findSingleDuplicate(arr):
    cumulativeXor = 0
    
    for i in range(1,len(arr)):
        cumulativeXor = cumulativeXor ^ i ^ arr[i-1]
        
    cumulativeXor = cumulativeXor ^ arr[len(arr)-1]
    return cumulativeXor
    
print(findSingleDuplicate(arr2))
        