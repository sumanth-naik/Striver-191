#returns (repeating, missing)
def findRepeatingAndMissingNumber(arr):    
    
    missingXorRepeating = 0
    for i in range(0,len(arr)):
        missingXorRepeating = missingXorRepeating ^ (i+1) ^ arr[i]
        
    numberWithLSBAsOneInMissingXorRepeating = missingXorRepeating & ~(missingXorRepeating - 1)
    
    cumulativeXorOfArrElementsXoredToZero = 0
    cumulativeXorOfArrElementsXoredToOne = 0
    cumulativeXorOfActualNumbersXoredToZero = 0
    cumulativeXorOfActualNumbersXoredToOne = 0
    
    for i in range(0, len(arr)):
        if((missingXorRepeating ^ arr[i]) & numberWithLSBAsOneInMissingXorRepeating == 0):
            cumulativeXorOfArrElementsXoredToZero = cumulativeXorOfArrElementsXoredToZero ^ arr[i]
        else:
            cumulativeXorOfArrElementsXoredToOne = cumulativeXorOfArrElementsXoredToOne ^ arr[i]
        
        if((missingXorRepeating ^ (i+1)) & numberWithLSBAsOneInMissingXorRepeating == 0):
            cumulativeXorOfActualNumbersXoredToZero = cumulativeXorOfActualNumbersXoredToZero ^ (i+1) 
        else:
            cumulativeXorOfActualNumbersXoredToOne = cumulativeXorOfActualNumbersXoredToOne ^ (i+1) 
            
    num1 = cumulativeXorOfArrElementsXoredToZero ^ cumulativeXorOfActualNumbersXoredToZero
    num2 = cumulativeXorOfArrElementsXoredToOne ^ cumulativeXorOfActualNumbersXoredToOne
    
    for x in arr:
        if(num1==x):
            return (num1, num2)
        
    return (num2,num1)
    
arr = [3,4,2,5,1,6,6,9,8]
print(findRepeatingAndMissingNumber(arr))
