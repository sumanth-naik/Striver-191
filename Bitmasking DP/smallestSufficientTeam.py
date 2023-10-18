class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:

        skillToIndexMap = {skill:index for index, skill in enumerate(req_skills)}
        peopleSkillsBitMasks = []
        for skills in people:
            bitMask = 0
            for skill in skills:
                bitMask |= (1<<skillToIndexMap[skill])
            peopleSkillsBitMasks.append(bitMask)
        
        finalBitMask = 2**len(req_skills) - 1

        @lru_cache(None)
        def recursion(index, skillsMask):
            if skillsMask==finalBitMask: return 0
            if index==len(peopleSkillsBitMasks): return 1e9
            return min(1+recursion(index+1, peopleSkillsBitMasks[index]|skillsMask), recursion(index+1, skillsMask))

        return recursion(0, 0)
    
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:

        skillToIndexMap = {skill:index for index, skill in enumerate(req_skills)}
        peopleSkillsBitMasks = []
        for skills in people:
            bitMask = 0
            for skill in skills:
                bitMask |= (1<<skillToIndexMap[skill])
            peopleSkillsBitMasks.append(bitMask)
        
        finalBitMask = 2**len(req_skills) - 1

        @lru_cache(None)
        def recursion(index, skillsMask):
            if skillsMask==finalBitMask: return (0, [])
            if index==len(peopleSkillsBitMasks): return (1e9, [])
            if recursion(index+1, skillsMask)[0]<1+recursion(index+1, peopleSkillsBitMasks[index]|skillsMask)[0]:
                return recursion(index+1, skillsMask)
            return (1+recursion(index+1, peopleSkillsBitMasks[index]|skillsMask)[0], recursion(index+1, peopleSkillsBitMasks[index]|skillsMask)[1] + [index])

        return recursion(0, 0)[1]
    
from collections import deque
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:

        skillToIndexMap = {skill:index for index, skill in enumerate(req_skills)}
        peopleSkillsBitMasks = []
        for skills in people:
            bitMask = 0
            for skill in skills:
                bitMask |= (1<<skillToIndexMap[skill])
            peopleSkillsBitMasks.append(bitMask)
        
        finalBitMask, queue, visited = 2**len(req_skills) - 1, deque([(0, [])]), set()

        while True:
            skillsMask, peopleIds = queue.popleft()
            if skillsMask==finalBitMask: return peopleIds
            for personId, personSkillMask in enumerate(peopleSkillsBitMasks):
                if personSkillMask|skillsMask not in visited:
                    visited.add(personSkillMask|skillsMask)
                    queue.append((personSkillMask|skillsMask, [personId]+peopleIds))

