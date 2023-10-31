# Key Idea 1: Use Binary Search on answer
# Key Idea 2: Have a function which can sum from number A to number B
# Key Idea 3: subtract n from maxSum to make minNeeded as 0 instead of 1 for easier implementation. (This, ans will be low+1)

# Note: defining A, B is tricky. Take an example
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        
        # b(b+1)/2 - (a-1)(a-1+1)/2
        def sumFromAToB(a, b):
            return ((b-a+1)*(b+a))//2

        # 0 1 2 3 4 5 6 7 8 9 -> indices
        # 3 4 5 6 7 8 7 6 5 4 -> array
        def mountainSum(target):
            # (index) is the number of elements to left
            # (n-1 - index) is the number of elements to right
            return sumFromAToB(max(0, target - index), target) + \
                   sumFromAToB(max(0, target - (n-1 - index)), target) - \
                   target
            
        maxSum -= n # as good as making minNeeded as 0 instead of 1  for arr[i]
        low, high = 0, maxSum
        while low<high:
            mid = (low+high+1)//2
            if mountainSum(mid)<=maxSum:
                low = mid
            else:
                high = mid - 1
        return low + 1