class Solution:
    def maxCompatibilitySum(self, students, mentors):
        m, n, numQuestions = len(students), len(mentors), len(students[0])
        dpArrOfCompatabilty = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                for k in range(numQuestions):
                    dpArrOfCompatabilty[i][j] += (1 if students[i][k]==mentors[j][k] else 0)
        
        maxCompatabilitySumSoFar = 0
        def bitMaskingBacktracking(studentIndex, bitmaskOfMentorsUsed, assignmentSumSoFar):
            nonlocal maxCompatabilitySumSoFar
            if studentIndex==m: 
                maxCompatabilitySumSoFar = max(maxCompatabilitySumSoFar, assignmentSumSoFar)
            else:
                for mentorIndex in range(n):
                    if not (bitmaskOfMentorsUsed & (1<<mentorIndex)):
                        bitMaskingBacktracking(studentIndex+1, bitmaskOfMentorsUsed | (1<<mentorIndex), assignmentSumSoFar+dpArrOfCompatabilty[studentIndex][mentorIndex])
        bitMaskingBacktracking(0, 0, 0)
        return maxCompatabilitySumSoFar