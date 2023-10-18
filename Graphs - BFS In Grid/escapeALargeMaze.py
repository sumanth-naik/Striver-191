from typing import List
class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        blocked = set(tuple(block) for block in blocked)
        def dfs(x, y, visited, need):
            if (x, y) in blocked or not(0<=x<10**6 and 0<=y<10**6) or (x, y) in visited: return False
            visited.add((x, y))
            if len(visited)>19900 or (x, y)==need: return True
            return dfs(x+1, y, visited, need) or dfs(x, y+1, visited, need) or dfs(x-1, y, visited, need) or dfs(x, y-1, visited, need)

        return dfs(source[0], source[1], set(), tuple(target)) and dfs(target[0], target[1], set(), tuple(source)) 
    
# can check manhatten distance as well instead of area, but thats slower