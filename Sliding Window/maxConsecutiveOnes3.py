class Solution:
    def longestOnes(self, nums, k: int) -> int:
        # window is always the size of max window seen so far with atmost k zeroes
        numZeroesInWindow, sizeOfMaxWindowSeenSoFar = 0, 0

        for index in range(len(nums)):
            if nums[index]==0: 
                numZeroesInWindow += 1
            if numZeroesInWindow>k:
                # if there are more than k zeroes, we slide the window right by one (by removing the left most number in window) 
                # update numZeroesInWindow is applicable... only after we see that in future is there is case where
                # numZeroesInWindow<=k, we are going to increase the size of the window
                # The difference between this and normal sliding window where we pop all elements on left from current window till we see a 0 is that
                # we dont decrease the window size by popping all till left most 0, but we drag along that max window sized window and update 
                # number of zeroes in the window just in case there is a bigger window that we can see in future 
                #    right-left+1 = range = sizeOfWindowWeWant + 1
                # => left = right-sizeOfWindowWeWant
                if nums[index-sizeOfMaxWindowSeenSoFar]==0: numZeroesInWindow -= 1
            else:
                sizeOfMaxWindowSeenSoFar += 1
        return sizeOfMaxWindowSeenSoFar