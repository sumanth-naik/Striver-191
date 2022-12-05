arr1 = [0,1,2,3] 
n = len(arr1)
arr2 = [5,6,7,8,9]
m = len(arr2)

for index in range(0, n):
    if(arr1[index]>arr2[0]):
        arr1[index], arr2[0] = arr2[0], arr1[index]
        indexJ = 1
        while(indexJ<m and arr2[indexJ-1]>arr2[indexJ]):
            arr2[indexJ], arr2[indexJ-1] = arr2[indexJ-1], arr2[indexJ]
            indexJ += 1
    
      
indexJ = 1
while(indexJ<m and arr2[indexJ-1]>arr2[indexJ]):
    arr2[indexJ], arr2[indexJ-1] = arr2[indexJ-1], arr2[indexJ]
    indexJ += 1
         
print(arr1)
print(arr2)
