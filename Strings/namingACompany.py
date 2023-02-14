class Solution:
    def distinctNames(self, ideas):
        charSets = [set() for _ in range(26)]
        numCompanyNames = 0
        for idea in ideas:
            charSets[ord(idea[0]) - ord('a')].add(idea[1:])
        for i in range(26):
            for j in range(i+1, 26):
                numCommon = len(charSets[i] & charSets[j])
                numCompanyNames += 2*(len(charSets[i])-numCommon)*(len(charSets[j])-numCommon)
        return numCompanyNames