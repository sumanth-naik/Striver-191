class Solution:
    def peakIndexInMountainArray(self, arr) -> int:
        low, high = 0, len(arr)-1
        while low<high:
            mid = (low+high)//2
            if mid+1==len(arr): return mid
            if arr[mid+1]>arr[mid]: low = mid+1
            elif arr[mid+1]<arr[mid]: high = mid
        return low