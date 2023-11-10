# Key Idea: At each person, take or not take [min function is on key bit_count()]

# Optimization: take only if they add a new skill
# Note 1: In take case, we need to add person =>  | (1<<person)
# Note 2: Base case is where we take every person

class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:

        skillToIndexMap = {skill:index for index, skill in enumerate(req_skills)}
        personSkillsMasks = [reduce(lambda acc, skill: acc|(1<<skillToIndexMap[skill]), skills, 0) for skills in people]
        finalBitMask = (1<<len(req_skills)) - 1

        @lru_cache(None)
        def bitMaskingDp(index, skillsMask):
            if skillsMask==finalBitMask: return 0
            if index==len(people): return (1<<len(people))-1 # Note 2
            notTake = bitMaskingDp(index+1, skillsMask)
            if personSkillsMasks[index]|skillsMask != skillsMask: # Optimization
                take = bitMaskingDp(index+1, personSkillsMasks[index]|skillsMask) | (1<<index) # Note 1
                return min(take, notTake, key = lambda x: x.bit_count())
            return notTake

        minPeopleMask = bitMaskingDp(0, 0)
        return [personIndex for personIndex in range(len(people)) if minPeopleMask & (1<<personIndex)]

    

# Key Idea: Given skillsMask, what is the minPeopleMask needed? [min function is on minPeopleMask.bit_count()]

# Note 1: In take case, we need to add person =>  | (1<<person)
# Note 2: Base case is where we take every person
# Note 3: take only if person adds a new skill, else inf loop

class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:

        skillToIndexMap = {skill:index for index, skill in enumerate(req_skills)}
        personSkillsMasks = [reduce(lambda acc, skill: acc|(1<<skillToIndexMap[skill]), skills, 0) for skills in people]

        @cache
        def bitMaskingDp(skillsMask):
            if not skillsMask: return 0
            minPeopleMask = (1<<len(people))-1  # Note 2
            for person in range(len(people)):
                remainingMask = skillsMask & ~personSkillsMasks[person]
                if remainingMask!=skillsMask: # Note 3                                # Note 1
                    minPeopleMask = min(minPeopleMask, bitMaskingDp(remainingMask) | (1<<person), key = lambda x: x.bit_count())
            return minPeopleMask

        minPeopleMask = bitMaskingDp((1<<len(req_skills)) - 1)
        return [personIndex for personIndex in range(len(people)) if minPeopleMask & (1<<personIndex)]



# Key Idea: minimum in qn => BFS, starting with no skills. Each level deeper in BFS corresponds to one person added.
# Brute Force BFS

from collections import deque
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:

        skillToIndexMap = {skill:index for index, skill in enumerate(req_skills)}
        personSkillsMasks = [reduce(lambda acc, skill: acc|(1<<skillToIndexMap[skill]), skills, 0) for skills in people]
        finalBitMask, queue, visited = (1<<len(req_skills)) - 1, deque([(0, 0)]), set()

        while True:
            skillsMask, peopleIdsMask = queue.popleft()
            if skillsMask==finalBitMask: return [personIndex for personIndex in range(len(people)) if peopleIdsMask & (1<<personIndex)]
            for personId, personSkillMask in enumerate(personSkillsMasks):
                if personSkillMask|skillsMask not in visited:
                    visited.add(personSkillMask|skillsMask)
                    queue.append((personSkillMask|skillsMask, peopleIdsMask | (1<<personId)))


# Key Idea: BFS on number of skills left. Start with skillIndexToPeopleMap. Prioritize skills with least number of people.

# Note: bitmaksing made it very complicated. Can do with simple set.

from collections import deque
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:

        skillToIndexMap = {skill:index for index, skill in enumerate(req_skills)}
        personSkillsMasks = [reduce(lambda acc, skill: acc|(1<<skillToIndexMap[skill]), skills, 0) for skills in people]
        skillIndexToPeopleMap = defaultdict(int)
        for personId, skills in enumerate(people):
            for skill in skills:
                skillIndexToPeopleMap[skillToIndexMap[skill]] |= (1<<personId)

        queue = deque([(skillIndexToPeopleMap, 0)])
        while queue:
            skillIndexToPeopleMap, peopleMask = queue.popleft()
            peopleWithMostDemandingSkillMask = min(list(skillIndexToPeopleMap.values()), key = lambda x: x.bit_count())
            for person in range(len(people)): 
                if (1<<person) & peopleWithMostDemandingSkillMask:
                    remainingSkills = {skillIndex:people for skillIndex, people in skillIndexToPeopleMap.items() if not (1<<skillIndex) & personSkillsMasks[person]}
                    if len(remainingSkills)==0: return [personIndex for personIndex in range(len(people)) if (peopleMask | (1<<person)) & (1<<personIndex)]
                    queue.append((remainingSkills, peopleMask | (1<<person)))












