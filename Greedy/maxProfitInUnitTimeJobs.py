#User function Template for python3
import heapq
class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,jobs,n):
        jobs.sort(key=lambda x:x.deadline)
        numJobs, maxProfit, heap, index, nextDeadline = 0, 0, [], n-1, 0
        printJobs(jobs)
        while index>=0:
            currDeadline = jobs[index].deadline

            #add future deadline jobs which are in heap if you can in extra slots if you can
            numExtraSlots = nextDeadline - currDeadline - 1
            while heap and numExtraSlots>=1:
                maxProfitJobWithFutureDeadline = heapq.heappop(heap)
                maxProfit -= maxProfitJobWithFutureDeadline
                numJobs += 1
                numExtraSlots -= 1

            #add all elements with currentDeadline to heap
            while index>=0 and jobs[index].deadline==currDeadline:
                currDeadlineProfit = jobs[index].profit
                heapq.heappush(heap, -currDeadlineProfit)
                index -= 1
            
            #add max profit job in this slot   
            maxProfitJobWithAnyDeadline = heapq.heappop(heap)
            maxProfit -= maxProfitJobWithAnyDeadline
            numJobs += 1
            
            nextDeadline = currDeadline

        #add jobs till deadline = 0
        currDeadline = 0
        numExtraSlots = nextDeadline - currDeadline - 1
        while heap and numExtraSlots>=1:
            maxProfitJobWithFutureDeadline = heapq.heappop(heap)
            maxProfit -= maxProfitJobWithFutureDeadline
            numJobs += 1
            numExtraSlots -= 1
        return (numJobs, maxProfit)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha
class Job:
    '''
    Job class which stores profit and deadline.
    '''
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0

if __name__ == '__main__':
    test_cases = 1
    # for cases in range(test_cases) :
    #     info = [(1,1,100),(1,4,1),(1,4,2),(1,5,2),(1,5,2)]
    #     n = len(info)
    #     Jobs = [Job() for i in range(n)]
    #     for i in range(n):
    #         # Jobs[i].id = info[3*i]
    #         # Jobs[i].deadline = info[3 * i + 1]
    #         # Jobs[i].profit=info[3*i+2]
    #         Jobs[i].id = info[i][0]
    #         Jobs[i].deadline = info[i][1]
    #         Jobs[i].profit=info[i][2]
    #     ob = Solution()
    #     def printJobs(jobs):
    #         for job in Jobs:
    #             print(job.id, job.deadline, job.profit)
    #     # printJobs(Jobs)
    #     res = ob.JobScheduling(Jobs,n)
    #     print (res[0], end=" ")
    #     print (res[1])
    for cases in range(test_cases) :
        n = 79
        s = "1 23 400 2 100 143 3 31 191 4 64 291 5 30 140 6 5 23 7 63 137 8 91 443 9 97 403 10 99 28 11 62 463 12 87 114 13 10 486 14 73 489 15 73 468 16 67 248 17 19 218 18 42 1 19 8 406 20 44 489 21 45 48 22 63 359 23 36 305 24 53 284 25 8 4 26 64 221 27 66 250 28 35 328 29 36 359 30 16 60 31 26 135 32 7 396 33 52 401 34 97 112 35 6 392 36 100 202 37 91 315 38 61 326 39 19 213 40 9 326 41 16 124 42 99 34 43 74 85 44 61 461 45 43 176 46 72 121 47 10 31 48 16 14 49 31 264 50 25 236 51 55 76 52 37 445 53 90 497 54 22 361 55 62 83 56 38 277 57 6 436 58 10 431 59 20 170 60 91 315 61 98 263 62 35 359 63 93 450 64 72 75 65 66 496 66 10 220 67 72 98 68 17 313 69 47 138 70 73 8 71 72 211 72 84 278 73 46 446 74 8 18 75 67 451 76 32 164 77 65 266 78 23 209 79 67 394"
        info = list(map(int,s.strip().split()))
        Jobs = [Job() for i in range(n)]
        for i in range(n):
            Jobs[i].id = info[3*i]
            Jobs[i].deadline = info[3 * i + 1]
            Jobs[i].profit=info[3*i+2]

        ob = Solution()
        def printJobs(jobs):
            for job in Jobs:
                print(job.id, job.deadline, job.profit)
        # printJobs(Jobs)
        res = ob.JobScheduling(Jobs,n)
        print (res[0], end=" ")
        print (res[1])
# } Driver Code Ends

