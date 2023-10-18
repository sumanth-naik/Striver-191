class Solution:
    def permute(self, arr: List[int]) -> List[List[int]]:
        allPermsArr, n = [], len(arr)
        
        def getPermutations(arr, startIndex, allPermsArr):
            if startIndex==n:
                allPermsArr.append(deepcopy(arr))
            for i in range(startIndex, n):
                arr[i], arr[startIndex] = arr[startIndex], arr[i]
                getPermutations(arr, startIndex + 1, allPermsArr)
                arr[i], arr[startIndex] = arr[startIndex], arr[i]
        
        getPermutations(arr, 0, allPermsArr)
        return allPermsArr
        

class Solution:
    def permute(self, arr: List[int]) -> List[List[int]]:
        return [[num] + others for index, num in enumerate(arr) for others in self.permute(arr[:index]+arr[index+1:])] or [[]]