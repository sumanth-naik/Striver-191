class Solution:
    def minimumTime(self, time, totalTrips: int) -> int:
        left, right = 1, pow(10, 14)
        while left<right:
            mid = (left+right)//2
            tripsWithMidAsTime = 0
            for timeOfBus in time:
                tripsWithMidAsTime += (mid//timeOfBus)
                if tripsWithMidAsTime>=totalTrips: break
            if tripsWithMidAsTime>=totalTrips: 
                right = mid
            else:
                left = mid + 1
        return right
