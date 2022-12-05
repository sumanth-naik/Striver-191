
start = "AAAAACCC"
end = "AACCCCCC"
bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
'''

start = "AACCGGTT"
end = "AAACGGTA"
bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
'''
'''
start = "AACCGGTT"
end = "AACCGGTA"
bank = ["AACCGGTA"]
'''

def recursiveGeneMutation(start, end, bank, visited, minimumChanges, numChanges):
    if(start==end):
        minimumChanges[0] = min(minimumChanges[0], numChanges)
    for ch in ["A","C","G","T"]:
        for index in range(8):
            mutatedGene = start[0:index]+ch+start[index+1:]
            if(mutatedGene not in visited and mutatedGene in bank):
                visited.add(mutatedGene)
                recursiveGeneMutation(mutatedGene, end, bank, visited, minimumChanges, 1+numChanges)
                visited.remove(mutatedGene)
                
minimumChanges = [1e9]
recursiveGeneMutation(start, end, set(bank), set([start]), minimumChanges, 0)

if(minimumChanges[0]==1e9):
    print("-1")
else:
    print(minimumChanges[0])

'''
Back tracking is essentially DFS. In DFS we are forced to store the each path's visited
and update it while traversing (adding before recursion call and removing after recursion call)
This is because we are not guaranteed that the path we take firsst will be the minimum length path to that node
But here there is property of shortest path; If there is a shorter path and you can take it
you dont have to keep visited set for each path. You can have a visited set for enitre graph
since if you are in the shortest path to that node, you dont have to consider other paths to that node
Hence when Backtracking And Shortest Path property comes into picture => think BFS
'''

from collections import deque
def iteractiveBFSGeneMutations(start, end, bank, minChanges):
    visited = {start}
    queue = deque()
    queue.append((start,0))
    while(queue):
        current = queue.popleft()
        currentGene = current[0]
        currentNumChanges = current[1]
        if(currentGene == end):
            minChanges[0] = min(minChanges[0], currentNumChanges)
            break
        for ch in ["A","C","G","T"]:
            for index in range(8):
                mutatedGene = currentGene[0:index] + ch + currentGene[index+1:]
                if(mutatedGene not in visited and mutatedGene in bank):
                    visited.add(mutatedGene)
                    queue.append((mutatedGene, currentNumChanges+1))
                    

minimumChanges = [1e9]
iteractiveBFSGeneMutations(start, end, set(bank), minimumChanges)

if(minimumChanges[0]==1e9):
    print("-1")
else:
    print(minimumChanges[0])









