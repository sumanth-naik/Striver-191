from sortedcontainers import SortedList
class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        minHeapOfServerEndTimeAndServerNumber, availableServersSortedList, numRequestsArr = [], SortedList([index for index in range(k)]), [0]*k

        for requestIndex in range(len(arrival)):
            while minHeapOfServerEndTimeAndServerNumber and minHeapOfServerEndTimeAndServerNumber[0][0]<=arrival[requestIndex]:
                availableServersSortedList.add(heappop(minHeapOfServerEndTimeAndServerNumber)[1])
            if not availableServersSortedList: 
                continue
            offset = requestIndex%k
            index = bisect_left(availableServersSortedList, offset)
            if index==len(availableServersSortedList):
                index = 0
            serverNum = availableServersSortedList[index]
            numRequestsArr[serverNum] += 1
            availableServersSortedList.remove(serverNum)
            heappush(minHeapOfServerEndTimeAndServerNumber, (arrival[requestIndex]+load[requestIndex], serverNum))

        maxReqs = max(numRequestsArr)
        return [server for server in range(k) if numRequestsArr[server]==maxReqs]

from sortedcontainers import SortedList
class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        minHeapOfServerEndTimeAndServerNumber, availableServersSortedList, numRequestsArr = [], SortedList([index for index in range(k)]), [0]*k

        for requestIndex in range(len(arrival)):
            while minHeapOfServerEndTimeAndServerNumber and minHeapOfServerEndTimeAndServerNumber[0][0]<=arrival[requestIndex]:
                availableServersSortedList.add(heappop(minHeapOfServerEndTimeAndServerNumber)[1])
            if availableServersSortedList: 
                index = bisect_left(availableServersSortedList, requestIndex%k) % len(availableServersSortedList)
                serverNum = availableServersSortedList.pop(index)
                numRequestsArr[serverNum] += 1
                heappush(minHeapOfServerEndTimeAndServerNumber, (arrival[requestIndex]+load[requestIndex], serverNum))

        maxReqs = max(numRequestsArr)
        return [server for server in range(k) if numRequestsArr[server]==maxReqs]


class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        before, after, reqs, busy = list(range(k)), [], [0]*k, []

        for reqIndex in range(len(arrival)):
            serverIndex = reqIndex%k
            if serverIndex==0:
                after, before = before, []
            
            while busy and busy[0][0]<=arrival[reqIndex]:
                serverNum = heappop(busy)[1]
                if serverNum<serverIndex: heappush(before, serverNum)
                else: heappush(after, serverNum)
            
            usePQ = after if after else before
            if usePQ:
                serverNum = heappop(usePQ)
                reqs[serverNum] += 1 
                heappush(busy, (arrival[reqIndex]+load[reqIndex], serverNum))
        
        maxReqs = max(reqs)
        return [serverNum for serverNum, reqCount in enumerate(reqs) if reqCount==maxReqs]

                    