nums = [4,-2,-3,4,1]



def sumOfSubarrayRanges(nums):
   
    maxArray = []
    minArray = []

    sumOfAllRanges = 0
    sumOfAllRangesEndingAtIndex = 0
    for index, num in enumerate(nums):
        maxArray.append(num)
        minArray.append(num)
        i = index - 1
        while i>=0 and (maxArray[i]<num or minArray[i]>num):
            sumOfAllRangesEndingAtIndex -= abs(maxArray[i] - minArray[i])
            if maxArray[i]<num:
                maxArray[i] = num
            if minArray[i]>num:
                minArray[i] = num
            sumOfAllRangesEndingAtIndex += abs(maxArray[i] - minArray[i])
            i -= 1

        sumOfAllRanges += sumOfAllRangesEndingAtIndex
    return sumOfAllRanges

print(sumOfSubarrayRanges(nums))

