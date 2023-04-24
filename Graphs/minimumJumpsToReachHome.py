from collections import deque
class Solution:
    def minimumJumps(self, forbidden, a: int, b: int, x: int) -> int:
        queue, visited, forbidden, maxPos = deque(), set(), set(forbidden), max(x, max(forbidden)) + a + b
        # pos, lastMoveWasBackward, numSteps
        queue.append((0, False, 0))
        visited.add((0, False))
        visited.add((0, True))

        while queue:
            pos, lastMoveWasBackward, numSteps = queue.popleft()
            if pos==x: return numSteps
            if pos+a<=maxPos and pos+a not in forbidden and (pos+a, False) not in visited:
                queue.append((pos+a, False, numSteps+1)) 
                visited.add((pos+a, False))
                visited.add((pos+a, True))
            if pos-b<=maxPos and not lastMoveWasBackward and pos-b>0 and pos-b not in forbidden and (pos-b, True) not in visited: 
                queue.append((pos-b, True, numSteps+1)) 
                visited.add((pos-b, True))

        return -1