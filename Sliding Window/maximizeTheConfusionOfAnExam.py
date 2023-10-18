class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # only False to True
        countOfFalsesChangesToTrue, maxConsecutiveTruesSeen = 0, 0
        right = left = 0
        while right<len(answerKey):
            if answerKey[right]=="F": countOfFalsesChangesToTrue += 1
            while countOfFalsesChangesToTrue>k:
                if answerKey[left]=="F": countOfFalsesChangesToTrue -= 1
                left += 1
            right += 1
            maxConsecutiveTruesSeen = max(maxConsecutiveTruesSeen, right-left)
        return maxConsecutiveTruesSeen
    


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        countOfFalsesChangesToTrue = countOfTruesChangesToTrue = maxConsecutiveSeen = 0
        right = leftOfTrues = leftOfFalses = 0

        while right<len(answerKey):
            if answerKey[right]=="F": countOfFalsesChangesToTrue += 1
            while countOfFalsesChangesToTrue>k:
                if answerKey[leftOfTrues]=="F": countOfFalsesChangesToTrue -= 1
                leftOfTrues += 1
            
            if answerKey[right]=="T": countOfTruesChangesToTrue += 1
            while countOfTruesChangesToTrue>k:
                if answerKey[leftOfFalses]=="T": countOfTruesChangesToTrue -= 1
                leftOfFalses += 1

            right += 1
            maxConsecutiveSeen = max(maxConsecutiveSeen, right-min(leftOfTrues, leftOfFalses))

        return maxConsecutiveSeen
    

    
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        countOfFalsesChangesToTrue = countOfTruesChangesToTrue = maxConsecutiveSeen = 0
        right = left = 0

        while right<len(answerKey):
            
            if answerKey[right]=="F": countOfFalsesChangesToTrue += 1
            else: countOfTruesChangesToTrue += 1

            # only move left till both are wrong
            while countOfFalsesChangesToTrue>k and countOfTruesChangesToTrue>k:
                if answerKey[left]=="F": countOfFalsesChangesToTrue -= 1
                else: countOfTruesChangesToTrue -= 1
                left += 1

            right += 1
            maxConsecutiveSeen = max(maxConsecutiveSeen, right-left)

        return maxConsecutiveSeen