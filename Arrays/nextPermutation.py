# 
# 1 2 3 4
# 1 2 
# 2 4 5 1
# 2 5 1 4 

# 2 4 5 4 1 0
# 2 5 4 4 1 0 
# 2 5 0 1 4 4

# 2 4 5 4 4 0
# 2 5 4 4 4 0
# 2 5 0 4 4 4 

def nextGreatestPermutation(arr):
    prev = arr[len(arr)-1]
    found = False
    i = 0
    for i in range(len(arr) - 2, -1, -1):
        if(arr[i]<prev):
            found = True
            break
        else:
            prev = arr[i]
    if(not found):
        arr.reverse()
    else:
        for j in range(len(arr) - 1, -1, -1):
            if(arr[i]<arr[j]):
                arr[i], arr[j] = arr[j], arr[i]
                l=0
                for k in range(i+1, (len(arr) + i)//2 + 1):
                    temp = arr[k]
                    arr[k] = arr[len(arr)-1-l]
                    arr[len(arr)-1-l] = temp
                    l+=1
                break
    print(arr)
                    
arr = [5,4,7,5,3]
nextGreatestPermutation(arr)           