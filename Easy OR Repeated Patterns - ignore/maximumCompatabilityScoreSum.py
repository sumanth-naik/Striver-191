class Solution:
    def maxCompatibilitySum(self, students, mentors):
        n, numQuestions = len(students), len(students[0])
        dpArrOfCompatabilty = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(numQuestions):
                    dpArrOfCompatabilty[i][j] += int(students[i][k]==mentors[j][k])
        
        @cache
        def bitMaskingDp(studentIndex, usedMentorsMask):
            if studentIndex==n: 
                return 0
            return max([dpArrOfCompatabilty[studentIndex][mentorIndex] + bitMaskingDp(studentIndex+1, usedMentorsMask | (1<<mentorIndex)) \
                        for mentorIndex in range(n) if not (usedMentorsMask & (1<<mentorIndex))] , default=0)
        
        return bitMaskingDp(0, 0)