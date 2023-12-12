#User function Template for python3

from functools import lru_cache
#Function to find the maximum possible amount of money we can win.
class Solution:
    def optimalStrategyOfGame(self,arr, n):
        # code here

        memo = {}
        
        @lru_cache(None)
        def dp(i, j):
            if i>=j: return [0,0]
            
            # if (i,j) not in memo:
                
            left, right = dp(i+1, j), dp(i, j-1)
            leftChoice = [arr[i] + left[0], left[1]]
            rightChoice = [arr[j] + right[0], right[1]]
            
            return leftChoice[::-1] if leftChoice[0]>rightChoice[0] else rightChoice[::-1]
        return dp(0, n-1)[-1]
            
            
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(2003)

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int,input().strip().split()))
        ob = Solution()
        print(ob.optimalStrategyOfGame(arr,n))

# } Driver Code Ends