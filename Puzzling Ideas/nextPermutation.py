class Solution:
    def nextPermutation(self, arr: List[int]) -> None:
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

class Solution:
    def nextPermutation(self, arr: List[int]) -> None:
        # 4 2 3 5 2 1
        for peakIndex in range(len(arr)-1, 0, -1):
            # find first peak elem from last -> index 3
            if arr[peakIndex-1]<arr[peakIndex]:     
                # reverse from index 4 2 3 1 2 5
                right = lastIndex = len(arr)-1
                for left in range(peakIndex, (peakIndex+lastIndex)//2 + 1):
                    arr[left], arr[right] = arr[right], arr[left]
                    right -= 1
                # find first "strictly" greater element to the right of index and replace with pre-PeakElem
                # 4 2 5 1 2 3
                k = peakIndex
                while arr[k]<=arr[peakIndex-1]:
                    k += 1
                arr[k], arr[peakIndex-1] = arr[peakIndex-1], arr[k]
                return 
        return  arr.reverse()

