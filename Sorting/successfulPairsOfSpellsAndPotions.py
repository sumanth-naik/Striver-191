class Solution:
    def successfulPairs(self, spells, potions, success: int):
        n, m = len(spells), len(potions)
        sortedSpellsWithIndices, ansArr, potionIndex = sorted([(spell, index) for index, spell in enumerate(spells)]), [0]*n, m
        potions.sort()
        for spell, index in sortedSpellsWithIndices:
            while potionIndex-1>=0 and spell*potions[potionIndex-1]>=success: potionIndex-=1
            ansArr[index] = m-potionIndex
        return ansArr
            