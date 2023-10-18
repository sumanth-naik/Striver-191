class Solution:
    def countPairs(self, n: int, edges, queries):

        degreeArr = [0 for _ in range(n+1)]
        numEdgesMap = defaultdict(int)
        for u, v in edges:
            degreeArr[u] += 1
            degreeArr[v] += 1
            numEdgesMap[(min(u,v), max(u,v))] += 1

        
        sortedDegrees = sorted(degreeArr)
        
        for query in queries:
            count  = 0
            low, high = 1, n
            while low<high:
                if sortedDegrees[low] + sortedDegrees[high] > query:
                    count += (high - low)
                    high -= 1
                else:
                    low += 1
            for u, v in numEdgesMap.keys():
                if degreeArr[u] + degreeArr[v] - numEdgesMap[(min(u,v), max(u,v))]<=query<degreeArr[u] + degreeArr[v]:
                    count -= 1
            yield count

'''
https://leetcode.com/problems/count-pairs-of-nodes/solutions/1096740/c-java-python3-two-problems-o-q-n-e/
 
It helps to solve two problems independently.

cnt[i] is the count of edges for node i.
shared[i][j] is the count of shared edges between nodes i and j (if exists), where i < j.

How many node pairs i and j are there, so that cnt[i] + cnt[j] is greater than q?
    We can solve it in O(n) by sorting counts (sorted_cnt) and usign two-pointer approach.
How many connected node pairs are there, so that cnt[i] + cnt[j] is greater than q, but cnt[i] + cnt[j] - shared[i][j] is not?
    We can solve it in O(e) as there are no more than e connected node pairs.
The result is [1] - [2]. Pairs in [2] were incldued in [1] but they should not.


'''