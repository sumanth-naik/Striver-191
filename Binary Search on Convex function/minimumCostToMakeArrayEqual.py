# TotalCost(x) = sum(cost[i] * (abs(nums[i])-x))
# let nums be sorted for simplicity and are n_1, n_2, n_3, .... n_m
# let n_k<x<n_k+1
# TotalCost(x) = c_1(x - n_1) + c_2(x - n_2) + ... + c_k(x - n_k) + c_k+1(n_k+1 - x) + ... + c_m(n_m - x)
# TotalCost(x) = x[(c_1 + c_2 + .. + c_k) - (c_k+1 + ... + c_m)] + 
#  [ -(c_1*n_1 + c_2*n_2 + .. + c_k*n_k) + (c_k+1*n_k+1 + ... + c_m*n_m)] 
# x is positive since its given that every num is positive
# derivative of Totalcost(x) = [(c_1 + c_2 + .. + c_k) - (c_k+1 + ... + c_m)] 
# Lets analyse this function
# Think x as a slider on number line and analyse TotalCost(x)
# let (c_1 to c_k) belong to set1 and (c_k+1 to c_m) belong to set2
# if x is small, there will be less of set1 and more of set2 (remember n_k < x < n_k+1)
# if x is medium, there will be equal of set1 and set2
# if x is large, there will be more of set1 and less of set2
# Hence, derivative will be negative at first(since [small set sum] - [large set sum] is <0), slowly moving to 0, then positive
# Hence original function (TotalCost(x)) will be dipping down(negative derivative) at first and then shooting up(positive derivative)

class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        
        def getCost(need):
            return sum(abs(num-need)*cost[index] for index, num in enumerate(nums))
        
        low, high, minCostSeen = min(nums), max(nums), 1e20
        while low<high:
            mid = (low+high)//2
            midCost, nextCost = getCost(mid), getCost(mid+1)
            minCostSeen = min(minCostSeen, midCost, nextCost)
            if midCost<=nextCost:
                high = mid
            else:
                low = mid+1
        return minCostSeen if minCostSeen!=1e20 else 0



# derivative [(c_1 + c_2 + .. + c_k) - (c_k+1 + ... + c_m)] 
# derivative >= 0 when (c_1 + c_2 + .. + c_k)>=(c_k+1 + ... + c_m)
# find index when first part cumulative sum is greater than second part
# sum1 >= sum2 where sum1+sum2 = sum(costArray)
#                   => sum2 = sum(costArray) - sum1
# => sum1 >= sum(costArray) - sum1
# => 2*sum1 >= sum(costArray)

# Ref : https://leetcode.com/problems/minimum-cost-to-make-array-equal/solutions/2734091/Pivot-vs.-W-Median-vs.-Binary-Search/
# Why one of the values in nums is the answer?
# Well, you say, if our array is [2, 5], what if we can achieve min cost by making them 3 or 4?
# For this to be the case, the cost for both 2 and 5 must be the same. But if the cost the same, we can achieve the same min cost if we pick 2 or 5.

class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        totalCost, cumSum = sum(cost), 0
        for bestIndex in sorted(range(len(nums)), key=lambda x:nums[x]): # sort indices wrt nums values
            cumSum += cost[bestIndex]
            if 2*cumSum>=totalCost:
                break
        return sum(abs(num-nums[bestIndex])*cost[index] for index, num in enumerate(nums))



