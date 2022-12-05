nums = [1,1,1,2,2,3]
k = 2



def topKFrequent(nums, k):
    counter = Counter(nums)
    counterList = list(counter)
    high = len(counterList) - 1
    low = 0

    while low<=high:
        pivotValue = counter[counterList[high]]
        swapPointer = low
        for i in range(low, high):
            #pivot check
            if counter[counterList[i]] > pivotValue:
                counterList[swapPointer], counterList[i] = counterList[i], counterList[swapPointer]
                swapPointer += 1
        #pivot swap
        counterList[swapPointer], counterList[high] = counterList[high], counterList[swapPointer]
        
        #binary search conditions
        numbersGreaterThanEqualToPivot = swapPointer - low + 1
        if numbersGreaterThanEqualToPivot==k:
            return (counterList[:swapPointer+1])
        elif numbersGreaterThanEqualToPivot<k:
            low = swapPointer + 1
            k = k - numbersGreaterThanEqualToPivot
        else:
            high = swapPointer - 1





from collections import Counter
print(topKFrequent(nums,k))
